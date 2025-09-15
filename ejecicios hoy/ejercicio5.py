class persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

persona1= persona("Gonzalo", 19, "Buenos Aires")
print(persona1.nombre) 
print(persona1.edad)
print(persona1.ciudad)