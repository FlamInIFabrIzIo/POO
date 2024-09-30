# #El diccionario va a tener toda la logica para verificar que funcione
# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #Logica pra verificar palabras
#         pass
# #
# class CorrectorOrtografico:
#     #el problema esta aca, pq esta muy ligado/conectado con diccioanrio 
#     def __init__(self):
#         self.diccionario = Diccionario()
#     #corregir Texto vamos  usra la logica del diccionario para verificarlo
#     def CorregirTexto(self,Texto):
#         #Usamos el diccionario para corregir el Texto
#         pass

#la forma correcta seria la siguiente
from abc import ABC, abstractmethod
    
class VerificadorOrtogrfico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        #Logica pra verificar palabra
        pass
    
class Diccionario(VerificadorOrtogrfico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabra si esta en el diccionario
        pass
    
class ServicioOnline(VerificadorOrtogrfico):
    def verificar_palabra(self, palabra):
        #Logica para verificar palabras desde el servicionweb
        pass
    
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        #usamos el verificador para corregir texto
        pass
corrector = CorrectorOrtografico(Diccionario())