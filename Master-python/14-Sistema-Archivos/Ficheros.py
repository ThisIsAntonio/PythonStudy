"""
    Creador de archivos con un import, abrir o modificar
    a+ son permisos para el fichero
"""
from io import open
import pathlib #creador o sirve para abrir el archivo que se creara
#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/Fichero_texto.txt"
#print(ruta)
archivo = open(ruta,  "a+")
"""
#Escribir dentro del archivo
archivo.write("\n***** Soy un texto metido desde python *****\n")

#Cerrar archivo
archivo.close()
"""
#Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/Fichero_texto.txt"
#print(ruta)
archivo_lectura = open(ruta,  "r")


"""
Dos formas de leer contenidos
"""
#Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

#leer contenido y guardar en la lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
"""
#print(lista)
#split() es para hacer listas
for frase in lista:
    if not frase.isnumeric():
        print("-" + frase.upper())


for frase in lista:
    lista_frase = frase.split()
    print(lista_frase)

for frase in lista:
    print("-" + frase.capitalize())

for frase in lista:
    print("-" + frase.center(5))

"""

#Copiar un archivo, renombrar archivo, o eliminar archivo
import shutil

#Copiar

ruta_original = str(pathlib.Path().absolute()) + "/Fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/Fichero_copiado.txt"
ruta_alternativa = "../07-Ejercicios/Fichero_copiado77.txt"
ruta_alternativa2 = str(pathlib.Path().absolute()) + "/../07-Ejercicios/Fichero_copiado99.txt" "#Otra forma de copiar archivos indicando la ruta absoluta y agregando la devolucion de ruta"
#shutil.copyfile(ruta_original, ruta_nueva)
#shutil.copyfile(ruta_original, ruta_alternativa) #Copia el archivo nombrado y lo manda a la ruta solicitada
#shutil.copyfile(ruta_original, ruta_alternativa2)

#Mover y renombrar archivos archivos
"""
ruta_original = str(pathlib.Path().absolute()) + "/Fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/Fichero_copiado_nuevo.txt"
shutil.move(ruta_original, ruta_nueva)
"""

#Eliminar archivos
import os
ruta_nueva = str(pathlib.Path().absolute()) + "/Fichero_copiado_nuevo.txt"
#os.remove(ruta_nueva)

#Comprobar si existe
import os.path
print(os.path.abspath("./")) #muestra la ruta en la que nos encontramos

#ruta a comprobar
ruta_comprobar = os.path.abspath("./") + "/Fichero_texto.txt"
#print(ruta_comprobar)
if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("el archivo no existe")