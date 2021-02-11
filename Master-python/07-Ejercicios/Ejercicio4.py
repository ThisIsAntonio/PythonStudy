"""
    Ejercicio 4. Pedir dos numeros al usuario y hacer todas las operaciones basicas de una calculadora y mostrarla por pantalla
"""

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("\n##### CALCULADORA #####\n")

print (f"Suma: " + str(suma) + "\n")
print (f"resta: " + str(resta) + "\n")
print (f"multiplicacion: " + str(multiplicacion) + "\n")
print (f"division: " + str(division))
