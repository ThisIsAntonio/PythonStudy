"""

"""

cantantes = ["Metallica", "Iron Maiden", "Megadeth", "Satirycon"]
numeros = [ 1, 2, 5, 8, 3, 4]

#Ordenar
print( numeros )
numeros.sort() #Metodo para ordenar una lista
print(numeros)

#Añadir elementos a una lista
cantantes.append("Los Bunkers")
print(cantantes)

cantantes.insert(5, "Los prisioneros") #con insert se debe indicar en que indice se quiere agregar el nuevo elemento a la lista
print(cantantes)

#Eliminar elementos
cantantes.pop(3) #Elimina el valor de la lista segun el indice indicado
print(cantantes)

cantantes.remove("Iron Maiden") #Elimina el valor segun el nombre indicado dentro de los parentecis
print(cantantes)

#Da la vuelta a la lista
print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de una lista
print("Los Bunkers" in cantantes) #con el "in" se sabe si existe un valor buscado dentro de una lista 

#Contar elementos de una lista
print(len(cantantes))

#Cuenta cuantas veces aparece un elemento en la lista
numeros.append(8)
print(numeros.count(8))

#Conseguir indice
print(cantantes.index("Los Bunkers"))

#Unir listas
cantantes.extend(numeros)
print(cantantes)