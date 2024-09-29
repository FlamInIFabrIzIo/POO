class persona:
    ####metodo especial __init__: construye el objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    ###metodo especial __str__: nos devuelve una representacion del objeto
    #en una cadena de texto    
    def __str__(self):
        return f'persona(nombre={self.nombre}, edad={self.edad})'
    ###metodo especial __repr__: actua como "la representacion de"
    def __repr__(self):
        return f'persona("{self.nombre}",{self.edad})'    
    
Fabri = persona("fabrizio", 22)

repre = repr(Fabri)
resultado = eval(repre)

print(resultado)