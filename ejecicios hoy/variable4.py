class vehiculo:
    def __init__(self, marca, llantas, capacidad):
        self.marca = marca
        self.llantas = llantas
        self.capacidad = capacidad

carro1= vehiculo("Toyota", "rin6", 5)
print(carro1.marca)
print(carro1.llantas)
print(carro1.capacidad)