from logging import exception
import usuarios.usuario as modelo
import notas.acciones 

class Acciones:
    def registro(self):
        print("\nOk!!, vamos a registrarte en el sistema...\n")
        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cual es tu apellido?: ")
        email = input("Cual es tu email?: ")
        pasword = input("introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, pasword)
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nno te has registrado correctamente.")

    def login(self):
        print("\nVale!!, Identificate en el sistema...\n")
        try:
            email = input("Cual es tu email?: ")
            pasword = input("introduce tu contraseña: ")

            usuario = modelo.Usuario('','',email,pasword)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto!!, intentalo mas tarde")
    
    def proximasAcciones(self, usuario):
        print(f"\nHola {usuario[1]}")
        print("""
        Estas son las acciones disponibles:
            - Crear nota (crear)
            - Mostrar tus notas (mostrar)
            - Eliminar nota (eliminar)
            - Salir (salir)
        """)

        accion = input("Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            print("\nVamos a crear")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            print("\nVamos a mostrar")
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            print("\nVamos a eliminar")
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"\nOk {usuario[1]} hasta pronto")
            exit()


        return None