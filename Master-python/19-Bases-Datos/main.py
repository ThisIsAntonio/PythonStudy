import mysql.connector

#Coneccion a DBA
master = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

#La coneccion ha sido correcta?
#print(database)

#Cursor para ejecutar consultas
cursor = master.cursor(buffered=True) #Ojo con el buffered, cuando no me arranca la dba es recomendable poner esto, igual buscar mas info

#Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

"""
for bd in cursor:
    print("-- bases de datos --")
    print(bd)
"""
#Borrar tablas
#cursor.execute("DROP TABLE IF EXISTS vehiculos")

#Crear Tablas
#cursor.execute("""
"""
CREATE TABLE vehiculos(
    id INT(10) AUTO_INCREMENT NOT NULL,
    marca VARCHAR(40) NOT NULL,
    modelo VARCHAR(40) NOT NULL,
    precio FLOAT(10,2) NOT NULL,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
"""#)


cursor.execute("SHOW TABLES")

for tables in cursor:
    print("--tablas--")
    print(tables)



#Insertar datos en tablas
#cursor.execute("INSERT INTO vehiculos VALUES(null,'audi','A5', 32500)")
coches = [
    ('Seat', 'Ibiza', 2500),
    ('Renault', 'Clio', 1500),
    ('Hyundai', 'accent', 3250),
    ('Nizzan', 'qashqai', 1850),
    ('Audi', 'A3', 4500),
]
#cursor.executemany("INSERT INTO vehiculos VALUES (null,%s,%s,%s)", coches)

master.commit() #Guardar cambios


#Listar datos de la tabla

#Forma 1
print("-- vehiculos --")
for autos in coches:
    
    print(autos)

print("\n")

#Forma 2
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Audi'")
result = cursor.fetchall()
print(cursor)
print(result)


print("\n todos mis coches")
for coche in result:
    print(coche[1], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone() #Sacar el primer coche
print(coche)

#Borrar datos de una tabla
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Nizzan' ")
master.commit()

print(cursor.rowcount, "Borrados!!!") #contador de vehiculos borrados

#Actualizar datos

cursor.execute("UPDATE vehiculos SET modelo = 'i0' WHERE marca = 'Hyundai' ")
master.commit()

print(cursor.rowcount, "Actualizados!!!") #contador de vehiculos actualizados