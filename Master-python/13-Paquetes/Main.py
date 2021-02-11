"""
    __init__py siempre se crea este archivo en una carpeta
    dentro de la carpeta se crean los paquetes con funciones que sirven para llamarse aqui, despues se llaman con el from
    y se van llamando las funciones
    usar https://pypi.org para descargar paquetes
"""

print("#### probando paquetes: ####")
from miPaquete import Pruebas
from miPaquete import Herramientas

Pruebas.probando()
Herramientas.nombreCompleto("Marcos", "Astudillo")