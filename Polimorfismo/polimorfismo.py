class gato():
    def sonido(self):
        return "miau"
    
class perro():
    def sonido(self):
        return "guau"
    
def hacer_sonido(animal):
    print(animal.sonido())
    
gato = gato()

perro = perro()

#en este caso tenemos polimorfismo de funcion, primero va la funcion(el mensaje) 
#y luego el parametro o classe o objeto como se quiera llamar , peden ser varios.
#en este caso se cambiaria gato por perro.
hacer_sonido(gato)
#aca cambia el argumento para la funcion.

######## Aca tengo polimorfismo por que el mensaje que estoy mandoando es el mismo
#seria sonido(el metodo o la accion de las dos manera esta bien)
#si yo cambiara perro por gato, seria un cambio de objeto pero el mensaje va a ser siempre
#el mismo, solo que con un resultado final diferente.
print(perro.sonido())
#aca cambia el objeto para el metodo.