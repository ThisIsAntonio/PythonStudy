"""
Una variable es un contenedor de información 
que dentro guardará un dato, se pueden crear 
muchas variables y que cada una tenga un dato distinto.
"""
#Crear variables y asignar un valor
texto = "Máster en Python"
texto2 = "Con Marcos Astudillo"
numero = 45
decimal = 6.7
#mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)
print ("-----------------------")
#mostrar valor de las variables/Reasignando valores
numero = 77
decimal = 8.9

print(numero)
print(decimal)

print ("-----------------------")
#Concatenación
nombre = "Marcos"
apellido = "Astudillo"
web = "ThisIsAntonio.com"

print(nombre + " " + apellido + " " + web) #metodo concatenado
print(f"{nombre} {apellido} - {web}") #metodo concatenado funcion variable
print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellido,web)) #metodo format donde en las llaves iran las variables del .format
print(nombre,apellido,web)

