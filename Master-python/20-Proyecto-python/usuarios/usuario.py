from mysql.connector import connect
import usuarios.conexion as conexion
import datetime
import hashlib #modulo para cifrar contraseñas

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    #Constructor
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    def registrar(self):
        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) #codifica en bytes y pasa a codificar a sha256
        fecha = datetime.datetime.now()
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount,self]
        except:
            result = [0, self]

        return result

    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email  = %s AND password = %s"

        #cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) #codifica en bytes y pasa a codificar a sha256
        #datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result