"""
#FOR

for variable in elemento_iterable (lista, rango, etc)
    bloque de instrucciones

"""
contador = 0 

for contador in range(0,10):
    print("Voy por el " + str(contador))


contador = 0 
resultado = 0
resultado2 = 0
for contador in range(0,10):
    print("Voy por el " + str(contador))

    resultado = resultado + contador
    resultado2 += contador

print(f"El resultado es: {resultado}")
print(f"El resultado es: {resultado2}")


#Ejemplo con tablas de multiplicar

print("\n##########  EJEMPLO ##########")

numero_usuario=int(input("De que número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"\n########## TABLA DE MULTIPLICAR DEL NUMERO {numero_usuario} ##########\n")

for numero_tabla in range(1, 11):
    if numero_usuario == 45:
        print("No se pueden mostrar números prohibidos")
        break #sirve para cortar los bucles
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("\nTabla Finalizada")