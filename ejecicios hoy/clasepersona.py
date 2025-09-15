class producto:
    def __format__(self, formato):
        if formato == "precio":
            return f"El precio del producto es: {self.precio}"