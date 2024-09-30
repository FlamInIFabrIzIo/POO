#PRINCIPIO ABIERTO/CERRADO:

#tenemos la clase padre que no se puede modificar 
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError
#pero queda escalable para agregar mas funcionalidades, el resultado es un codigo + limpio
#y optimizamos riesgos
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensjae por MAIL a {self.usuario.email}")
        
        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando mensjae por SMS a {self.usuario.sms}")
        
        
class NotificadorWhatsApp(Notificador):
    def Notificar(self):
        print(f"Enviando WhatsApp a {self.usuario.whatsapp}")
        
        