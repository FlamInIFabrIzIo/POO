class persona():
    def __init__(self, nombre, edad ):
        self._nombre = nombre
        self._edad = edad
#De esta maner accedo al nombre, con un getter o get_atributo 
#para poder acceder a un valor que en teoria deberia ser privado _    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

##Creamos un objeto de la calse persona que se llama Fabri        
Fabri = persona("fabri", 22)

#para poder acceder a un valor que en teoria deberia ser privado _ 
##y obtuvimos su nomber con el getter
nombre = Fabri.get_nombre()
##y despues lo mostamose en pantalla
print(nombre)

##Despues cambiamos el nombre y se muestro Fabrizio 
Fabri.set_nombre("Fabrizio")
#aca obtuvimos su propiedad, obtuvimos nombre
nombre = Fabri.get_nombre()
#y se vuelve a mostrar en pantalla, en este caso:"Fabrizio"
print(nombre)

 

