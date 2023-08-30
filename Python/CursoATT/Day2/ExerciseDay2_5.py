#Clases y Sobrecargas

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self, other):
        print('Hola soy', self.nombre, ', Hola amigo', other.nombre)


juanito = Persona('Juanito',28)
pepe = Persona('Pepe', 32)

c = juanito + pepe
#juanito.saludar()
