estudiantes = {
    "Juan": {"notas": [4, 2.5, 4.5, 3, 1]},
    "Maria": {"notas": [8, 9, 10, 7, 8]},
    "Carlos": {"notas": [6, 7, 8, 9, 10]},
    "Ana": {"notas": [9, 8, 7, 10, 9]},
    "Luis": {"notas": [8, 7, 9, 10, 6]}
}


estudiantes["Juan"]["promedio"] = sum(estudiantes["Juan"]["notas"]) / len(estudiantes["Juan"]["notas"]) 
estudiantes["Maria"]["promedio"] = sum(estudiantes["Maria"]["notas"]) / len(estudiantes["Maria"]["notas"])
estudiantes["Carlos"]["promedio"] = sum(estudiantes["Carlos"]["notas"]) / len(estudiantes["Carlos"]["notas"])
estudiantes["Ana"]["promedio"] = sum(estudiantes["Ana"]["notas"]) / len(estudiantes["Ana"]["notas"])
estudiantes["Luis"]["promedio"] = sum(estudiantes["Luis"]["notas"]) /   len(estudiantes["Luis"]["notas"])


print(estudiantes["Juan"])
print(estudiantes["Maria"])
print(estudiantes["Carlos"])
print(estudiantes["Ana"])
print(estudiantes["Luis"])