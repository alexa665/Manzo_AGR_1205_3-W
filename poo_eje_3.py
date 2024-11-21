print(" ")
print("alexa guadalupe ramirez manzo 3-w 1205")
print(" ")
class Cuenta:
    def __init__(self, titular, cantidad=0.0):#funsion para la cantidad y el titular 
        self.titular, self.cantidad = titular, cantidad
    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.cantidad:.2f}")#funsion para la cantidad y el titular 

    def ingresar(self, cantidad):
        if cantidad > 0: self.cantidad += cantidad #funsion para ingresar

    def retirar(self, cantidad):
        if cantidad > 0: self.cantidad -= cantidad  #funsion para retirar

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)    #cuenta joven funsion para bonificasion
        self.bonificacion = bonificacion

    def esTitularValido(self, edad):
        return 18 <= edad < 25        #funsion para para validar
    
    def retirar(self, cantidad, edad):
        if self.esTitularValido(edad): super().retirar(cantidad)
        else: print("No válido para retirar.")                   #funsion para no validar 

    def mostrar(self):
        print(f"Cuenta Joven - Bonificación: {self.bonificacion}%")
        super().mostrar()      #funsion para dar una bonificasion
cuenta = CuentaJoven("alexa manzo", 11000.00, 6.7)     #suma de la cuenta
cuenta.mostrar()
cuenta.retirar(155, 50)
cuenta.mostrar()
cuenta.retirar(640, 70)
