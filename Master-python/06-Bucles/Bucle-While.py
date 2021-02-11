"""
    #Bucle while
    Estructura de control que itera o repite la ejecución de una serie
    de instrucciones tantas veces como sea necesario, hasta que deje 
    de cumplirse la condición indicada.

    while condición:
        bloque de instrucciones
        actualización de contador
"""

contador = 1
while contador <= 100:
    print(f"Estoy en el número {contador}")

    contador += 1
print("\n----------------------------------------")

contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame = muestrame + ", " + str(contador)

    contador += 1

print(muestrame)

print("\n----------------------------------------\n")


#EJEMPLO
print("\n########## EJEMPLO ##########\n")
numero_usuario = int(input("De que Numerop quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"########## Tabla del {numero_usuario} ##########\n")

contador =1
while contador <=10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1
else:
    print("\nTabla terminada")