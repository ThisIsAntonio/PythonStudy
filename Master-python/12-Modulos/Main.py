"""
    Los modilos son funcionalidades ya realizadas para reutilizar.
    En python existen muchos modulos:
    https://docs.python.org/3/py-modindex.html
    Podemos conseguir modulos que existen en lenguaje,
    tambien conseguir modulos en internet y por ultimo crear nuestros propios modulos.
"""

#importar modulo propio
import miModulo
#from miModulo import HolaMundo #Este codigo sirve para llamar solo una funcion, si se quiere importar todas solo usar import miModulo o el codigo siguiente
from miModulo import *

#print(miModulo.HolaMundo("Marcos Astudillo"))

#print(miModulo.calculadora( 12, 12, True))

print(HolaMundo("Marcos Astudillo"))
print(calculadora( 12, 12, True))


#Modulo fechas
import datetime

print(datetime.date.today())

fechaCompleta = datetime.datetime.now()

print(fechaCompleta)
print(fechaCompleta.year)
print(fechaCompleta.day)

fechaPersonalizada = fechaCompleta.strftime("mi fecha personalizada %d/%m/%Y, %H:%M:%S")
print(fechaPersonalizada)

print(datetime.datetime.now().timestamp())

#Modulo Matematica
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Sacar numero PI: ", math.pi)
print("Redondear: ", math.ceil(math.pi)) #Redondea a la alta
print("Redondear: ", math.floor(math.pi)) #Redondea a la baja

#Modulo Random
import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15,67))