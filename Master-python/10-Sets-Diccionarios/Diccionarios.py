"""
    Diccionario. es un tipo de datos que almacena un conjunto de datos, en formato clave>valor
    es parecido a un array asociativo o un objeto json
"""

persona = {
    "nombre": "Marcos",
    "apellidos": "Astudillo",
    "web": "www.thisisantonio.com"
} #este se parece mucho a un json

print(persona)
print(type(persona))

print(persona["apellidos"]) #con los parentecis de cuadrado se pueden sacar los indices que uno quiera


#Lista con diccionarios

contactos = [
    {
        'nombre':'Marcos',
        'email':'antonio.ac86@hotmail.com'
    },
    {
        'nombre':'Paulina',
        'email': 'pauli.sp87@gmail.com'
    },
    {
        'nombre': 'lucia',
        'email': 'lucia.as2018@gmail.com'
    }
]

print(contactos)
print(contactos[0]['nombre'])

print('\n##### listado #####')
for contacto in contactos:
    print(f"Nombre: {contacto['nombre']}")
    print(f"Email: {contacto['email']}")
    print("------------")