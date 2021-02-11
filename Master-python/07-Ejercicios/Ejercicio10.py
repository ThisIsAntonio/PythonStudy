"""
    Ejercicio 10. Crear un programa que pida al usuario la nota de 15 alumnos y el programa
    indicara cuantos alumnos aprobaron y cuantos suspendido
"""

contador = 1
aprobados = 0
suspendidos = 0
numAlumnos = int(input("Ingrese la cantidad de alumnos que tiene: "))

while contador <= numAlumnos:
    nota = int(input(f"Que nota tiene el \"alumno {contador}\": "))

    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    
    contador += 1
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {suspendidos}")
