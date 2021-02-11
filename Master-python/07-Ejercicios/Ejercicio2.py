"""
    Ejercicio 2. Escribir un Script que nos muestre por pantalla, 
    todos los numeros pares del 1 al 120.
"""

print("########## EJERCICIO 2 ##########\n")

contador = 1

for contador in range(1, 121):
    if contador%2 == 0:
        print(contador)
    else:
        print(f"{contador} No es par")