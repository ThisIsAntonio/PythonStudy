import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
    def __init__(self, usuario_id, titulo = "", descripcion = ""): #en caso de que no llegue nada y los campos sean vacios se pone eso
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO notas VALUES(null,%s,%s,%s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        try:
            cursor.execute(sql, nota)
            database.commit()
            result = [cursor.rowcount,self]
        except:
            result = [0, self]

        return result

    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'" #uso del like y los porcentajes es cuando algo se encuentra contenido en otro

        try:
            cursor.execute(sql)
            database.commit()
            result = [cursor.rowcount,self]
        except:
            result = [0, self]

        return result
        