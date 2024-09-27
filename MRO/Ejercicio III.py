#HERENCIA MULTIPLE Y MRO:

#Imagina que estas modelando animales en un zoologico.
#Crear tres clases "Animal","Mamifero" debe tener un metodo llamado
#"amamantar" y la clase "Ave" un metodo llamado "Volar".

#Ahora, crea una clase "Murcielago" que herede de "Mamifero" y "Ave"
#en ese orden, y por lo tanto debe ser capaz de "Amamantar" y "Volar",
#ademas de "comer".

#Finalmente, juega con el orden de herencia de la calse "Muercielago" y 
#observa como cambia el  MRO y el comportamiento de los metodos al usar
#super()

class Animal():
    def comer (self):
        print("el animal esta comiendo") 
        
class Ave(Animal):
    def volar (self):
        print("el animal esta Volando")
        

class Mamifero(Animal):
    def amamantar (self):
        print("el animal esta amamantando")
        
class Murcielago(Mamifero, Ave):
    pass


Ave = Ave()


Ave.volar()
Ave.comer()

print(Murcielago.mro())