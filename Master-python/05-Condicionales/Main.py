#Condicional: es una estructura de control que permite controlar el flujo del programa.
"""
#condicional IF

Si se_cumple_esta_condicion:
    ejecutar grupo de instrucciones
Si NO:
    Se ejecutan otro grupo de instrucciones


ejemplo

if condicion:
    instrucciones
else:
    otras instrucciones


# Operadores de comparacion
== igual que 
!= distinto que
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadore logicos

and Y
or O
! negation
not NO

"""

#   Ejemplo  1

print(" ")
print("######################### EJEMPLO 1 #########################")
print(" ")
color = "rojo"

if color == "rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("El color NO es ROJO")


#   Ejemplo  2

print("\n######################### EJEMPLO 2 #########################")
print(" ")

#color = input("Adivina cual es mi color Favorito?:")
#color = rojo
if color == "rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("El color incorrecto")


#   Ejemplo  3

print("\n######################### EJEMPLO 3 #########################")
print(" ")

year = 2020
#year = int(input("En que año estamos?:"))

if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")


#   Ejemplo  4

print("\n######################### EJEMPLO 4 #########################")
print(" ")

nombre  = "Marcos Astudillo"
ciudad = "Santiago"
continente = "America"
edad = 35
mayoria_edad = 18

if edad >= mayoria_edad:
    #instrucciones
    print(f"{nombre} es mayor de edad!!.")
    if continente != "America":
        print("El usuario no es Americano")
    else:
        print(f"tambien es Americano y vive en {ciudad}.")
else:
    print(f"{nombre} No es mayor de edad.")


#   Ejemplo  5

print("\n######################### EJEMPLO 5 #########################")
print(" ")

#dia = int(input("introduce el día de la semana: "))
dia = 4

if dia == 1:
    print("El día es Lunes.")
elif dia == 2:
    print("El día es Martes.")
elif dia == 3:
    print("El día es Miercoles.")
elif dia == 4:
    print("El día es Jueves.")
elif dia == 5:
    print("El día es Viernes.")
elif dia == 6:
    print("El día es Sabado.")
elif dia == 7:
    print("El día es Domingo.")
else:
    print("No corresponde a un día de la semana.")


#   Ejemplo  6

print("\n######################### EJEMPLO 6 #########################")
print(" ")

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("Tienes edad de trabajar? \nIntroduce tu edad:"))
edad_oficial = 25

if edad_oficial >= 18 and edad_oficial <= edad_maxima:
    print("Se encuentra en edad de trabajar.")
else: 
    print("No se encuentra en edad de trabajar.")


#   Ejemplo  7

print("\n######################### EJEMPLO 7 #########################")
print(" ")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un Pais de habla hispana!!!.")
else:
    print(f"{pais} no es un pais de habla hispana.")


#   Ejemplo  8

print("\n######################### EJEMPLO 8 #########################")
print(" ")

pais = "España"

#con el operador not se puede comprobar si algo NO corresponde a la condicion indicada

if not (pais == "Mexico" and pais == "España" and pais == "Colombia"):
    print(f"{pais} No es un Pais de habla hispana!!!.")
else:
    print(f"{pais} SI es un pais de habla hispana.")



#   Ejemplo  9

print("\n######################### EJEMPLO 9 #########################")
print(" ")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} No es un Pais de habla hispana!!!.")
else:
    print(f"{pais} SI es un pais de habla hispana.")