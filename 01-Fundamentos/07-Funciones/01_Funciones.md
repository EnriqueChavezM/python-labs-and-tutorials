# 7. Funciones

Las funciones son bloques de código reutilizables que nos permiten encapsular tareas específicas y ejecutarlas cuando sea necesario. Las funciones nos ayudan a organizar nuestro código, evitar la repetición y hacer que nuestros programas sean más modulares y fáciles de mantener.

---

## Tabla de Contenido

- [Funciones de Usuario](#funciones-de-usuario)
  - [Parámetros y Argumentos](#parámetros-y-argumentos)
  - [Funciones con número variable de argumentos](#funciones-con-número-variable-de-argumentos)
    - [`*args`](#args)
    - [`**kwargs`](#kwargs)
- [Funciones Integradas](#funciones-integradas)
- [Ejemplos Practicos](#ejemplos-practicos)
- [Funciones de Conversión y Estructuras](#funciones-de-conversión-y-estructuras)

---

## Funciones de Usuario

Para definir una función, utilizamos la palabra clave ``def`` seguida del nombre de la función y paréntesis. Opcional mente, podemos especificar parámetros dentro de los paréntesis. El bloque de código de la función se indenta después de los dos puntos.
Para llamar a una función, simplemente escribimos el nombre de la función seguido de paréntesis:

***Sintaxis***

```python
def Nombre_funcion():
    # Codigo de la funcion

#Llamar a la funcion
Nombre_funcion()
```

### Parámetros y Argumentos

Los parámetros son valores que enviamos cuando invocamos la función y nos permiten realizar operaciones dentro de la función. Los parámetros se especifican en la misma cabecera de la función
Al llamar la función es necesario mandar los argumentos que serán el valor que se le asignara a los parámetros.
Las funciones pueden devolver valores utilizando la palabra clave ``return``.

***Sintaxis***

```python
def Nombre_funcion(parametros):
    # Codigo de la funcion
    return valor de retorno # OPCIONAL!!, puede no tener valor de retorno

#Llamar a la funcion
Nombre_funcion(argumentos)
```

Puedes asignar valores predeterminados a los argumentos de una función. Si no se proporciona un argumento al llamar a la función, se utiliza el valor predeterminado.

**Ejemplo:**

```python
def saludar(nombre, saludo = "Hola"):
    print (nombre, saludo)
saludar("Kique") #Imprime: Kique Hola
```

> [!WARNING]
> Los argumentos predeterminados siempre deben seguir a los argumentos no predeterminados en la definición de la función.
> **Forma correcta:**
> `def saludar(nombre, saludo = "Hola"):...`
> **Forma incorrecta:**
> `def saludar(saludo = "Hola", nombre):...`

### Funciones con número variable de argumentos

Cuando pasamos un argumento a una función directamente y se asigna a un parámetro en función de su posición, se denomina argumento posiciónal. Así mismo, al declarar una función podemos definir una serie de parámetros con los que invocamos a dicha función, pero por regla general el número y el nombre de estos parámetros es inmutable, es decir que si defino que tendrá dos parámetros, entonces no podría agregar más.
Existen dos tipos de parámetros posiciónales:

- ``*args``: Se usa para pasar de forma opcional distintos valores
- ``**kwarg``: Se emplea para pasar distintos valores con la diferencia de que en este caso las variables tienen un nombre.

El principal uso de ``*args`` y ``**kwargs`` es en la definición de funciones. Ambos permiten pasar un número variable de argumentos a una función, por lo que si quieres definir una función cuyo número de parámetros de entrada puede ser variable, considera la utilización de ``*args`` o ``**kwargs`` como una opción.

#### `*args`

Te permite pasar un número variable de argumentos posicionales (es decir, una lista de valores sueltos) sin tener que definir un límite en los parámetros.
Reglas importantes de uso:

- **El nombre no importa, el asterisco sí:** El nombre *args* es solo una convención que usan todos los programadores. Podrías llamarlo *numeros* o *cosas*, y funcionará igual. Lo importante es el asterisco (``*``).
- **El tipo de dato es una Tupla:** Dentro de la función, Python convierte todos esos valores en una tupla. Por eso puedes usar estructuras como *for item in args* para revisarlos uno por uno.
- **Va al final:** Si combinas parámetros normales con *args*, el *args* siempre debe ir al final.

***Sintaxis***

```python
def Nombre_funcion(*args):
    # Dentro de la funcion, "args" funciona com una tupla
    for elemento in args:
        print(elemento)

#Llamar a la funcion (Se pasa valores separados por comas)
Nombre_funcion(valor1, valor2, ..., valorn)
```

#### `**kwargs`

Recibe valores con un nombre asignado (clave y valor), como un **diccionario**.
Reglas importantes de uso:

- **El orden de los parámetros es estricto:** Si combinas *kwargs* con otros tipos de parámetros en la definición de una función, *kwargs* siempre debe ir al final.
- **Las claves al llamar la función deben ser nombres válidos:** Cuando pasas datos a *kwargs*, las claves (los nombres de las variables) se convierten en cadenas de texto (*strings*) internamente. Por lo tanto, deben cumplir las reglas de nombres de variables de Python.
- **Las claves no se pueden duplicar en la llamada:** No puedes enviar dos veces el mismo nombre de parámetro en una sola llamada a la función.
- **No colisiones con parámetros posicionales:** Si tu función ya tiene un parámetro normal con un nombre específico, no puedes mandarle un valor a ese mismo nombre a través de *kwargs*.
- **Las claves siempre son Strings por dentro:** Dentro de la función, *kwargs* se transforma en un diccionario.

***Sintaxis***

```python
def Nombre_funcion(**kwargs):
    # Dentro de la funcion, "kwargs" funciona com un diccionario
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")

#Llamar a la funcion (Se usa la estructura nombre = valor)
Nombre_funcion(clave1 = valor1, clave2 = valor2, ..., claven = valorn)
```

---

## Funciones Integradas

Son herramientas predefinidas que están siempre disponibles en el lenguaje sin necesidad de importar ningún módulo o librería adicional.

| Funcion | Descripcion | Sintaxis | Opciones |
| :---: | :--- | :---: | :--- |
| *print()* | Muestra un mensaje o el valor de una variable en la consola. | `print("Mensaje")` | |
| *len()* | Devuelve el número de elementos que tiene un objeto, como una cadena o una lista. | `len(objeto)` | |
| *type()* | Permite conocer el tipo de dato de un objeto. *type()* también es la metaclase por defecto en Python. Puedes usarla con 3 argumentos para crear una clase en tiempo de ejecución sin usar la palabra clave class. | <ul><li>`type(objeto)`</li><li>`type(nombre_de_clase, bases, atributos_y_metodos)` | <ul><li>``nombre_de_clase``: Cadena de texto con el nombre de la clase.</li><li>``bases``: Tupla con las clases de las cuales hereda (dejar vacía () si no hereda de ninguna).</li><li>``atributos_y_metodos``: Diccionario con los atributos y funciones de la clase.</li></ul> |
| *round()* | Redondea un número decimal al entero o decimales especificados(n_decimales). Cuando un número está exactamente a la mitad (.5), Python no redondea siempre hacia arriba, sino hacia el número par más cercano | `round(numero, n_decimales)` | <ul><li>``numero``: El número entero o flotante (float) que deseas redondear.</li><li>``n_decimales`` (opcional): La cantidad de posiciones decimales a las que se redondeará. Si se omite, redondea al entero más cercano.</li></ul> |
| *enumerate()* | Toma una colección (como una lista, tupla o cadena) y devuelve un objeto enumerado que genera pares de (índice, elemento) en cada iteración. | `enumerate(iterable, start=0)` | <ul><li>``iterable``: La lista, tupla, cadena o colección a recorrer.</li><li>``start (opcional)``: El número entero desde el cual empieza a contar el índice (por defecto es 0).</li></ul> |
| *strip()* | Utiliza para eliminar todos los espacios en blanco (espacios, tabulaciones \t y saltos de línea \n) al inicio y al final de una cadena de texto | `cadena.strip([caracteres])` | <ul><li>``cadena``: La cadena de texto que deseas limpiar.</li><li>``caracteres`` (opcional): Una cadena de caracteres específicos que deseas eliminar en lugar de los espacios en blanco.</li></ul> |
| *join()* | Se utiliza para unir o concatenar todos los elementos de un iterable (como una lista, tupla o conjunto) en una sola cadena de texto (str), utilizando una cadena específica como separador. | `separador.join(iterable)` | <ul><li>``separador``: La cadena de texto que se colocará entre cada uno de los elementos.</li><li>``iterable``: La colección que contiene los textos a unir (debe contener únicamente cadenas de texto).</li></ul> |

---

## Funciones de Conversión y Estructuras

Python incluye funciones para convertir tipos de datos y construir estructuras principales:

- *int(), float(), str() y bool():* transforman valores entre enteros, decimales, textos y booleanos.
- *list(), tuple(), set() y dict():* crean o convierten elementos en listas, tuplas, conjuntos y diccionarios.

---

## Ejemplos Practicos

- [Ejemplo Funciones](/01-Fundamentos/07-Funciones/02_Funciones.py)
- [Ejemplo Funciones Posicionales](/01-Fundamentos/07-Funciones/03_Funciones_posicionales.py)
- [Ejemplo Funcion *len()*](/01-Fundamentos/07-Funciones/04_Funcion_len.py)
- [Ejemplo Funcion *type()*](/01-Fundamentos/07-Funciones/05_Funcion_type.py)
- [Ejemplo Funcion *round()*](/01-Fundamentos/07-Funciones/06_Funcion_round.py)
- [Ejemplo Funcion *enumerate()*](/01-Fundamentos/07-Funciones/07_Funcion_enumerate.py)
- [Ejemplo Funcion *strip()*](/01-Fundamentos/07-Funciones/08_Funcion_strip.py)
- [Ejemplo Funcion *join()*](/01-Fundamentos/07-Funciones/09_Funcion_join.py)

---

[Inicio](#7-funciones)

---

[Tabla de contenido principal](/Tabla_Contenido.md)

---
