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
        print(f"Mi habilidad es {self.habilidad}")
        
class EmpleadoArtista(persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
        
