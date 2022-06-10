class Coche():
    def desplazamiento(self): #método o comportamiento
        print("Me desplazo usando cuatro ruedas")

class Moto():
    def desplazamiento(self): #método o comportamiento
        print("Me desplazo usando dos ruedas")

class Camion():
    def desplazamiento(self): #método o comportamiento
        print("Me desplazo usando seis ruedas")
#
#miVehiculo=Moto()
#miVehiculo.desplazamiento()

#miVehiculo2=Coche()
#miVehiculo2.desplazamiento()

#miVehiculo3=Camion()
#miVehiculo3.desplazamiento()

#Para evitar el código anterior
#Crear método/funcion (recibe objeto por parametro)
def desplazamientoVehiculo(vehiculo):
    #usa el objeto que recibe por parametro para llamar al método desplazamiento
    vehiculo.desplazamiento()
#miVehiculo es de tipo Camion
miVehiculo=Camion()
#uso el metodo desplazamientoVehiculo y le paso por parametro el objeto de tipo camión
desplazamientoVehiculo(miVehiculo)
#el objeto miVehiculo se almacena dentro de vehiculo, entonces se trasforma en un objeto de tipo camion
#