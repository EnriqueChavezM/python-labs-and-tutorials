# 3. Variables

En Python, no es necesario declarar una variable (especificando el tipo de datos) antes de usar, ya que es un lenguaje de tipado dinámico, él se encarga de reconocer y trabajar con las variables almacenadas, es posible cambiar el tipo de dato durante la ejecución. Si quieres crear una variable, solo tienes que escribir un nombre válido para la variable y asignarle algún valor mediante el operador de asignación

---

## Tabla de Contenido

- [Alcance de Variables (Local vs Global)](#alcance-de-variables-local-vs-global)
- [Tipo de Variables](#tipo-de-variables)
- [Casteo de datos o casting](#casteo-de-datos-o-casting)
  - [Tipos de Casting que Existen](#tipos-de-casting-que-existen)
- [Variables Constantes](#variables-constantes)
- [Asignación de múltiples variables]
- [Ejemplo practico](#ejemplo-practico)

---

## Alcance de Variables (Local vs Global)

Las variables definidas dentro de una función tienen un alcance local, lo que significa que solo son accesibles dentro de la función. Por otro lado, las variables definidas fuera de cualquier función tienen un alcance global y pueden ser accedidas desde cualquier parte del programa.

---

## Tipo de Variables

- **Enteros (int):** Son todos los números positivos o negativos, incluido el 0. Este tipo de dato no tiene límites en Python.
- **Flotante (float):** Son todos los números que incluyan decimales, es decir, que tengan un punto p "separador" entre 2 números.
- **Cadenas (strings):** Es cualquier texto encerrado entre comillas, sin importar si son simples (``' '``) o dobles (``" "``). 
- **Booleanos (bool):** Es el tipo de variable que devuelve únicamente un True si el valor es verdadero y un False si el valor es falso.

---

## Casteo de datos o casting

Hace referencia a forzar o convertir explícitamente una variable de un tipo de dato a otro.

### Tipos de Casting que Existen

Existen dos formas en las que un dato cambia de tipo:

- **Casting Implícito (Automático):** El propio lenguaje hace la conversión sin que tú se lo pidas, porque sabe que no se perderá información.
   **Ejemplo:** Si sumas un número entero (5) con un número decimal (2.5), Python convierte automáticamente el 5 a 5.0 para poder hacer la operación matemática correctamente.
- **Casting Explícito (Manual):** Es el que tú escribes directamente en el código usando funciones como *str(), int(), float()*, etc. Ocurre cuando el lenguaje no puede adivinar qué quieres hacer o cuando hay riesgo de modificar el valor.
  
  ```python
  nombre = "Enrique"      #variable de tipo str
  numero = 1234567890     #variable de tipo int
  #Casting de variable int a str
  print("Hala " + nombre + " tu numero es: " + str(numero))
  ```

Para concatenar una variable de tipo *int* es necesario primero convertir el valor de la variable a cadena para evitar errores o perdida de información *(str(variable))*.

| Funcion | Descripcion | Ejemplo | Resultado |
| :---: | :---: | :---: | :---: |
| *str()* | Convierte cualquier cosa a texto | ``str(100)`` | "100" |
| *int()* | Convierte a número entero | ``int("25")`` | 25 |
| *float()* | Convierte a número decimal | ``float("3.14")`` | 3.14 |
| *bool()* | Convierte a booleano (True/False) | ``bool(1)`` | True |

> [!NOTA]
> No todo se puede castear a cualquier cosa. Si intentas hacer *int("hola")*, el programa va a fallar ``(Value Error)`` porque la palabra "hola" no tiene una representación numérica lógica.

---

## Variables Constantes

En programación, una **constante** es un tipo de variable cuyo **valor no se puede cambiar durante la ejecución de un programa**. Las constantes son útiles para definir valores que se utilizan varias veces a lo largo de un programa, como constantes matemáticas como PI o el número de horas de un día.

En Python, *no existe una aplicación* estricta de las constantes como en algunos otros lenguajes (como c++). Sin embargo, existe una convención ampliamente adoptada para indicar que una variable debe tratarse como una constante. Esto se hace escribiendo el nombre de la variable usando únicamente letras mayúsculas, a menudo con guiones bajos para separar las palabras.

**Ejemplo**

```python
PI = 3.14159
HOURS_IN_A_DAY = 24
MAX_USERS = 100
```

---

## Asignación de múltiples variables

Puedes asignar valores a múltiples variables en una sola línea. Esta característica puede hacer que tu código sea más conciso y legible.

- **Asignaciones múltiples básicas:**

  ```python
  a, b, c = 1, 2, 3
  print(a)  # Salida: 1
  print(b)  # Salida: 2
  print(c)  # Salida: 3
  ```

- **Asignar el mismo valor a múltiples variables:**

  ```python
  x = y = z = 10
  print(x)  # Salida: 10
  print(y)  # Salida: 10
  print(z)  # Salida: 10
  ```

- **Asignación de valores de una lista (desempaquetado):**

  ```python
  numbers = [4, 5, 6]
  a, b, c = numbers
  print(a)  # Salida: 4
  print(b)  # Salida: 5
  print(c)  # Salida: 6
  ```
  
---

## Ejemplo Practico

- [Ejemplo Variables](/01-Fundamentos/03-Variables/02_Ejemplo_Variables.py)

---

[Inicio](#3-variables)

---

[Tabla de contenido principal](/Tabla_Contenido.md)

---
