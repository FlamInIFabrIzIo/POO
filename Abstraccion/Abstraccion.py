class auto():
    def __init__(self):
        self._estado = "apagado"
                
    def encender(self):
        self._encender = "encendido"
        print("el auto esta encendido")
        
    def conducir(self):
        #si el auto esta apagado
        if self._estado == "apagado":
            #lo encendemos
            self.encender()
        #y si ya esta encendido:
        print("conduciendo el auto")
        
mi_auto = auto()
#aca se genera la abstraccion, pq le estoy oculatando toda la logica interna
#y solo le doy un metodo para que sepa lo que esta conduciendo al usuario
mi_auto.conducir()