from abc import ABC, abstractmethod
########### De aca ######## hasta 
class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass 
###### aca #### es crear una plantilla

#luego se basan en la plantilla de aca para abajo ->>
#ya se estaria aplicando la claseAbstracta, pq? pq todas las demas de abjo depoenden
#de la plantill de arriba 
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
        
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
            
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
            
    def hacer_actividad(self):
        print(f"Actualemente estoy trabajanodo en el rubro de: {self.actividad}")
        

Juan = Estudiante("Juan", 27, "No binari", "programacion")

fabrizio = Trabajador("Fabrizio", 22, "Masculino", "abogacia y programacion")


fabrizio.presentarse()
fabrizio.hacer_actividad()
Juan.presentarse()
Juan.hacer_actividad()
            
                

#Digamos que creo una clase Persona normal y luego creo otras clases que hereden de Persona.
#Antes que todo el quliombo de code anteriori, Esto estaria ok.
#Sin embargo, en algunas situaciones, el uso de clases abstractas nos proporciona 
#ciertas ventajas.
#Por ejemplo, las clases abstractas nos permiten hacer autodocumentación y establecer 
#lo que se conoce como un "contrato". Esto significa que cuando heredas de una clase 
#abstracta, los métodos definidos como abstractos deben ser implementados en las subclases.
#Si no se implementan, el código no se podrá ejecutar correctamente.
#Además, las clases abstractas ayudan a evitar errores. Si tenes una clase base 
#(superclase) y, por error, alguien intenta instanciarla directamente, 
#Python lanzará un error porque la clase está definida como abstracta, 
#lo que previene este tipo de situaciones.
#Tambienn otro puntito a favor con esto, es que fomenta el polimorfismo dada la
#breve esplicacion anterior.