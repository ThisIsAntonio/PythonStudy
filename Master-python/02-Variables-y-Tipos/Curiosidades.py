miTexto = "'Master'" #Dependiendo de como  se inicia si es con comillas dobles o simple la otra funciona para dejarla como string
miTexto2 = "En \"Python\"" #Con \" sirve para agregar una comilla entre el textoy solo funciona en comillas dobles no en comillas simple

"""
\n sirve para salto de linea
\t sirve para tabulacion
\r borra las variables previas a este comando
"""
textoUnido = miTexto + " \n " + miTexto2

print(textoUnido)