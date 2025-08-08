calc = ["1.sumar", "2.restar", "3.multiplicar", "4.dividir"]
print("calculadora")
print("Seleccione una opción:") 
for operacion in calc:
    print(operacion)
    for i in range(1, 5):
        if f"{i}." in operacion:
            opcion = i
opcion = int(input("Ingrese su opción: "))
a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
if opcion == 1:
    print("La suma es:", a + b)
elif opcion == 2:
    print("La resta es:", a - b)
elif opcion == 3:
    print("La multiplicación es:", a * b)
elif opcion == 4:
    if b != 0:
        print("La división es:", a / b)
    else:
        print("Error: División por cero no permitida.")
else:
    print("Opción inválida.")