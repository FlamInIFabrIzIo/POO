#polimorfismo de herencia o polimorfismo de subtipos o de sub clase
#Dada la propiedad DUCK TYPING en python podemos hacer este tipo de herencia,
#en otros lenguajes no es asi. 
#no importa de que calse sea ni de donde provenga, si teiene un metodo llamado sonido
#entonces es eso.

#si aca yo le pongo sonido , puede hacerlo un animal
class Animal():
    def sonido(self):
        pass
    

class Vaca(Animal):
    def sonido(self):
        return "mu"


class perro(Animal):
    def sonido(self):
        return "guau"
    
    
class loro(Animal):
    def sonido(self):
        return "cantar"
    
def hacer_sonido(animal):
    print(animal.sonido())
    
    
vaca = Vaca()
perro = perro()
loro = loro()

hacer_sonido(perro)
#entonces si tiene la posibilidad de hacer un sonido es un animal.
#esto siginifica que no tengo que relacioanr las clases de ninguna manera, en otro lenguaje
#commo en JAVA por ejemplo esto tira error, si no lo hago con la clase animal.
print(loro.sonido())    
    