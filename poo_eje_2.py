print(" ")
print("alexa guadalupe ramirez manzo 3-w 1205")
print(" ")
class Cuenta:   #nombre de la clase 
    def __init__(self, titular, cantidad=0.0):  #funsion para el titular, cantidad
        self.titular, self.cantidad = titular, cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}") #funsion para introdusir

    def ingresar(self, cantidad):
        if cantidad > 0: self.cantidad += cantidad # funsion para sumar la cantidad y dar un igual

    def retirar(self, cantidad):
        if cantidad > 0: self.cantidad -= cantidad #funsion para retirar

cuenta1 = Cuenta("alexa manzo", 11000.00)  #cuenta para sumar los numeros ingresados
cuenta1.mostrar()
cuenta1.ingresar(155)
cuenta1.mostrar()
cuenta1.retirar(640)
cuenta1.mostrar()
