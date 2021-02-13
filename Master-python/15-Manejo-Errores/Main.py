#Capturar excepciones y manejar errores en código
#Susceptible a fallos/errores

"""
try:
    nombre = input("Cual es tu nombre?: ")
    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre
    print(nombre_usuario)
except: #Aparece este mensaje cuando arroja errores
    print("Ha ocurrido un error, mete bien el nombre")
else: #Si no paso por except, manda este mensaje
    print("Todo ha funcionado correctamente")
finally: #Detecta cuando haya terminado el try o el except
    print("Fin de la iteración")
"""

"""
print("\n#### ejemplo ####")
numeros = [13,64,52, 73, 21, 7, 91, 63]
#Busqueda de la lista
print("\n#### Busqueda de la lista ####")
busqueda = int(input("Introduce un número:"))

try:
    comprobar = isinstance(busqueda,int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce un número:"))
    else:
        print(f"Has introducido el {busqueda}")

    print(f"Buscar en la lista el número {busqueda} ")
    search = numeros.index(busqueda)
    print (f"El número buscado existe en la lista, y es el indice {search}")
except:
    print("El número no está en la lista, lo siento")
"""
"""
#Multiples excepciones
try:
    numero = int(input("Número para elevarlo al cuadrado: "))
    print(f"El cuadrado es {numero * numero}")
except TypeError:
    print("Debes convertir tus cadenas a enteros")
#except ValueError:
#    print("introduce un número correcto")
except Exception as e: #en este punto se guardan en una variable el tipo de error y los muestra
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__)
"""

#Excepciones personalizadas o lanzart excepciones

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("Edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido {nombre} al master de python")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Existe un error: ", type(e).__name__)