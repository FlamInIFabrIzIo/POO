#Ejercicio de herencia y uso super:

###Crear un sistema para una escuela, En este
#sistema vamos a tener dos clases principales;
#PERSONA y ESTUDIANTE. La clase PERSONA tendra los
#atributos de nombre y edad y un metodo que imprima
#el nombre y la edad de la persona. La clase ESTUDIANTE
#heredara de la calse PERSONA y tambien tendra un atributo
#adicional: GRADO y un metodo que imprima el grado
#del estudiante

#Deberas utilizar super en el metodo de inicialiazcion
#(init) para reutilizar el codigo de la clase padre
# (PERSONA). Luego crea una instancia de la clase ESTUDIANTE
#e imprime sus atributos y utiliza sus metodos para 
#asegurarte de que todo funciona correctamente.


class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        
class estudiante(persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_grado(self):
        print(f"Grado: {self.grado}")
        

estudiante = estudiante("fabrizio", "22", "4")
estudiante.mostrar_datos()
estudiante.mostrar_grado()