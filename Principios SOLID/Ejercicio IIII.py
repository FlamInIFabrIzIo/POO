#Biblioteca que utiliza procesamiento de lenguaje natural (NLP), e IA
#entiende ingles y no es tan precisa
from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self,Texto ):
        analisis = TextBlob(Texto)
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else:
            return "negativo"
        
analizador = AnalizadorDeSentimientos()
resultado_1 = analizador.analizar_sentimiento("i'm be happy")
resultado_2 = analizador.analizar_sentimiento("sad")
print(resultado_1)
print(resultado_2)
