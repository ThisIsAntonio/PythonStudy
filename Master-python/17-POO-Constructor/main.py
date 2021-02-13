from coche import Coche
carro = Coche("Amarillo","Renault", "Clio", 150, 200, 4)
carro1 = Coche("Gris","Audi", "A5", 300, 190, 4)
carro2 = Coche("Blanco","Audi", "A3", 250, 100, 4)
carro3 = Coche("Negro","Nissan", "Qashqai", 250, 100, 5)

"""
print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
"""

# Detectar tipado siempre se compara con la clase del objeto
"""
if type(carro3) == Coche:
    print("Si es un objeto correcto")
else:
    print("No es un objeto!!!")
"""

#Visibilidad
print(carro.soy_publico)
#print(carro.__soy_privado)
print(carro.getPrivado())