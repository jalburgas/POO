class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def descripcion(self):
        print(f"{self.nombre} es un pokemon de tipo {self.tipo}")


class Pikachu(Pokemon):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
    
    def ataque(self):
        return f"{self.nombre} tipo de ataque {self.tipo}"


class Charmander(Pokemon):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)


# Crear el objeto Pikachu con nombre "Boby" y tipo "eléctrico"
boby_pikachu = Pikachu("Boby", "eléctrico")

# Probar los métodos
boby_pikachu.descripcion()
print(boby_pikachu.ataque())
