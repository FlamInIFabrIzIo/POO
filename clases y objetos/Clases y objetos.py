#Se crea una calse que tiene la receta/definicion de que van a contener o como
#van a ser los objetos que creemos

#class celular():
#    marca =  "Samsung"
#    modelo = "S23"
#    camara = "48MP"
    
#Objetos ###instancia de la clase celular

#celular1 = celular()
#celular2 = celular()
#celular3 = celular()
#celular4 = celular()

#print(celular2.camara)


#Creamos la calse(OBJETO)
class celular:
    #Metodo constructor
    #Esta funcion se ejecuta automaticamente cada vez que creamos un objeto
    #Metodo -> (funcion) especial (_init_)
    def __init__(self, marca, modelo, camara):
        #########self, es una forma de hacer referencia asi misma
        self.marca = marca 
        self.modelo = modelo
        self.camara = camara
    
    #Metodos(acciones)
    #el objeto self siempre tiene que estar
    def llamar(self):
        print(f"estas haciendo una llamado desde: {self.modelo}")
    
    def cortar(self):
        print(f"cortaste la llamda desde tu {self.modelo}")

celular1 = celular("Samsung", "S23", "48MP")
celular2 = celular("Apple", "Iphone 14 pro", "96MP") 

celular2.llamar() 