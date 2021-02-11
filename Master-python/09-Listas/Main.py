"""
    Listas(Arrays)
    Son colecciones o conjuntos de datos/Valores, bajo un unico nombre.
    Para acceder a esos valores podemos usar un indice númerico.
"""

pelicula = "Batman"
#Definir una lista
peliculas = ["Batman", "Spiderman", "Harry Potter"] #listas normal o array
cantantes = list(("Metallica", "Iron Maiden", "Megadeth")) #lista con tuplas
years = list(range(2020,2050)) #lista de años por rango
variada = ["Marcos", 30, 4.4, True,"Texto"]
"""
print(pelicula)
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

#Indices
"""
print(peliculas[1])
print(peliculas[-2]) #llama al indice inverso, en este caso -1 es harry potter y -2 spiderman y -3 batman
print(cantantes[0:1]) #sirve para sacar los elementos por rangos segun uno necesite
print(peliculas[1:]) #saca todos los elementos a contar del indice 1 en adelante
"""

#para modificar un indice hacer lo siguiente:
peliculas[1] = "Iron Man" #indicar el indice a actualizar
#print(peliculas)

# Añadir elementos a una lista
cantantes.append("Los Bunkers")  #Agregando .append se agrega el valor que se quiera agregar a una lista
#print(cantantes)


#Recorrer lista con bucles
"""
print("#### Listado Peliculas ####")

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la Nueva Pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula) + 1} {pelicula}")
"""


# Listas Multidimensionales
print("\n #### Listado de contactos ####")
contactos = [
    [
        "Antonio",
        "antonio.ac86@hotmail.com"
    ],
    [
        "Lucia",
        "lucy.as2018@gmail.com"
    ],
    [
        "Paulina",
        "pauli.sp87@gmail.com"
    ]
]
"""
for contacto in contactos:
    for elemento in contacto:
        if contacto.index( elemento ) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")
"""
#print(contactos[1][1])