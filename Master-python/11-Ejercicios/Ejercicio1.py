"""
    Crear un programa con una lista de 8 numeros enteros y haga lo siguiente:
        1. recorrer la lista y mostrarla
        2. hacer una funcion que recorra listas de numeros y devuelva un string
        3. ordenarla y mostrarla
        4. mostrar su longitud
        5. buscar algun elemento (que el usuario pida por teclado)
"""

#Crear una lista

numeros = [13,64,52, 73, 21, 7, 91, 63]

#Crear funcion que recorra lista y devuelva string

def mostrarLista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemento " + str(elemento)
        resultado += "\n"
    return resultado
    
#Recorrer y mostrar lista
"""
print("#### RECORRER Y MOSTRAR ####")
for numero in numeros:
    print(numero)
"""

#Llamado de funcion par mostrar lista en string
"""
print("#### FUNCION MOSTRAR LISTA ####")

print(mostrarLista(numeros))
"""

#Ordenar lista y mostrar
"""
print("\n#### MOSTRAR LISTA ORDENADA ####")
numeros.sort()
print(mostrarLista(numeros))
"""

#Longitud de lista
"""
print("\n#### MOSTRAR LONGITUD ####")
print(len(numeros))
"""

#Busqueda de la lista
print("\n#### Busqueda de la lista ####")
busqueda = int(input("Introduce un número:"))
comprobar = isinstance(busqueda,int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce un número:"))
else:
    print(f"Has introducido el {busqueda}")

print(f"Buscar en la lista el número {busqueda} ")
search = numeros.index(busqueda)
print (f"El número buscado existe en la lista, y es el indice {search}")
