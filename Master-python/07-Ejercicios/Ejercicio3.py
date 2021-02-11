"""
    Ejercicio 3, escribir el cuadrado de los 60 primeros numeros naturales.
    con for y con while
"""

#while
contador = 0

while contador <= 60:
    cuadrado = contador * contador
    print(f"El cuadrado del {contador} es {cuadrado}")
    contador += 1


#for

contador = 0

for contador in range (61):
    cuadrado = contador * contador
    print(f"El cuadrado del {contador} es {cuadrado}")