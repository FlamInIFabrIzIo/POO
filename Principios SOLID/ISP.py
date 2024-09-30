# from abc import ABC, abstractmethod

# class Trabajdor(ABC):
    
#     @abstractmethod
#     def comer (self):
#         pass
    
#     @abstractmethod
#     def trabajar(self):
#         pass
    
#     @abstractmethod
#     def dormir (self):
#         pass
    
# class Humano(Trabajdor):
#     def comer(self):
#         print("el humano esta trabajando")

#     def trabajar(self):
#         print("el humano esta trabajando")
        
#     def dormir(self):
#         print("el humano esta durmiendo")


# #en este caso esta mal, por que estmos dependiedno de una interfaz y con interfaz
# #se hace referencia a las calses abtractas, esta mal pq me veo obligdo a utilizar
# #metodos que no me sirven, por que robot no come, ni duerme   
# class Robot(Trabajdor):
#     def comer(self):
#         pass

#     def trabajar(self):
#         print("el robot esta trabajando")
        
#     def dormir(self):
#         pass
        

    
# robot = Robot()

#solucion, dividir una interfaz en varias interfaces mas pequeñas

from abc import ABC, abstractmethod

class Trabajdor(ABC):

    @abstractmethod
    def trabajar (self):
        pass

class comedor(ABC):
    
    @abstractmethod
    def comer (self):
        pass

class durmiente(ABC):
    
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajdor, durmiente, comedor):
    def comer(self):
        print("el humano esta comiendo")

    def trabajar(self):
        print("el humano esta trabajando")
        
    def dormir(self):
        print("el humano esta durmiendo")

class Robot(Trabajdor):

    def trabajar(self):
        print("el robot esta trabajando")

robot = Robot()
humanou = Humano()

robot.trabajar()
humanou.trabajar()
humanou.comer()
humanou.dormir()

