"""
    Ejercicio 6. Hacer un programa que realice todas las tablas de multiplicar 
    mostrando el titulo de la tabla y luego las multiplicaciones
    del 1 al 10
"""

for cabecera in range (1, 11):
    print (f"\n##### TABLA DEL {cabecera} #####\n")

    for numero in range (1, 11):
        print (f"{numero} x {cabecera} = {numero * cabecera}")
    
    print("--------------------------\n")



