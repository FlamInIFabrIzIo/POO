class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola,estoy hablando un poco")

class estudiante(persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

pedrito = estudiante("pedrito",30,"colombiano","regular","UNL")

print(f"Pedrito estudia en: {pedrito.universidad}")

