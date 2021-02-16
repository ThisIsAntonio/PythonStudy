"""
    Proyecto python y Mysql:
        -Abrir asistente
        -Login o Registro
        -Si elegimos registro, creará un usuario en la bbdd
        -si elegimos login, identifica al usuario y nos preguntará
        -crear nota, mostrar notas, y borrarlas.
"""
from usuarios import acciones #importo la clase acciones dentro del proyecto

print("""
Acciones disponibles:
    - registro
    - login
""")

hazEl = acciones.Acciones() #instancia la clase dentro del proyecto

accion = input("Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()