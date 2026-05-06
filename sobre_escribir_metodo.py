#Herencia básica
class Padre:
    def saludar(self):
        return "Hola desde Padre"

class Hijo(Padre):  # Hereda de Padre
    pass  # No necesita redefinir el método

h = Hijo()
print(h.saludar())  # "Hola desde Padre"

#class Hijo(Padre):
    def saludar(self):  # Sobrescribe el método
        return "Hola desde Hijo"

h = Hijo()
print(h.saludar())  # "Hola desde Hijo"
#Usar super() para extender el método padre
class Padre:
    def saludar(self):
        return "Hola"

class Hijo(Padre):
    def saludar(self):
        mensaje_padre = super().saludar()  # Llama al método padre
        return f"{mensaje_padre} desde Hijo"

h = Hijo()
print(h.saludar())  # "Hola desde Hijo"

#Herencia múltiple
class A:
    def metodo(self):
        return "Método de A"

class B:
    def metodo(self):
        return "Método de B"

class C(A, B):  # Hereda de A y B
    pass

c = C()
print(c.metodo())  # "Método de A" (hereda del primero en la lista)
