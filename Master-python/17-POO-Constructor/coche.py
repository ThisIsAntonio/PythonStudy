# Programación orientada a objetos (POO o OOP)

#Definir una clase (molde para crear más objetos de ese tipo
# (coche) con caracteristicas similares)
class Coche:
    #Atributos o variables
    #Caracteristicas del coche
    color = "Red"
    marca = "Audi"
    model = "A5"
    velocidad = 300
    hp = 190
    plaza = 4

    soy_publico = "Hola, soy un atributo publico"

    __soy_privado = "Hola, soy un atributo privado"

    def __init__(self, color, marca, model, velocidad, hp, plaza):
        self.color = color
        self.marca = marca
        self.model = model
        self.velocidad = velocidad
        self.hp = hp
        self.plaza = plaza
    
    #Métodos, son acciones que hacen que el objeto (Car) (funciones)
    def getPrivado(self):
        return self.__soy_privado

    def acelerate(self):
        self.velocidad += 1
    
    def stop(self):
        self.velocidad -= 1
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setModelo(self, model):
        self.model = model
    
    def getModelo(self):
        return self.model

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):
        info = "--- informacion del vehiculo ---"
        info += "\n Marca: " + self.getMarca()
        info += "\n Color: " + self.getColor()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())
        return info



#Fin definicion clase