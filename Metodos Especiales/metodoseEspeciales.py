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
    
    ###Con esto acabamos de definir como se va a comportar los objetos de la clase persona cuando los 
    #sumamos 
    def __add__ (self, otro):
        nuevo_valor = self.edad + otro.edad
        return persona(self.nombre + otro.nombre, nuevo_valor)
    
Fabri = persona("fabrizio", 22)
pedro = persona("pedro", 25)
pilar = persona("pilar", 26)

nueva_persona = Fabri + pedro + pilar
print(nueva_persona.edad)

#solo algunos de los METODOS ESPECIALES para tenerlos en cuenta:

#ARITMETICOS:
#El "other" hace referencia a lo que le quermos sumarle

#__add__(self, other): Sobrecarga del operador de suma(+)
#__sub__(self, other): sobrecarga del operador de resta(-)
#__mult__(self, other): sobrecarga del operador de multiplicacion
#__div__(self, other): sobrecarga del operador de division(/)
#__mod_(self, other): sobrecarga del operador de modulo(%)
#__pow__(self, other): sobrecarga del operador de exponenciacion(**)

#COMPARACION:
#__pow__(self, other): sobrecarga del operador de igualdad(==)
#__ne__(self, other): sobrecarga del operador de desiguldad(!=)
#__it__(self, other): sobrecarga del operador de menor que(<)
#__gt__(self, other): sobrecarga del operador de mayot que(>)
#__le__(self, other): sobrecarga del operador de menor o igual que(<=)
#__ge__(self, other): sobrecarga del operador de mmayor o igual que(>=)


#ASIGNACION:

#__ladd__(self, other): sobrecarga del operador de suma en asignacion(+=)
#__isub__(self, other): sobrecarga del operador de resta en asignacion(-=)
#__imul__(self, other): sobrecarga del operador de multiplicacion en asignacion(*=)
#__idiv__(self, other): sobrecarga del operador de division en asignacion(!=)
#__imod__(self, other): sobrecarga del operador de modulo en asignacion(%=)
#__ipow__(self, other): sobrecarga del operador de exponenciacion en asignacion(**=)

#OTROS:

#__len__(self): sobrecarga del operador len(). Devuelve longitud del objeto
#__getitem(self, index): sobrecarga del operador de indexacion([]). Permite acceder a elementos
#del obejto indice 
