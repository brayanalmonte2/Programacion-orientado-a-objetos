class vehiculo:
    def __init__ (self, ruedas, marca, color):
        self.ruedas = ruedas
        self.marca = marca
        self. color = color 

class autos(vehiculo):
    def __init__ (self,ruedas,marca,color,puertas):
        super().__init__(ruedas,marca,color)
        self.puertas = puertas
        self.estado = False
        self.marcha = None

    def encendido (self):
        self.estado = True
        if self.estado == True:
            print(f"Vehiculo {self.marca} encendido")

    def apagado (self):
        self.estado = False
        if self.estado == False :
             print(f"Vehiculo {self.marca} a pagado")
    
    def acelerar (self):
        self.marcha = True
        if self.marcha == True:
            print(f"El vehiculo {self.marca}, esta acelerando")
    
    def frenos (self):
        self.marcha = False
        if self.marcha == False :
            print(f"Frenando vehiculo {self.marca}")
    
    def detalles (self):
        print(f"detalles del vehiculo: Marca:{self.marca}, Color:{self.color}, Ruedas:{self.ruedas}, Puertas:{self.puertas}, Estado:{self.estado}, Marcha:{self.marcha}")

Coche1=autos(4,"Toyota","azul",4)
Coche1.encendido()
Coche1.acelerar()
Coche1.frenos()
Coche1.apagado()
Coche1.detalles()