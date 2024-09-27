class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hola, estoy hablando un poco")
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es {self.habilidad}"
#clase EmpleadoArtista hereda lo metodos y fucniones de persona y artista;
#ademas tiene sus propias funciones y metodos.        
class EmpleadoArtista(persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        #Aca heredamos de la clase persona directamente
        persona.__init__(self, nombre, edad, nacionalidad)
        #nuevamente se hereda lo de la otra clase, Artista.
        Artista.__init__(self,habilidad)
        #y aca se le agrega sus propias funciones
        self.salario = salario
        self.empresa = empresa
        
    #    def presentarse(self):
                        #Aca le estamos diciendo al programa que es un metodo que estamos
                        #trayendo de arriba, es un metodo que esta heredado
                        #normalmente cuando queremos llamar a un metodo de una clase padre
                        #se utiliza SUPER
#        return f"{super().mostrar_habilidad()}"

            
    def presentarse(self):
        print (f"Hola, soy:{self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}")
    
roberto = EmpleadoArtista("robert", 45, "argentino", "cantar", 1000, "apple")

roberto.presentarse()


#iamginemos que todo lo anterior es un modulo y no lo podemos ver
#por ej: EmpleadoArtista ¿hereda de de la clase Artista?

herencia = issubclass(EmpleadoArtista,Artista)

#Esto me permite ver si un objeto es una instatancia de una clase
instancia = isinstance(roberto, EmpleadoArtista)


print(instancia)