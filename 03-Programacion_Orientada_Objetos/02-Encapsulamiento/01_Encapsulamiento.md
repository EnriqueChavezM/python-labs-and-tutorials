# 2. Encapsulamiento y Atributos Privados

El encapsulamiento consiste en ocultar o proteger los datos internos de una clase para evitar que se modifiquen o alteren de forma indebida desde fuera. Python utiliza convenciones de nombres con guiones bajos (*_ y __*)

---

## Tabla de Contenido

- [Atrivutos Privados](#atrivutos-privados)
- [¿Cómo funciona el "Name Mangling" (Deformación de Nombres)?](#cómo-funciona-el-name-mangling-deformación-de-nombres)
- [Ejemplo Practico](#ejemplo-practico)

---

## Atrivutos Privados

| Tipo | Sintaxis | Nivel de protección | Descripción |
| :---: | :---: | :---: | :--- |
| Público | `self.atributo` | Ninguno | Acceso total desde cualquier parte del código. |
| Protegido | `self._atributo` | Por convención | Indica a otros programadores: "este atributo es de uso interno, no lo modifiques directamente". |
| Privado | `self.__atributo` | Por Name Mangling | Python altera internamente el nombre para dificultar su acceso directo desde fuera. |

---

## ¿Cómo funciona el "Name Mangling" (Deformación de Nombres)?

Cuando usas dos guiones bajos *(__atributo)*, Python cambia automáticamente el nombre del atributo añadiendo *_NombreDeClase* al inicio.
Aunque no se recomienda hacerlo, técnicamente aún podrías acceder al atributo privado así:

***Sintaxis***

```python
#Acceso "secreto" por Name Mangling: _Clase__atributo
print(objeto._NombreClase__atributo)
```

---

## Ejemplo Practico

- [Ejemplo Encapsulamiento](/03-Programacion_Orientada_Objetos/02-Encapsulamiento/02_Encapsulamiento.py)

---

[Inicio](#2-encapsulamiento-y-atributos-privados)

---

[Tabla de contenido principal](/Tabla_Contenido.md)

---
