"""
    Ejercicio 5. Crear una lista con el contenido de esta tabla:
    accion  aventura            deportes
    gta     AC                  fifa 21
    cod     CTR                 pro 21
    pugb    Prince of Persia    moto gp 21

    Mostrar esta informacion ordenada
"""

tabla = [
    {
        'categoria': 'accion',
        'juegos': ['gta','cod','pugb']
    },
    {
        'categoria': 'aventura',
        'juegos': ['ac','ctr','prince of persia']
    },
    {
        'categoria': 'deportes',
        'juegos': ['fifa 21','pro 21','moto gp 21']
    }
]

print(tabla)

for categoria in tabla:
    print(f"####Categoria: {categoria['categoria']} ####")
    numero = 1
    for juegos in categoria['juegos']:
        print(f"Juego n°{numero}: {juegos}")
        numero += 1