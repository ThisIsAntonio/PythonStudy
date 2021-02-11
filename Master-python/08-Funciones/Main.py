"""
Funciones son basicamente un conjunto de instrucciones agrupadas bajo un nombre concreto
que pueden reutilizarse invocando a la funcion tantas veces como sea necesario

ejemplo

def nombreDeFuncion(parametros):
    #bloque de codigo / conjunto de instrucciones

nombreDeFuncion(mi_parametro) #se puede invocar todas las veces que uno quiera
"""

#Ejemplo 1

print("##### EJEMPLO 1 #####")

#definir funcion
def muestraNombres ():
    print("Marcos")
    print("Victor")
    print("Lucia")
    print("Paulina")
    print("Majo")
    print("Pablot")
    print("\n")

#invocar función

muestraNombres()
muestraNombres()
muestraNombres()

#Ejemplo 2

print("##### EJEMPLO 2 #####")

#Parametros


def mostrarTuNombre(nombre):
    print(f"Tu Nombre es: {nombre}")

mostrarTuNombre("Marcos Astudillo")
mostrarTuNombre("Paulina Silva")
mostrarTuNombre("Lucia Isidora")

#nombre = input("Introduce tu nombre:")
#mostrarTuNombre(nombre)

def mostrarTuNombre2(nombre, edad):
    print(f"Tu Nombre es: {nombre}")
    if edad >= 18:
        print("Ya eres mayor de edad")
#nombre = input("Introduce tu nombre: ")
#edad = int(input("Introduce tu edad: "))

#mostrarTuNombre2(nombre, edad)

#Ejemplo 3

print("##### EJEMPLO 3 #####")

#Crear una funcion que cree una tabla de multiplicar 

def tabla (numero):
    print(f"Tabla de multiplicar del número {numero}")
    for contador in range(11):
        print(f"{numero} x {contador} = {numero * contador}")
    print("\n")

#tabla(3)
#tabla(7)
#tabla(12)

#Ejemplo 3.1

print("\n##### EJEMPLO 3.1 #####")

#Crear todas las tablas de multiplicar

for numero_tabla in range(1, 11):
    tabla(numero_tabla)


#Ejemplo 4

print("\n##### EJEMPLO 4 #####")

#Parametros Opcionales

def getEmpleado(nombre, ID=False): #False o None significa que son parametros opcional
    print("Empleado:")
    print(f"Nombre: {nombre}")
    if ID != False:
        print(f"ID: {ID}")


getEmpleado("Marcos Astudillo", "16416582-5")

#Ejemplo 5

print("\n##### EJEMPLO 5 #####")

#Parametros Opcionales y Return
#Return devuelve un dato de una funsion
    #Ejemplo return

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

print(saludame("Marcos Astudillo"))

#Ejemplo 6

print("\n##### EJEMPLO 6 #####")

#Generar una calculadora 

def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)
    return cadena

print(calculadora(5, 5))
print(calculadora(10, 10, True))


#Ejemplo 7

print("\n##### EJEMPLO 7 #####")

#Generar una calculadora 

def getNombre(nombre):
    texto = f"El nombre es {nombre}"
    return texto

def getApellido(apellido):
    texto = f"El apellido es {apellido}"
    return texto

def devuelveTodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(devuelveTodo("Marcos", "Astudillo"))

#Ejemplo 8

print("\n##### EJEMPLO 8 #####")

#Funciones lambda: son funciones anonimas que son simples o repetitivas y que se traducen en una linea o codigo (tareas pequeñas)

dime_el_year = lambda year:f"El año es {year}"

print(dime_el_year(2021))