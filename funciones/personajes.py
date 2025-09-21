class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, agilidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.agilidad = agilidad
    def saludar(self):
        print(f"Hola,{self.nombre} como estas?")
personaje1 = Personaje("Aragorn", 80, 70, 60)
personaje2 = Personaje("Legolas", 60, 80, 90)   
personaje3 = Personaje("Gimli", 90, 50, 40)
personaje4 = Personaje("Gandalf", 50, 100, 70)
personaje5 = Personaje("Frodo", 30, 60, 80)
personaje6 = Personaje("Sam", 40, 50, 70)
print(personaje1.nombre, personaje1.fuerza, personaje1.inteligencia, personaje1.agilidad)
print(personaje2.nombre, personaje2.fuerza, personaje2.inteligencia, personaje2.agilidad)
print(personaje3.nombre, personaje3.fuerza, personaje3.inteligencia, personaje3.agilidad)
print(personaje4.nombre, personaje4.fuerza, personaje4.inteligencia, personaje4.agilidad)
print(personaje5.nombre, personaje5.fuerza, personaje5.inteligencia, personaje5.agilidad)
print(personaje6.nombre, personaje6.fuerza, personaje6.inteligencia, personaje6.agilidad)

print(personaje1.saludar())
print(personaje2.saludar())
print(personaje3.saludar())
print(personaje4.saludar())
print(personaje5.saludar())
print(personaje6.saludar())