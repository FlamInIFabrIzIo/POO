def decorador(funcion):
    #esto hace la funcion decoradora, literalmente lo que hace es, agregar una 
    #funcionalidad antes y despues
    #es basicamente como podemos agregar un codigo antes y/o despues o no hacer nada
    #solamente decoramos la funcion, se lo puede hacer pora una validacion
    def funcion_modificada():
        print("antes de llamar a la funcion")
        funcion()
        print("despues de llamar a la funcion")
    return funcion_modificada

# def saludo():
#     print("Hola Fla")

# #aca creamos una funcnion con una variable    
# saludo_modificado = decorador(saludo)
# saludo_modificado()


#Si bien tnato lo de arriba como lo de abajo son maneras correactas de hacerlo,
#la convencion adecuada es la que lleca el @ , ya que es una forma de hacer codigo
#mas estandar y legible, como asi tambien te ayuda a visulaizar mucho mejor que 
#decorador estas usando y a que funcion
@decorador
def saludo():
    print("Hola Fla, como va?")
    
saludo()