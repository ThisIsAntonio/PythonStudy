
#Ojo las funciones siempre deben retornar algo no imprimir, y dar parametros dentro cosa que cuando se llamen, se pasen las variables globales
def mi_funcion(nombre):
    return "Hola que tal" + nombre

def mi_funcion2(apellidos):
    return "Hola que tal 2 " + apellidos

#Ojo, las variables globales siempre deben estar al comienzo o antes de llamar a las funciones
nombre = "Marcos"
apellidos = "Astudillo"

print("Hola mundo")
print(f"Bienvenido {nombre}")

print(mi_funcion(nombre))
print(mi_funcion2(apellidos))