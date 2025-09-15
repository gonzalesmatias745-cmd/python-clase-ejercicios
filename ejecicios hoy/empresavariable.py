class empresa:
    def __init__(self, nombre, empleados, ubicacion):
        self.nombre = nombre
        self.empleados = empleados
        self.ubicacion = ubicacion

empresa1 = empresa("Tech Solutions", 100, "Medellín")
print(empresa1.nombre)
print(empresa1.empleados)
print(empresa1.ubicacion)