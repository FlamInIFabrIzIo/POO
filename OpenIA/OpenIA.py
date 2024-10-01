import OpenIA

OpenIA.api_key = "sk-k79Y..."

system_init = "" #Texto para decirle como queremos que se comporte, asignarle un rol digamos

mensaje = [{"role":"system", "content":"system_rol"}]

#Maaal code, violamos varios principios de SOLID
class AnalizadorDeSentimientos:
    def Analizar_sentimiento(self, polaridad):
        if polaridad > -0.8 and polaridad <= -0.3:
            #Con esto le damos color  la consola
            return "\x1b[1;31m" + "Negativo" + "\x1b[0;37m"
        
        elif polaridad > -0.3 and polaridad < -0.1:
            return "\x1b[1;31m" + "Algo Negativo" + "\x1b[0;37m"
        
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"

        elif polaridad >= 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo" + "\x1b[0;37m"
        
        elif polaridad >= 0.9:
            return "\x1b[1;32m" + "Muy Positivo" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "Muy Negativo"  + "\x1b[0;37m"      


Analizador = AnalizadorDeSentimientos()

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