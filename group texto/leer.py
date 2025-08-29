try:
 archivo = open("datos.txt", "r")
except:
 print("El archivo no existe. Por favor, cree el archivo primero.")
 exit()
lineas = archivo.readlines()
archivo.close() 
if len(lineas) == 0:
 print("El archivo está vacío")
else:
 print(f"se encontraron {len(lineas)} líneas:")
 for numero, lineas in enumerate(lineas,1):
  lineas_limpiar = lineas.strip()
  datos = lineas_limpiar.split(",")
  print(f"registro #{numero}:")
  print(f"Nombre: {datos[0]}")
  print(f"Apellido: {datos[1]}")
  print("fin de la información")