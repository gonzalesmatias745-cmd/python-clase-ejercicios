class animal:
    def __init__(self, especie, edad, color):
        self.especie = especie
        self.edad = edad
        self.color = color

animal1 = animal("Perro", 5, "Marrón")
print(animal1.especie)
print(animal1.edad)
print(animal1.color)
