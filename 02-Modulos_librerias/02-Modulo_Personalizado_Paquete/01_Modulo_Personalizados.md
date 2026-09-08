# 2. Módulos Personalizados

Un módulo personalizado en Python no es más que un archivo de *código .py* escrito por ti, que contiene funciones, variables o clases que deseas reutilizar en otros programas.
En lugar de copiar y pegar el mismo código en varios archivos, guardas esas funciones en un archivo aparte e importas ese archivo como un módulo.

---

## Tabla de Contenido

- [Crear y Utilizar Módulos Personalizados](#crear-y-utilizar-módulos-personalizados)
- [Paquetes](#paquetes)
  - [Crear y Utilizar Paquetes](#crear-y-utilizar-paquetes)
    - [Estructura de Carpetas Recomendada](#estructura-de-carpetas-recomendada)
    - [Archivo Especial __init__.py](#archivo-especial-__init__py)
- [Ejemplo Practico](#ejemplo-practico)

---

## Crear y Utilizar Módulos Personalizados

Para crear un módulo personalizado, simplemente creamos un nuevo archivo Python con el nombre deseado y definimos las funciones, clases y variables que queremos incluir en el módulo.
A medida que nuestros programas crecen en tamaño y complejidad, es una buena práctica organizar nuestro código en módulos separados según su funcionalidad. Esto nos permite conservar un código más legible, agrupado en módulos y fácil de mantener.

**Ejemplo:**

```python
#mi_modulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!!")
def calcular_suma(a, b):
    return a + b
```

creamos un archivo **(en el mismo directorio donde estamos ejecutando Python)** llamado ``mi_modulo.py.`` Luego, podemos importar y utilizar las funciones definidas en *mi_modulo.py* en otro archivo Python.

```python
import mi_modulo

mi_modulo.saludar("Juan") #Imprime "Hola, Juan!!"
print(mi_modulo.calcular_suma(5, 3)) #Imprime 8

```

---

## Paquetes

Un paquete es una forma de organizar módulos relacionados en una estructura jerárquica de directorios. Los paquetes nos permiten agrupar módulos relacionados y evitar conflictos de nombres entre módulos.

### Crear y Utilizar Paquetes

Para crear un paquete, creamos un directorio con el nombre deseado y agregamos un archivo especial llamado ``__init__.py`` dentro del directorio. Este archivo puede estar vacío o contener código de inicialización del paquete.

#### Estructura de Carpetas Recomendada

Imagina que quieres organizar tu proyecto en un paquete llamado *mi_paquete*

**Ejemplo:** 

```text
mi_proyecto/
│
├── main.py                 # Script Principal
└── mi_paquete/             # Carpeta del Paquete
│   ├── __init__.py         # Archivo Especial que Define el Paquete
│   ├── matematicas.py      # Módulo 1
│   └── textos.py           # Módulo 2
```

#### Archivo Especial ``__init__.py``

Para que Python reconozca una carpeta como un paquete, tradicionalmente debe contener un archivo llamado ``__init__.py.``

- Puede estar **completamente vacío.**
- Su presencia indica a Python que la carpeta debe tratarse como un módulo *ejecutable/importable.*
- También se puede usar para inicializar código del paquete o simplificar las importaciones.

---

## Ejemplo Practico

- [Modulo Personalisado y Paquete](/02-Modulos_librerias/02-Modulo_Personalizado_Paquete/02_Modulo_personalizado.py)

---

[Inicio](#2-módulos-personalizados)

---

[Tabla de contenido principal](/Tabla_Contenido.md)

---
