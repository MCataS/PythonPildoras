class Persona():
    def __init__(self, nombre, edad, Lugar_residencia):

        self.nombre=nombre

        self.edad=edad

        self.Lugar_residencia=Lugar_residencia

    def descripcion(self):

        print("Nombre: ", self.nombre, "\n Edad: ", self.edad, "\n Residencia: ", self.Lugar_residencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado): #parametros a pasar
        
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        #Esta llamando al método de la clase padre (persona)
        #Inicia los valores correspondientes y los almacena

        self.salario=salario
        
        self.antiguedad=antiguedad

    def descripcion(self): #reescribir descripción
        super().descripcion() #Llamado al método de la clase padre y lo ejecuta en su totalidad, 
                                #para luego seguir siguiente linea con salario y antigüedad
        print("Salario: ", self.salario, "\nAntigüedad: ", self.antiguedad)

Catalina=Empleado(800, 5, "Catalina", 31, "Colombia")
#Nombre de instancia
Catalina.descripcion()#Llama al método de la clase hijo (Empleado), pues el objeto Catalina es de tipo Empleado

print(isinstance(Catalina, Empleado))#Funcion que informa si un objeto es instancia de una clase 
#determinada (NombredeInstancia, Clase)