import OpenIA

OpenIA.api_key = "sk-k79Y..."

system_init = "" #Texto para decirle como queremos que se comporte, asignarle un rol digamos

mensaje = [{"role":"system", "content":"system_rol"}]

#Creamos la clase sentimeinto que tiene la responsbildiad unica de representar el nobre y
#su color
class sentimiento:
    def __init__(self,nombre, color):
        self.nombre = nombre
        self.color = color
        
    def __str__(self):
        #esto se hace pq el primer {} remplaza a color y el segundo {} a nombre
        #o sea positivo, muy positivo,etc
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.nombre)


#esta clase teiene la responsabilidad de mapear polaridades a sentieinto
#cumplio el principio abierto/cerrado pq esta abierto a futuras extensiones sin cmabiar
#este codigo y el principio de inversion de dependecia, depende de dos implementaciones,
#de sentimeintos y de rango, no dependemos de una biblioteca externa 
class AnalizadorDeSentimientos:
    def __init__(self,rangos):
        self.rangos = rangos
    
    def Analizar_sentimiento(self, polaridad):
        #basicamente esto es una forma de desempaquetar
        #pq rangos es una tupla y adentro tiene tuplas tambien
        for rango, sentimiento in self.rangos:
            #primer tupla contiene los rangos
            if rango[0] < polaridad <= rango[1]:
                #sengunda tupla el sentimeinto
                return sentimiento
            #si no ocurre nada de lo anterior se ejcuta lo siguiente
            return Sentimiento("muy negativo", "31")

rangos = [
    ((-0.6, -0.3), sentimiento("muy negativo","31")),
    ((-0.3, -0.1), sentimiento("algo negativo","31")),
    ((-0.1, 0.1), sentimiento("neutral","33")),
    ((0.1, 0.4), sentimiento("algo positivo","32")),
    ((0.4, 0.9), sentimiento("positivo","32")),
    ((0.9, 1), sentimiento("muy positivo","32")),
]

Analizador = AnalizadorDeSentimientos(rangos)

while True:
    user_prompt = input("\x1b[1;33m" + "\nDecime algo"+ "\x1b[0;37m")
    #aca cada vez que escriba un mensaje el usuario, va a tener un rol diferente
    mensaje.append({"role":"user", "content" : user_prompt}) 
    #por que esto? porque chatgpt lo que hace es, lee el un chat, los entiende y lo
    ###################autocompleta
    completion = OpenIA.ChatCompletion.create(
        model = " GPT-4o",
        messages = mensaje,
        max_tokens = 8 #bits
        
    )
    
    respuesta = completion.choices[0].message["content"]
    mensaje.append({"role" : "assistant", "content" : respuesta})
    
    Sentimiento = Analizador.Analizar_sentimiento(float(respuesta))