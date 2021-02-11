"""
    Ejercicio 7, mostrar los numeros impares entre 2 numeros que decida el usuario
"""

        
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 < numero2:

    for contador in range (numero1, numero2 + 1):
        if contador%2 == 0:
            print(f"{contador} es par")
        else:
            print(f"{contador} es impar")
else:
    print("Número 1 debe ser mayor al 2")