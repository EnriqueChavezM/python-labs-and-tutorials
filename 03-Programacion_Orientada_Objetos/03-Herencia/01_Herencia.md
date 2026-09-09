# 3. Herencia

La herencia permite crear una clase nueva *(clase hija o subclase)* basada en una clase existente *(clase padre o superclase)*. La clase hija hereda automáticamente todos los atributos y métodos de la clase padre, permitiéndote reutilizar código y extender su funcionalidad.

---

## Tabla de Contenido

- [Funció *super()*](#funció-super)
- [Beneficios de *super()*](#beneficios-de-super)
- [Ejemplo Practico](#ejemplo-practico)

---

## Funció ``super()``

La función ``super()`` da acceso directo a los métodos de la clase padre desde la clase hija, siendo indispensable para invocar su constructor (``__init__``) sin repetir código.

***Sintaxis***

```python
#Clase Padre
class Padre:
    def --init--(self, atributo_padre):
        self.atributo_padre =  atributo_padre
#Clase Hija(recibe a la clase padre como argumento)
class Hija(Padre):
    def __init__(self, atributo_padre, atributo_hija):
        #super() llama al __init__ de la clase padre
        super().__init__(atributo_padre)
        self.atributo_hija = atributo_hija
```

---

## Beneficios de ``super()``

| **Sin *super()*** | **Con *super()*** |
| :--- | :--- |
| Si cambias el nombre de la clase padre, debes cambiarlo en todas las clases hijas. | Si la clase padre cambia de nombre, el código de las hijas no se rompe. |
| Difícil de mantener en herencia múltiple. | Maneja automáticamente el orden de resolución de métodos (MRO). |

---

## Ejemplo Practico

- [Ejemplo Herencia](/03-Programacion_Orientada_Objetos/03-Herencia/02_Herencia.py)

---

[Inicio](#3-herencia)

---

[Tabla de contenido principal](/Tabla_Contenido.md)

---
