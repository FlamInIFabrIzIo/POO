# Crear una clase ESTUDIANNTE que tenga los atributos nombre, edad y grado.
#Ademas hay que agregar un METODO que se llame ESTUDIAR que imprima el mensjae
#EL ESTUDIANTE "el estudiante (nombre) esta estudiando".
#Para trabajr con instancias, crear una instancia de esta clase y usar le metodo pero
#para esto abria que generar una interaccion con el usuario, o sea debe ser un requerimiento.
#se tiene que pedir el nombre, edad y grado; y a continuacion se tiene que instanciar esta clase
#y mostrar los datos de la clase creada.
#si despues de registra al estudiante el usuario escribe "estudiar" pone al estudiante a 
#estudiar indistinto de min o may.

#class estudiante():
#    def __init__(self, nombre, edad, grado):
#        self.nombre = nombre
#        self.edad = edad
#        self.grado = grado
        
#pedro = estudiante("Pedro", "23", "3°")

#print(pedro.grado)


class estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print("estudiando...")
        
nombre = input("ingrese su nombre: ")
edad = input("ingrese su edad: ")
grado = input("ingrese su grado: ")

estudiante = estudiante(nombre, edad, grado)

print(f"""
DATOS DEL ESTUDIANTE: \n \n
nombre : {estudiante.nombre} \n
edad : {estudiante.edad} \n
grado : {estudiante.grado} \n  
""")

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
    
