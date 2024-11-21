print(" ")
print("alexa guadalupe ramirez manzo 3-w 1205")
print(" ")
class Persona: #nombre de la clase
    def __init__(self, nombre="", edad=0, DNI=""): #variable para el nombre edad y DNI 
        self.nombre, self.edad, self.DNI = nombre, edad, DNI

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.DNI}") #funsion para pedir 

    def esMayorDeEdad(self):
        return self.edad >= 18 #funsion para saber si es mayor de edad

persona1 = Persona("alexa", 15, "1205")
persona1.mostrar()
print(f"¿Es mayor de edad? {persona1.esMayorDeEdad()}") #funsiones para imprimir el nombre, edad y DNI y print para inpresion para saber si eres mayor de edad