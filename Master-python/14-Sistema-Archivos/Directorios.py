import os
import shutil
#Crear carpeta

if not os.path.isdir("./miCarpeta"):
    os.mkdir("./miCarpeta")
else:
    print("El directorio ya existe")

#Eliminar carpetas
#os.rmdir("./miCarpeta")
#os.rmdir("./miCarpetaCopiada")
#Copiar carpeta
"""
ruta_original = "./miCarpeta"
ruta_nueva = "./miCarpetaCopiada"

shutil.copytree(ruta_original, ruta_nueva)
"""

#Eliminar carpetas
#os.rmdir("./miCarpetaCopiada")



#Mostrar los archivos de la carpeta
print("Contenido de mi carpeta")
contenido = os.listdir("./miCarpeta")
print(contenido)

num = 1
for fichero in contenido:
    print(f"Fichero n°{num}: {fichero}")
    num += 1