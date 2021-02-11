"""
    Ejercicio 4. Crear un script que tenga 4 variables, una lista, un string, un entero, y un booleano.
    Y que imprima un mensaje segun el tipo de datos de cada variable
"""

def traducirTipo(tipo):
    result = ""
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "Cadena de Texto"
    elif tipo == int:
        result = "Numero entero"
    elif tipo == bool:
        result = "booleano"
    return result

def comprobarTipado(variable, tipo):
    test = isinstance(variable, tipo)
    result = ""
    if test:
        print(f"Este dato es del tipo {traducirTipo(tipo)}")
    else:
        result = "El tipo de dato no es correcto"
    
    return result


lista = ["Hola mundo", 77]
titulo = "Master en python"
numero = 100
verdadero = True

print(comprobarTipado(lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))
