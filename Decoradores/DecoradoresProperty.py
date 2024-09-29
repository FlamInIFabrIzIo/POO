#Todo esto tiene mucha mas ventaja en cuanto a lo otro
# - sintaxis mucho mas limpia y concisa
# - nos perimite ecapsutlar la logica adicional
#-la logica es mucho mas manejable, cuando podemos acceder, modificarlos y eliminarlos
#como si fueran atributos normales
# - mayor flexibilidad de la evolucion del codigo, nos permite hacer codigo escalable
class persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
####Creamos un decorador, como "nombre" como si fuera un atributo
####para poder acceder a su valor
    @property   
    def nombre(self):
        return self.__nombre
#De esta forma tambiien lo mismo pero sera para poder modificarla
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
#Otro decorador pero para eliminar
    @nombre.deleter
    def nombre(self):
        #aca en ves de "retrun" va "del", para eliminar
        del self.__nombre


fabrizio = persona("fabri", 22)

#aca creemos que estamos accediento a un atributo, con la notacion dle punto
#pero estamos accediendo a un getter
#y que si lo modificamos, estamos modificando el atributo, pero estmos
#modificando la  propiedad por que estamos utilizando un setter
nombre = fabrizio.nombre
        
print(nombre)

fabrizio.nombre = "fla"

nombre = fabrizio.nombre
print(nombre)

#con esto ahcemos que la propiedad deje de existir
#del fabrizio.nombre

#nombre = fabrizio.nombre
#print(nombre) 