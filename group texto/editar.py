try:
    archivo = open("datos.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
except:
    print("no hay registro que editar")
    if len(lineas) == 0:
        print("no hay registro para editar")
    for numero, lineas in enumerate(lineas, 1):
        datos = lineas.strip().split(",")
        print(f"registro #{numero} . {lineas[0]} - {datos[1]}")
    print()
numero_registro =input("ingrese el numero de registro a editar: ")
numero_registro = int(numero_registro)
if numero_registro < 1 or numero_registro > len(lineas):
    print("numero de registro no valido")
    exit()
    datos_actuales = lineas[numero_registro - 1].strip().split(",")
    print(f"Datos actuales del registro #{numero_registro}")
    print(f"Nombre: {datos_actuales[0]}")
    print(f"Apellido: {datos_actuales[1]}")
    print("ingrense los datos")
    
nuevo_nombre = input("Nombre: ")
nuevo_apellido = input("Apellido: ")
nuevo_edad = input("Edad: ")
lineas[numero_registro - 1] = nuevo_nombre + "," + nuevo_apellido + "," + nuevo_edad + "\n"
archivo = open("datos.txt", "w")
archivo.writelines(lineas)
archivo.close()
print("Registro editado con éxito")