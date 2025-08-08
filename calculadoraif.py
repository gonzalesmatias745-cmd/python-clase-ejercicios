a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
print("calculadora")
print("Seleccione una opción:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
opcion = int(input("Ingrese su opción: "))
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