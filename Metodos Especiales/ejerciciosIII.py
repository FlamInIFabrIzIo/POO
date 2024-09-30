#############CREAR UN JUEGO DE FUSION###########################

#el juego consiste en crear personajes de un juego y que esos personajes se puedan fusionar
#para formar personajes mas poderosos que tengan mas nievel/poder

#Para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes 
#se fusionen, salga un nuevo personaje con habilidades mejoradas

#Una posible formula es: el promedio de las habilidades de ambos, al cuadrado

class personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"{self.nombre} (fuerza: {self.fuerza}, velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad)/2)**1.34)
        return personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
#personajes        
goku = personaje("goku", 100, 200)
vegeta = personaje("vegeta", 80, 150)
jiren = personaje("jiren", 120, 120)

#fusiones
gogetin = goku + vegeta
jiretin = gogetin + jiren


print(goku)
print(vegeta)
print(jiren)
print(gogetin)
print(jiretin)


#Nuevos requisitos:
#- tiene que haber interaccion con el usuario
# - se tiene que poder agregar personajes
# - fusionar personajes
# - ver la lista de personajes disponible para fusioanr
# - y los creados