# Proyecto de Programación Orientada a Objetos (POO)

Este proyecto contiene una serie de ejemplos y ejercicios relacionados con los conceptos fundamentales de la Programación Orientada a Objetos (POO) en Python. El objetivo es proporcionar una comprensión clara y práctica de cómo aplicar estos conceptos en el desarrollo de software.

## Estructura del Proyecto

El proyecto está organizado en varias carpetas, cada una de las cuales aborda un tema específico de la POO. A continuación, se describe el contenido de cada carpeta y archivo:

---

### 🔹 Conceptos de POO

#### 📌 Clases y Objetos
- [Clases y objetos.py](clases%20y%20objetos/Clases%20y%20objetos.py): Ejemplo básico de creación de clases y objetos con la clase `Celular`.
- [Ejercicio I.py](clases%20y%20objetos/Ejercicio%20I.py): Ejercicio para crear una clase `Estudiante` con atributos y métodos, y una interacción con el usuario para instanciar la clase y utilizar sus métodos.

#### 📌 Atributos y Métodos
- Se abordan los diferentes tipos de atributos y métodos (de instancia, de clase y estáticos).

---

### 🔹 Herencia

#### 📌 Herencia Simple y Jerárquica
- [Herencia Simple.py](Herencia/Herencia%20Simple.py): Ejemplo de herencia simple con las clases `Persona` y `Estudiante`.
- [Herencia Jerárquica.py](Herencia/Herencia%20Jerarquica.py): Ejemplo de herencia jerárquica con las clases `Persona`, `Empleado`, `Estudiante` y `Jefe`.

#### 📌 Herencia Múltiple y MRO
- [Herencia Múltiple.py](Herencia/Herencia%20Multiple.py): Ejemplo de herencia múltiple con la clase `EmpleadoArtista`, que hereda de `Persona` y `Artista`.
- [MRO.py](MRO/MRO.py): Ejemplo de Method Resolution Order (MRO) con clases en una jerarquía de herencia.

#### 📌 Ejercicios II
- [Ejercicio II.py](Herencia/Ejercicio%20II.py): Ejercicio para reforzar el concepto de herencia mediante la creación de una jerarquía de clases.

---

### 🔹 Polimorfismo y Encapsulamiento

#### 📌 Polimorfismo
- [Polimorfismo.py](Polimorfismo/Polimorfismo.py): Ejemplo de polimorfismo con las clases `Gato` y `Perro`.
- [Polimorfismo de Herencia.py](Polimorfismo/Polimorfismo%20de%20Herencia.py): Ejemplo de polimorfismo aplicado a la herencia.

#### 📌 Encapsulamiento, Setters y Getters
- [Encapsulamiento.py](Encapsulamiento/Encapsulamiento.py): Ejemplo de encapsulamiento con atributos privados y métodos de acceso.
- [Setters y Getters.py](Setters%20y%20Getters/Setters%20y%20Getters.py): Implementación de métodos `setter` y `getter` para el acceso controlado a atributos.

#### 📌 Decoradores y @Property
- [Decoradores.py](Decoradores/Decoradores.py): Uso de decoradores en Python para modificar el comportamiento de funciones.
- [Decorador @Property.py](Decoradores/Decorador%20Property.py): Ejemplo de uso del decorador `@property` en una clase `Persona`.

---

### 🔹 Abstracción y Métodos Especiales

#### 📌 Abstracción y Clases Abstractas
- [Abstracción.py](Abstracción/Abstracción.py): Ejemplo de abstracción utilizando una clase `Auto`.
- [Clases Abstractas.py](Abstracción/Clases%20Abstractas.py): Uso de clases abstractas con `Persona`, `Estudiante` y `Trabajador`.

#### 📌 Métodos Especiales (Dunder Methods)
- [Métodos Especiales.py](Metodos%20Especiales/Metodos%20Especiales.py): Ejemplo de métodos `__init__`, `__str__`, `__repr__`, y sobrecarga de operadores.
- [Ejercicios III.py](Metodos%20Especiales/Ejercicios%20III.py): Ejercicio para implementar métodos especiales en un juego de fusión de personajes.

---

### 🔹 Principios SOLID

#### 📌 Introducción a SOLID
- Explicación de los cinco principios SOLID y su importancia en el diseño de software.

#### 📌 Principios SOLID en Práctica
- [SRP.py](Principios%20SOLID/SRP.py): Ejemplo del Principio de Responsabilidad Única (SRP).
- [OCP.py](Principios%20SOLID/OCP.py): Implementación del Principio Abierto/Cerrado (OCP).
- [LSP.py](Principios%20SOLID/LSP.py): Ejemplo del Principio de Sustitución de Liskov (LSP).
- [ISP.py](Principios%20SOLID/ISP.py): Principio de Segregación de Interfaces (ISP).
- [DIP.py](Principios%20SOLID/DIP.py): Principio de Inversión de Dependencias (DIP).

#### 📌 Ejercicio Final
- [Ejercicio Final.py](Principios%20SOLID/Ejercicio%20Final.py): Aplicación práctica de los principios SOLID en un proyecto realista.

---

## 🚀 Cómo Ejecutar el Proyecto

1. Clona el repositorio en tu máquina local:
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd POO
