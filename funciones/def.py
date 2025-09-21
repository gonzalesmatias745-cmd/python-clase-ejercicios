class persona:
    def __init__(self, nombre, edad, apellido):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido

persona1 = persona("Juan", 30, "Pérez")
persona2 = persona("María", 25, "Gómez")
persona3 = persona("Luis", 40, "Rodríguez")
print(persona1.nombre)
print(persona2.nombre)
print(persona3.nombre)

persona1.nombre = "Carlos"
print(persona1.nombre)
