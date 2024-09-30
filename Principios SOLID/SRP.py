#Principio de responsabilidad unica (single resposibility principle) (S)
class TanqueDeCombustible:
    def __init__(self):
        #el tanque de combustible tiene una propiedad estatica
        #de 100, o sea que cada vez que creemos un auto con este tanque, va a tener 100
        self.combustible = 100
    #luego se crean 3 metodos con funcionalidades distintas
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
        
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad
#tenemos la clase auto que se encarga del movimiento del auto
#seria un objeto de la cl
class Auto():
    def __init__(self, tanque):
        #este es un atributo estatico
        self.posicion = 0
        #atributo de instancia, pq lo definimos en la instancia
        self.tanque = tanque
    #se crea un metodo para mover el auto
    def mover(self, distancia):
        #despues hacemos validaciones par justamente moverlo
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("has movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")
    
    def obtener_posicion(self):
        return self.posicion
#y aca creamos los objetos de tanque y auto(bmw)            
tanque = TanqueDeCombustible()
bmw = Auto(tanque) 


print(bmw.obtener_posicion())
print(bmw.mover(10))
print(bmw.obtener_posicion())
print(bmw.mover(20))
print(bmw.obtener_posicion())
print(bmw.mover(60))
print(bmw.obtener_posicion())
print(bmw.mover(100))
print(bmw.obtener_posicion())
print(bmw.mover(100))
print(bmw.obtener_posicion())