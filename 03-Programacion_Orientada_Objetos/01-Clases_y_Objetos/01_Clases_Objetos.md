# 1. Clases y Objetos

Las clases son plantillas que contienen métodos y atributos, estas sirven para crear los objetos. Por otro lado, los objetos son una instancia de la clase.

---

## Tabla de Contenido

- [Conceptos clave](#conceptos-clave)
- [¿Qué es self?](#qué-es-self)
- [Ejemplo Practico](#ejemplo-practico)

---

## Conceptos clave

- *Clase:* El molde o plantilla para crear objetos. **(por ejemplo, el plano de un auto).**
- *Objeto:* Una instancia concreta creada a partir de una clase **(un auto concreto de color rojo, estacionado en tu cochera).**
- *Atributos:* Las características o datos que tiene el objeto **(por ejemplo,. marca, color, velocidad).**
- *Métodos:* Las acciones o funciones que puede realizar el objeto **(por ejemplo, acelerar, frenar).**

***Sintaxis***

```python
class Nombre_Clase:
    #Constructor: Se ejecuta automáticamente al crear elobjeto
    def __init__(self, atributo1, ..., atributon):
        #Atributo de instancia
        self.atributo1 = atributo1
        ...
        self.atributon = atributon
    #Método: Una acción que realiza el objeto
    def nombre_metodo(self):
        #Usamos "self" para acceder a los atributos del propio objeto
        print(f"Haciendo algo con {self.atributo1}")
```

---

## ¿Qué es self?

*self* representa a la instancia específica que está ejecutando el código. Le indica a Python: "accede a las propiedades o métodos de este objeto en particular y no de otro".

---

## Ejemplo Practico

1. [Clase y Objetos](/03-Programacion_Orientada_Objetos/01-Clases_y_Objetos/02_Clases_y_Objetos.py)

---

[Inicio](#1-clases-y-objetos)

---

[Tabla de contenido principal](/Tabla_Contenido.md)

---
