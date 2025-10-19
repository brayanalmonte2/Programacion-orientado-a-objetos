#Creacion de la clase padre y sus atributos
class vehiculo:
    #Constructor de la clase
    def __init__ (self, ruedas, marca, color):
        self.ruedas = ruedas
        self.marca = marca
        self. color = color 
#Creaccion de la clase hijo y sus atributos
class autos(vehiculo):
    #Constructor de la clase
    def __init__ (self,ruedas,marca,color,puertas):
        #Funcion para llamar al construtor de la clase padre
        super().__init__(ruedas,marca,color)
        self.puertas = puertas
        self.estado = False
        self.marcha = None
    #Metodos
    #Metodo de encendido: enciende el auto
    def encendido (self):
        self.estado = True
        if self.estado == True:
            print(f"Vehiculo {self.marca} encendido")
    #Metodo de apagado: apaga el auto
    def apagado (self):
        self.estado = False
        if self.estado == False :
             print(f"Vehiculo {self.marca} a pagado")
    #Metodo de acelar: acelera el auto
    def acelerar (self):
        self.marcha = True
        if self.marcha == True:
            print(f"El vehiculo {self.marca}, esta acelerando")
    #Metodo de frenos: Frena al auto
    def frenos (self):
        self.marcha = False
        if self.marcha == False :
            print(f"Frenando vehiculo {self.marca}")
    #Este metodo proporciona informacion del vehiculo
    def detalles (self):
        print(f"detalles del vehiculo: Marca:{self.marca}, Color:{self.color}, Ruedas:{self.ruedas}, Puertas:{self.puertas}, Estado:{self.estado}, Marcha:{self.marcha}")
#ejecucion del programa
#Creacion del odjeto
Coche1=autos(4,"Toyota","azul",4)
Coche1.encendido()
Coche1.acelerar()
Coche1.frenos()
Coche1.apagado()
Coche1.detalles()