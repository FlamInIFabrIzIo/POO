class Miclase():
    def __init__(self):
        #con el guion bajo (_) al principio le estamos diciendo a python que es
        #un atributo privado
        self._nombre = "valor"
        
nombre = Miclase()
#se puede accaeder igual, yo como desarrolador entiendo que es un atributo privado
#pero se puede acceder igual
print(nombre._nombre)


class Clase():
    def __init__(self):
        #En este caso vemos como se hace un atributo "muy muy privado"
        #que se hace poniendole dos guiones bajos (__) antes del atributo.
        #esto si ya nos genera otro tipo de impacto en el codigo.
        #si vemos un codigo que tiene esto debemos acceder de otra forma, a trves de los 
        #Setters(definidor o establecedor): modificar o establecer el valor de un atributo
        #privado o muy muy privado 
        # y Getters(obtenedor): se usa para acceder a un atributo
        #muy privado o privado.
        self._trigger = "trigger"
    
    #con los metodos tmabien lo mismo, al ponerle dos  guiones medio(__) al principio
    #no va a dejar mostrrlos, pq se define como muy privado 
    def __hablar(self):
        print("Hola, como va")
        
objeto = Clase()
#al ejecutar esto me va a tirar un error, me va a decir que no lo encuetra por que es
#un atrubuto privado
#que realemtne si se pueda acceder a traves de n == m
print(objeto.__hablar())
