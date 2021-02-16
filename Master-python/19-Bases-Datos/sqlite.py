"""
    Para usar DBA se debe usar sqlitle que trae instalado
"""
#Importar modulo
import sqlite3
from sqlite3.dbapi2 import connect

#Conexion
conexion = sqlite3.connect('pruebas.db')

#Crear cursor
cursor = conexion.cursor()

#Crear Tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT,
    PRECIO INT(255)
)
""")

#Guardar cambios

conexion.commit()

#Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (" + 
"null, " + 
"'primer producto', " +
"'descripcion de mi producto'," +
"550" +
")")
conexion.commit() #SE guarda la consulta
"""

#Borrar registros
#cursor.execute("DELETE FROM productos")
#conexion.commit()

#Insertar muchos registros de golpe
productos = [
    ("ordenador portatil", "buen pc", 700),
    ("Telefono movil", "buen telefono", 140),
    ("placa base", "buena placa", 80),
    ("Tablet 15", "buena tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

#Update
cursor.execute("UPDATE productos SET precio=678 WHERE precio = 80")

#Listar dados de la tabla
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
productos = cursor.fetchall()   #Sirve para ver los datos de la consulta
#print(cursor)
#print(productos)

for producto in productos:
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
    print("---------------------")

#Sacar el primer registro de la tabla
cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

#Cerrar conexion
conexion.close()