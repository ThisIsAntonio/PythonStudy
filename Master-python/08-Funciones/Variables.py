"""
    Variable local: es aquella que se encuentra disponible solo dentro de una funcion, a no ser que se 
    realice un return.
    Variable global: son aquellas que se encuentran disponibles tanto afuera de la funcion, asi como dentro
"""

frase = "Ni los genios son tan genios, noi los mediocres tan mediocres"

print(frase)

def holaMundo():
    frase = "hola mundo!!!"
    print("Dentro de la funcion")
    print(frase)

    year = 2021
    print(year)

    global website
    website = "thisisantonio.com"
    return "dato devuelto " + str(year)
holaMundo()
print(holaMundo())
print("Fuera: ", website)