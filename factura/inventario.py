from typing import List, Dict, Optional
from almacenamiento import leer_jsonl, escribir_jsonl, agregar_jsonl, ARCHIVO_INVENTARIO

def _siguiente_id(productos: List[Dict]) -> int:
    return (max([p.get("id", 0) for p in productos], default=0) + 1) if productos else 1

def agregar_producto(nombre: str, precio: float, stock: int) -> Dict:
    productos = leer_jsonl(ARCHIVO_INVENTARIO)
    for p in productos:
        if p["nombre"].strip().lower() == nombre.strip().lower():
            raise ValueError("Ya existe un producto con ese nombre.")
    prod = {
        "id": _siguiente_id(productos),
        "nombre": nombre.strip(),
        "precio": round(float(precio), 2),
        "stock": int(stock)
    }
    agregar_jsonl(ARCHIVO_INVENTARIO, prod)
    return prod

def listar_productos() -> List[Dict]:
    return leer_jsonl(ARCHIVO_INVENTARIO)

def buscar_producto_id(pid: int) -> Optional[Dict]:
    for p in leer_jsonl(ARCHIVO_INVENTARIO):
        if p.get("id") == int(pid):
            return p
    return None

def buscar_producto_nombre(nombre: str) -> List[Dict]:
    nombre = nombre.strip().lower()
    return [p for p in leer_jsonl(ARCHIVO_INVENTARIO) if nombre in p.get("nombre","").lower()]

def actualizar_producto(pid: int, precio: Optional[float] = None, stock: Optional[int] = None) -> Dict:
    productos = leer_jsonl(ARCHIVO_INVENTARIO)
    actualizado = None
    for p in productos:
        if p["id"] == int(pid):
            if precio is not None:
                p["precio"] = round(float(precio), 2)
            if stock is not None:
                p["stock"] = int(stock)
            actualizado = p
            break
    if actualizado is None:
        raise ValueError("Producto no encontrado.")
    escribir_jsonl(ARCHIVO_INVENTARIO, productos)
    return actualizado

def eliminar_producto(pid: int) -> bool:
    productos = leer_jsonl(ARCHIVO_INVENTARIO)
    antes = len(productos)
    productos = [p for p in productos if p.get("id") != int(pid)]
    escribir_jsonl(ARCHIVO_INVENTARIO, productos)
    return len(productos) < antes
