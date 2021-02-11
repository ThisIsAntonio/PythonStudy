"""
Set. Tipo de datos para tener una coleccion de valores, pero no tiene indice ni orden.
"""

persona = {
    "Victor", "Manolo", "Francisco"
}

print(persona)
print(type(persona))

persona.add("Marcos")
print(persona)
persona.remove("Victor")
print(persona)