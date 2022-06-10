class Vehiculos():
    
    def __init__(self, marca, modelo):
        self.marca=marca#constructor
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):#método
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", 
        self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculos):
    
    hcaballito=""#propiedad
    def caballito(self):
        self.hcaballito="Voy haciendo caballito"
    
    def estado(self):#método
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", 
        self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)

        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True

   
#Instancias
miMoto=Moto("Honda", "CBR")
 
miMoto.caballito()#Llamado al método

miMoto.estado() #El segundo estado (Moto) anula el estado de clase vehiculo

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))

class BicicletaElectrica(Vehiculos):
    pass

miBici=BicicletaElectrica("Marca x", "Modelo X")
#Cuando hay herencia múltiple se da preferencia a la clase
#que se indique primero, entonces se pasan los parámentros
#del constructor de VElectricos (ninguno)
miBici.estado()
