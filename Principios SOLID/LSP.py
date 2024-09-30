# class Ave:
#     def volar(self):
#         return "estoy volando"
# #Aca hay un problema pq pinguino deberia poder herdar todo lo que hace Ave
# #en este caso no se estaria cumpliendo el principio LSP
# class pinguino(Ave):
#     def volar(self):
#         return "no puedo volar"
    
#                 ###esto es una variable de parametro, pq se la pasmos entre adentro de los()
# def hacer_volar (ave = Ave):
#         return ave.volar()
    
# print(hacer_volar(pinguino()))

#En este caso si se cumpliria, en Ave deberiamos crear todas las cosas que 
#las aves tienen en comun
class Ave:
    pass
#despues creariamos subcalses para que puedan heredar de esta y tener sus propias
#funcionalidades pero que hereden de la calse base Ave, para asi cumplir con el 
#principio LSP y tener un codigo mas legible/escalable
class AveVoladora(Ave):
    def volar(self):
        return "estoy volando"
    
class AveNoVoladora(Ave):
    pass
    