from typing import List, Dict, Optional
from datetime import datetime
from almacenamiento import (
    leer_jsonl, escribir_jsonl, agregar_jsonl,
    ARCHIVO_FACTURAS, ARCHIVO_INVENTARIO
)

IVA = 0.19


def _cargar_inventario_idx() -> Dict[int, Dict]:
    inventario = leer_jsonl(ARCHIVO_INVENTARIO)
    return {p["id"]: p for p in inventario}

def _escribir_inventario_desde_idx(idx: Dict[int, Dict]) -> None:
    productos_ordenados = [idx[k] for k in sorted(idx.keys())]
    escribir_jsonl(ARCHIVO_INVENTARIO, productos_ordenados)

def _validar_disponibilidad(idx_inv: Dict[int, Dict], items: List[Dict]) -> None:
    for it in items:
        pid = int(it["id_producto"])
        cantidad = int(it["cantidad"])
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0.")
        prod = idx_inv.get(pid)
        if not prod:
            raise ValueError(f"Producto id {pid} no existe.")
        if int(prod.get("stock", 0)) < cantidad:
            raise ValueError(
                f"Stock insuficiente para '{prod.get('nombre','?')}' (ID {pid}). "
                f"Disponible: {prod.get('stock',0)}, requerido: {cantidad}."
            )

def _aplicar_movimiento_stock(idx_inv: Dict[int, Dict], items: List[Dict], signo: int) -> None:
    for it in items:
        pid = int(it["id_producto"])
        cantidad = int(it["cantidad"])
        prod = idx_inv.get(pid)
        if not prod:
            raise ValueError(f"Producto id {pid} no existe.")
        nuevo_stock = int(prod.get("stock", 0)) + (signo * cantidad)
        if nuevo_stock < 0:
            raise ValueError(
                f"Movimiento dejaría stock negativo en ID {pid} ('{prod.get('nombre','?')}')."
            )
        prod["stock"] = nuevo_stock


def _siguiente_id_factura(facturas: List[Dict]) -> int:
    return (max([f.get("id", 0) for f in facturas], default=0) + 1) if facturas else 1

def _recalcular_totales(factura: Dict) -> Dict:
    subtotal = sum(item["cantidad"] * item["precio_unitario"] for item in factura.get("items", []))
    iva = round(subtotal * IVA, 2)
    total = round(subtotal + iva, 2)
    factura["subtotal"] = round(subtotal, 2)
    factura["iva"] = iva
    factura["total"] = total
    return factura

def listar_facturas() -> List[Dict]:
    return leer_jsonl(ARCHIVO_FACTURAS)

def obtener_factura(fid: int) -> Optional[Dict]:
    for f in leer_jsonl(ARCHIVO_FACTURAS):
        if f.get("id") == int(fid):
            return f
    return None

def crear_factura(cliente: str, items: List[Dict]) -> Dict:
    facturas = leer_jsonl(ARCHIVO_FACTURAS)
    inv_idx = _cargar_inventario_idx()

    _validar_disponibilidad(inv_idx, items)

    items_norm = []
    for it in items:
        pid = int(it["id_producto"])
        cantidad = int(it["cantidad"])
        prod = inv_idx[pid]
        items_norm.append({
            "id_producto": pid,
            "nombre": prod["nombre"],
            "cantidad": cantidad,
            "precio_unitario": float(prod["precio"]),
            "total_linea": round(cantidad * float(prod["precio"]), 2)
        })

    _aplicar_movimiento_stock(inv_idx, items_norm, signo=-1)
    _escribir_inventario_desde_idx(inv_idx)

    factura = {
        "id": _siguiente_id_factura(facturas),
        "cliente": cliente.strip(),
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": items_norm
    }
    _recalcular_totales(factura)
    agregar_jsonl(ARCHIVO_FACTURAS, factura)
    return factura

def actualizar_factura(fid: int, nuevos_items: Optional[List[Dict]] = None, nuevo_cliente: Optional[str] = None) -> Dict:
    facturas = leer_jsonl(ARCHIVO_FACTURAS)
    inv_idx = _cargar_inventario_idx()

    objetivo = None
    for f in facturas:
        if f["id"] == int(fid):
            objetivo = f
            break
    if objetivo is None:
        raise ValueError("Factura no encontrada.")


    items_anteriores = list(objetivo.get("items", []))


    _aplicar_movimiento_stock(inv_idx, items_anteriores, signo=+1)

    try:
        if nuevos_items is not None:
            _validar_disponibilidad(inv_idx, nuevos_items)

            items_norm = []
            for it in nuevos_items:
                pid = int(it["id_producto"])
                cantidad = int(it["cantidad"])
                prod = inv_idx[pid]
                items_norm.append({
                    "id_producto": pid,
                    "nombre": prod["nombre"],
                    "cantidad": cantidad,
                    "precio_unitario": float(prod["precio"]),
                    "total_linea": round(cantidad * float(prod["precio"]), 2)
                })
            _aplicar_movimiento_stock(inv_idx, items_norm, signo=-1)
            objetivo["items"] = items_norm
        else:
            _aplicar_movimiento_stock(inv_idx, items_anteriores, signo=-1)

        if nuevo_cliente is not None:
            objetivo["cliente"] = nuevo_cliente.strip()


        _recalcular_totales(objetivo)
        _escribir_inventario_desde_idx(inv_idx)
        escribir_jsonl(ARCHIVO_FACTURAS, facturas)
        return objetivo

    except Exception as e:
        try:
            _aplicar_movimiento_stock(inv_idx, items_anteriores, signo=-1)
            _escribir_inventario_desde_idx(inv_idx)
        except Exception as e:
            print("Error al revertir cambios en el inventario:", e)
            pass
        raise e

def eliminar_factura(fid: int) -> bool:
    """
    - Restaura stock de los items de la factura.
    - Elimina la factura.
    """
    facturas = leer_jsonl(ARCHIVO_FACTURAS)
    inv_idx = _cargar_inventario_idx()

    objetivo = None
    restantes = []
    for f in facturas:
        if f.get("id") == int(fid):
            objetivo = f
        else:
            restantes.append(f)

    if objetivo is None:
        return False

    # 1) Reponer stock de esa factura
    _aplicar_movimiento_stock(inv_idx, objetivo.get("items", []), signo=+1)
    _escribir_inventario_desde_idx(inv_idx)

    # 2) Guardar facturas sin la eliminada
    escribir_jsonl(ARCHIVO_FACTURAS, restantes)
    return True
