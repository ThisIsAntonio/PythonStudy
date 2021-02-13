# Programación orientada a objetos (POO o OOP)

#Definir una clase (molde para crear más objetos de ese tipo
# (coche) con caracteristicas similares)
class Car:
    #Atributos o variables
    #Caracteristicas del coche
    color = "Red"
    marca = "Audi"
    model = "A5"
    velocidad = 300
    hp = 190
    plaza = 4

    #Métodos, son acciones que hacen que el objeto (Car) (funciones)
    def acelerate(self):
        self.velocidad += 1
    
    def stop(self):
        self.velocidad -= 1
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def getVelocidad(self):
        return self.velocidad

#Fin definicion clase

#Crear objetos / Instanciar la clase

car = Car()
car.setColor("Grey")
car.setModelo("RS 8")
print("#### auto 1 ####")
print(car.marca, car.getModelo(), car.getColor())
print("Velocidad actual: " + str(car.getVelocidad()) + " KM")
"""
car.acelerate()
car.acelerate()
car.acelerate()
print(car.marca, car.getModelo(), car.getColor())
print("Velocidad nueva: " + str(car.getVelocidad()) + " KM")

car.stop()
print(car.marca, car.getModelo(), car.getColor())
print("Velocidad nueva: " + str(car.getVelocidad()) + " KM")
"""

#Crear mas objetos

car2 = Car()
car2.setModelo("A3")
car2.setColor("white")


print("\n#### auto 2 ####")
print(car2.marca, car2.getModelo(), car2.getColor(), car2.getVelocidad())