"""
    Ejercicio 8. Crear un programa que permita sacar el % de otro número
"""

numero = int(input("Ingrese un número:"))
porcentaje = float(input(f"Ingrese el porcentaje que quiere calcular a {numero}: "))

if porcentaje > 1:
    total = numero * (porcentaje / 100)
else:
    total = numero * porcentaje

print(f"El resultado del {porcentaje} al {numero} es: {total}")