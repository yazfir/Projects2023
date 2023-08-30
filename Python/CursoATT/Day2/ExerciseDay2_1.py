#Clases y Sobrecargas

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print('Hola soy', self.nombre)


juanito = Persona('Juanito',28)

juanito.saludar()
juanito.saludar('Pepe')