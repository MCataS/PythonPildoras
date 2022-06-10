nombreUsuario=input("_Introduce tu nombre de usuario: ")
print("El nombre es: ", nombreUsuario.capitalize())

edad=input("Introduce edad: ")
#Crear un bucle para comprobar si es un digito y no se rompa el programa
while(edad.isdigit()==False):

    print("Por favor introduce un valor numérico")

    #Dentro se solicita el valor de la edad

    edad=input("Introduce edad: ")

#En python todo lo que se tome por input es string
if (int(edad)<18): #Siempre compararse con valo numérico

    print("No puede pasar")

else:

    print("Puede pasar")