class Ninja:
    def __init__(self, nombre, aldea, rango):
        self.nombre = nombre
        self.aldea = aldea
        self.rango = rango
    
    def presentacion(self):
        print(f"{self.nombre} es un ninja de la aldea {self.aldea} con rango {self.rango}")


class Naruto(Ninja):
    def __init__(self, nombre, aldea, rango, tecnica_especial):
        super().__init__(nombre, aldea, rango)
        self.tecnica_especial = tecnica_especial
    
    def ataque(self):
        return f"{self.nombre} usa su técnica especial: {self.tecnica_especial} del estilo {self.rango}!"


class Sasuke(Ninja):
    def __init__(self, nombre, aldea, rango, sharingan):
        super().__init__(nombre, aldea, rango)
        self.sharingan = sharingan
    
    def ataque(self):
        return f"{self.nombre} activa el {self.sharingan} y usa Chidori!"


# Crear objeto de Naruto
naruto_uzumaki = Naruto("Naruto Uzumaki", "Hoja Oculta", "Hokage", "Rasengan")

# Probar métodos
naruto_uzumaki.presentacion()
print(naruto_uzumaki.ataque())

print("\n" + "="*50 + "\n")

# Crear otro objeto de Sasuke
sasuke_uchiha = Sasuke("Sasuke Uchiha", "Hoja Oculta", "Genin", "Sharingan de 3 Aspas")
sasuke_uchiha.presentacion()
print(sasuke_uchiha.ataque())
