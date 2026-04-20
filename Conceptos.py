¿Qué es la POO y por qué usarla?
Conceptos Fundamentales
La Programación Orientada a Objetos es como organizar una cocina real. En lugar de tener ingredientes sueltos y utensilios por separado (programación tradicional), agrupamos todo en "objetos" que tienen sus propias características y comportamientos.
Analogía del mundo real:
•	Clase = El molde o plantilla (ej: el plano de un carro)
•	Objeto = La instancia concreta (ej: mi carro rojo específico)
python
# Versión sin POO (difícil de mantener)
nombre_coche1 = "Toyota"
color_coche1 = "Rojo"
velocidad_coche1 = 0

nombre_coche2 = "Honda"
color_coche2 = "Azul"
velocidad_coche2 = 0

def acelerar(velocidad, incremento):
    return velocidad + incremento

# ¿Qué pasa si tenemos 100 coches? ¡Imposible de manejar!

# Versión con POO (limpio y organizado)
class Coche:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.velocidad = 0
    
    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"{self.nombre} ahora va a {self.velocidad} km/h")

coche1 = Coche("Toyota", "Rojo")
coche2 = Coche("Honda", "Azul")
coche1.acelerar(50)  # Toyota ahora va a 50 km/h
Beneficios de la POO:
1.	Organización: El código se agrupa lógicamente
2.	Reutilización: No repites código (hereda y extiende)
3.	Mantenimiento: Cambiar algo en un lugar afecta todo el sistema de forma controlada
4.	Escalabilidad: Puedes añadir nuevas funcionalidades sin romper lo existente

