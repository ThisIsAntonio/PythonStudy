import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "master_python",
        port = 3306
    )
    #print(database)
    cursor = database.cursor(buffered=True)#El buffered sirve para usar el mismo cursor en muchas consultas

    return [database, cursor]