2. Clases y Objetos en profundidad
¿Qué es una clase exactamente?
Una clase es como un molde o blueprint. Define qué atributos (características) y métodos (comportamientos) tendrán los objetos creados a partir de ella.
python
# Definición de una clase
class Estudiante:
    """Esta clase representa a un estudiante universitario"""
    
    # Atributo de clase (compartido por TODOS los estudiantes)
    universidad = "Universidad Nacional"
    
    # Constructor: se ejecuta automáticamente al crear un objeto
    def __init__(self, nombre, edad, carrera):
        # Atributos de instancia (cada objeto tiene los suyos)
        self.nombre = nombre      # self se refiere al objeto actual
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []  # Lista vacía para cada estudiante
    
    # Método de instancia
    def estudiar(self, horas):
        print(f"{self.nombre} está estudiando por {horas} horas")
    
    def agregar_calificacion(self, nota):
        self.calificaciones.append(nota)
        print(f"Nota {nota} agregada a {self.nombre}")
    
    def promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

# Creando objetos (instancias)
estudiante1 = Estudiante("Ana García", 20, "Ingeniería")
estudiante2 = Estudiante("Carlos Ruiz", 22, "Medicina")

# Cada objeto tiene sus propios datos
print(estudiante1.nombre)  # Ana García
print(estudiante2.nombre)  # Carlos Ruiz

# Pero comparten atributos de clase
print(estudiante1.universidad)  # Universidad Nacional
print(estudiante2.universidad)  # Universidad Nacional

# Modificar atributo de clase afecta a todos
Estudiante.universidad = "Universidad Politécnica"
print(estudiante1.universidad)  # Universidad Politécnica

# Comportamientos individuales
estudiante1.agregar_calificacion(95)
estudiante1.agregar_calificacion(87)
estudiante2.agregar_calificacion(78)

print(f"Promedio de Ana: {estudiante1.promedio()}")   # 91.0
print(f"Promedio de Carlos: {estudiante2.promedio()}") # 78.0
¿Qué es self exactamente?
self es una referencia al objeto actual. Cuando llamas a un método, Python automáticamente pasa el objeto como primer argumento.
python
class ExplicacionSelf:
    def metodo_normal(self):
        print(f"self es: {self}")
        print(f"El tipo de self es: {type(self)}")

# Al crear un objeto
obj = ExplicacionSelf()
obj.metodo_normal()
# self es: <__main__.ExplicacionSelf object at 0x...>
# El tipo de self es: <class '__main__.ExplicacionSelf'>

# Lo que Python hace internamente:
ExplicacionSelf.metodo_normal(obj)  # Es equivalente a obj.metodo_normal()
Regla importante: El primer parámetro de los métodos de instancia SIEMPRE es self (puedes llamarlo de otra forma, pero NO lo hagas).
