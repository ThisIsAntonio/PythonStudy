"""
    Ejercicio 3. Programa que compruebe si una variable esta vacia y si esta vacia, rellenarla con texto en minusculas y mostrarlos en mayusculas
"""

texto = ""

if len(texto.strip()) <= 0:
    #Mostraar el texto
    texto = "hola soy un texto en minusculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido {texto}")