#Operadores de asignacion
"""
Los operadores de asignacion permiten dar un valor a una variable
"""
edad = 55

print(edad)

edad += 5
edad = edad + 5 #estas dos funciones son lo mismo, solo que la primera se ahorra anotar la edad anterior
print(edad)
edad -= 5
print(edad)



#operadores de incremento y decremento

year = 2021

#incremento
year = year + 1

print(year)
year += 1
print(year)
#decremento
year = year - 1
print(year)

year -= 1
print(year)
"""
este tipo de operador no existe en python
year ++
year--
--year
++year
"""

#Pre incremento
year = 1 + year

print(year)
#Pre decremento
year = 1 - year

print(year)