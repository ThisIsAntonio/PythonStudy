nombre = "Marcos Astudillo"

#Funciones generales
print(nombre) #funcion para imprimir en pantalla
print(type(nombre)) #Type es para saber que tipo de datos es

comprobar = isinstance(nombre, str) #detectar el tipado
if comprobar:
    print("Esa variable es un string")
else:
    print("Es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

#Limpiar espacios
frase = "               mi contenido    "
print(frase)
print(frase.strip())

#eliminar variables
year = 2022
print(year)
del year
#print(year)

#Comprobar variable vacia
texto = " ff   "
if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("la variable tiene contenido", len(texto))

#Encontrar caracteres
frase = "la vida es bella"
print(frase.find("bella"))

#Reemplazar palabras en string
nueva_frase = frase.replace("vida", "muerte")
print(nueva_frase)

#Mayusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())