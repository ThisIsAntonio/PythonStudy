"""
    Ejercicio 5. hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario
"""


numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero1 < numero2:
    for contador in range (numero1, numero2+1):
        print (contador)

else:
    print ("El numero 1 debe ser menor al número 2")


