class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola,estoy hablando un poco")

class empleado(persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class estudiante(persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

class jefe(persona):
    def __init__(self, nombre, edad, nacionalidad, ingresos, empresa):
        super().__init__(nombre, edad, nacionalidad)
        self.ingresos = ingresos
        self.empresa = empresa

roberto = empleado("roberto",45,"argentino","Programador",1000000)
pedrito = estudiante("pedrito",30,"colombiano","regular","UNL")
Esteban = jefe("Esteban","20","EEUU","1000000US","fintech")

print(f"Roberto trabaja en: {roberto.trabajo}")


print(f"Pedrito estudia en: {pedrito.universidad}")

print(f"Estebanquito es jefe en: {Esteban.empresa}")