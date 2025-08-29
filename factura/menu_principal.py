import sys
from typing import List, Dict
from inventario import (
    agregar_producto, listar_productos, buscar_producto_id,
    buscar_producto_nombre, actualizar_producto, eliminar_producto
)
from facturas import (
    crear_factura, listar_facturas, obtener_factura,
    actualizar_factura, eliminar_factura, IVA
)

def pausa():
    input("\nPresiona ENTER para continuar...")

def leer_flotante(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje).replace(",", "."))
        except ValueError:
            print("Ingresa un número válido.")

def leer_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingresa un número entero válido.")

def menu_inventario():
    while True:
        print("\n=== INVENTARIO ===")
        print("1) Agregar producto")
        print("2) Listar productos")
        print("3) Buscar por ID")
        print("4) Buscar por nombre")
        print("5) Actualizar precio/stock")
        print("6) Eliminar producto")
        print("0) Volver")
        opcion = input("Selecciona una opción: ").strip()
        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                precio = leer_flotante("Precio: ")
                stock = leer_entero("Stock: ")
                prod = agregar_producto(nombre, precio, stock)
                print("Agregado:", prod)
                pausa()
            elif opcion == "2":
                filas = listar_productos()
                if not filas:
                    print("No hay productos.")
                else:
                    print("\nID | Nombre | Precio | Stock")
                    for p in filas:
                        print(f"{p['id']:>2} | {p['nombre']} | {p['precio']:.2f} | {p['stock']}")
                pausa()
            elif opcion == "3":
                pid = leer_entero("ID del producto: ")
                p = buscar_producto_id(pid)
                print(p if p else "No encontrado.")
                pausa()
            elif opcion == "4":
                nombre = input("Nombre (o parte): ")
                res = buscar_producto_nombre(nombre)
                if not res:
                    print("Sin coincidencias.")
                else:
                    for p in res:
                        print(p)
                pausa()
            elif opcion == "5":
                pid = leer_entero("ID del producto a actualizar: ")
                cambio_precio = input("¿Actualizar precio? (s/n): ").lower() == "s"
                precio = leer_flotante("Nuevo precio: ") if cambio_precio else None
                cambio_stock = input("¿Actualizar stock? (s/n): ").lower() == "s"
                stock = leer_entero("Nuevo stock: ") if cambio_stock else None
                actualizado = actualizar_producto(pid, precio, stock)
                print("Actualizado:", actualizado)
                pausa()
            elif opcion == "6":
                pid = leer_entero("ID del producto a eliminar: ")
                ok = eliminar_producto(pid)
                print("Eliminado" if ok else "No se encontró el producto.")
                pausa()
            elif opcion == "0":
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print("Error:", e)
            pausa()

def _leer_items() -> List[Dict]:
    items = []
    print("\nAñade ítems (deja ID vacío para terminar):")
    while True:
        pid_str = input("ID producto: ").strip()
        if pid_str == "":
            break
        try:
            pid = int(pid_str)
        except ValueError:
            print("ID inválido.")
            continue
        cantidad = leer_entero("Cantidad: ")
        items.append({"id_producto": pid, "cantidad": cantidad})
    return items

def menu_facturas():
    while True:
        print("\n=== FACTURAS ===")
        print("1) Crear nueva factura")
        print("2) Listar facturas")
        print("3) Ver detalle de factura")
        print("4) Editar factura")
        print("5) Eliminar factura")
        print("0) Volver")
        opcion = input("Selecciona una opción: ").strip()
        try:
            if opcion == "1":
                cliente = input("Cliente: ")
                items = _leer_items()
                if not items:
                    print("Factura no creada.")
                else:
                    fac = crear_factura(cliente, items)
                    print("Factura creada:", fac["id"])
                pausa()
            elif opcion == "2":
                facs = listar_facturas()
                if not facs:
                    print("No hay facturas.")
                else:
                    print("\nID | Fecha | Cliente | Subtotal | IVA | Total")
                    for f in facs:
                        print(f"{f['id']:>2} | {f['fecha']} | {f['cliente']} | {f['subtotal']:.2f} | {f['iva']:.2f} | {f['total']:.2f}")
                pausa()
            elif opcion == "3":
                fid = leer_entero("ID de factura: ")
                f = obtener_factura(fid)
                if not f:
                    print("No encontrada.")
                else:
                    print(f"\nFactura #{f['id']} | {f['fecha']} | Cliente: {f['cliente']}")
                    for it in f['items']:
                        print(f" - {it['nombre']} (#{it['id_producto']}) x{it['cantidad']} @ {it['precio_unitario']:.2f} = {it['total_linea']:.2f}")
                    print(f"Subtotal: {f['subtotal']:.2f}")
                    print(f"IVA ({IVA*100:.0f}%): {f['iva']:.2f}")
                    print(f"TOTAL: {f['total']:.2f}")
                pausa()
            elif opcion == "4":
                fid = leer_entero("ID de factura: ")
                cambio_cliente = input("¿Cambiar cliente? (s/n): ").lower() == "s"
                nuevo_cliente = input("Nuevo cliente: ") if cambio_cliente else None
                cambio_items = input("¿Cambiar ítems? (s/n): ").lower() == "s"
                nuevos_items = _leer_items() if cambio_items else None
                actualizar_factura(fid, nuevos_items, nuevo_cliente)
                print("Factura actualizada.")
                pausa()
            elif opcion == "5":
                fid = leer_entero("ID de factura a eliminar: ")
                ok = eliminar_factura(fid)
                print("Eliminada" if ok else "No se encontró la factura.")
                pausa()
            elif opcion == "0":
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print("Error:", e)
            pausa()

def menu_listas():
    print("\n=== DEMOSTRACIÓN DE LISTAS EN PYTHON ===")
    lista = ["jose", "maria", "pedro", "miguel", "ivan", "laura"]
    numeros = [5, 2, 9, 1, 7, 3, 8]
    print("Lista inicial:", lista)
    lista.insert(0, "pedro sanchez")
    lista.append("pedro pablo")
    lista.extend(["luis", "carlos", "marta"])
    print("Después de insertar y agregar:", lista)
    lista.remove("maria")
    lista.pop(2)
    print("Después de eliminar:", lista)
    copia = lista.copy()
    ordenada = sorted(lista)
    print("Copia:", copia)
    print("Ordenada:", ordenada)
    lista.reverse()
    print("Invertida:", lista)
    lista4 = ["a", "a", "b", "c", "a"]
    print("Cantidad de 'a' en lista4:", lista4.count("a"))
    combinada = lista + numeros
    print("Lista combinada:", combinada)
    print("Primeros 3 nombres:", lista[:3])
    print("Últimos 2 nombres:", lista[-2:])
    cuadrados = [x**2 for x in numeros]
    print("Cuadrados:", cuadrados)
    pausa()

def main():
    while True:
        print("\n=== SISTEMA DE INVENTARIO Y FACTURACIÓN ===")
        print("1) Inventario")
        print("2) Facturas")
        print("3) Demostración de listas en Python")
        print("0) Salir")
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            menu_inventario()
        elif opcion == "2":
            menu_facturas()
        elif opcion == "3":
            menu_listas()
        elif opcion == "0":
            print("Hasta luego")
            sys.exit(0)
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
