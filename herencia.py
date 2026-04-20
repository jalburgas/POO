#¿Qué es la herencia?

#La herencia es un mecanismo que permite crear una nueva clase (clase hija) a partir de una clase existente (clase padre), heredando sus atributos y métodos.
#Sintaxis básica
#python

class Padre:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

class Hijo(Padre):  # Hereda de Padre
    pass  # Por ahora, igual que el padre

#Tipos de herencia
#1. Herencia simple

#Una clase hija hereda de una sola clase padre.
#python

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau!")  # Sobrescribe el método

mi_perro = Perro("Rex")
print(mi_perro.nombre)  # Rex (heredado)
mi_perro.hacer_sonido()  # Guau guau!

#2. Herencia múltiple

#Una clase puede heredar de múltiples clases padre.
#python

class Volador:
    def volar(self):
        print("Puedo volar")

class Nadador:
    def nadar(self):
        print("Puedo nadar")

class Pato(Volador, Nadador):
    def __init__(self, nombre):
        self.nombre = nombre

pato = Pato("Donald")
pato.volar()  # Puedo volar
pato.nadar()  # Puedo nadar

Método super()

#Permite llamar métodos de la clase padre:
#python

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Soy {self.nombre}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llama al constructor padre
        self.carrera = carrera
    
    def presentarse(self):
        return f"{super().presentarse()}, estudio {self.carrera}"

estudiante = Estudiante("Ana", 20, "Informática")
print(estudiante.presentarse())  # Soy Ana, estudio Informática

#Sobrescritura de métodos
#python

class Vehiculo:
    def moverse(self):
        return "El vehículo se mueve"

class Coche(Vehiculo):
    def moverse(self):
        return "El coche conduce por la carretera"

class Avion(Vehiculo):
    def moverse(self):
        return "El avión vuela por el cielo"

vehiculos = [Vehiculo(), Coche(), Avion()]
for v in vehiculos:
    print(v.moverse())
# Salida:
# El vehículo se mueve
# El coche conduce por la carretera
# El avión vuela por el cielo

#Orden de resolución de métodos (MRO)

#Python usa el MRO para determinar qué método llamar en herencia múltiple:
#python

class A:
    def metodo(self):
        print("Método de A")

class B(A):
    def metodo(self):
        print("Método de B")

class C(A):
    def metodo(self):
        print("Método de C")

class D(B, C):
    pass

d = D()
d.metodo()  # Método de B (sigue el MRO)

print(D.__mro__)  # Ver el orden: (D, B, C, A, object)

#Casos prácticos
#Ejemplo completo: Sistema de empleados
#python

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def calcular_bono(self):
        return self.salario * 0.05  # 5% base

class Gerente(Empleado):
    def __init__(self, nombre, salario, equipo):
        super().__init__(nombre, salario)
        self.equipo = equipo
    
    def calcular_bono(self):
        return super().calcular_bono() + self.salario * 0.10  # 15% total

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje
    
    def calcular_bono(self):
        return self.salario * 0.12  # 12% para devs

# Uso
gerente = Gerente("Carlos", 50000, ["Ana", "Luis"])
dev = Desarrollador("Ana", 40000, "Python")

print(f"{gerente.nombre}: ${gerente.calcular_bono()}")  # Carlos: $7500
print(f"{dev.nombre}: ${dev.calcular_bono()}")          # Ana: $4800

#Ventajas de la herencia

    #Reutilización de código: No repites lógica común

    #Extensibilidad: Puedes añadir funcionalidad sin modificar código existente

    #Organización: Estructura jerárquica clara

    #Polimorfismo: Un mismo método puede comportarse diferente

#Buenas prácticas

    #Usa herencia para relaciones "es-un" (un perro es un animal)

    #Para relaciones "tiene-un", usa composición

    #No abuses de la herencia múltiple (puede complicar el código)

    #Documenta bien las clases y métodos sobrescritos


