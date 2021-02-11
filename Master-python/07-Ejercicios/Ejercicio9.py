"""
    Ejercicio 9. Crear un programa que pida numeros indefinidamente hasta que pida 111
"""

contador = 1
while contador < 100:
    numero = int(input("Ingrese un numero: "))

    if numero == 111:
        break
    else:
        print(f"Has introducido el numero {numero}")
