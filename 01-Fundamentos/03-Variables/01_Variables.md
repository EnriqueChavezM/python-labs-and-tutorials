# 3. Variables

En Python, no es necesario declarar una variable (especificando el tipo de datos) antes de usar, ya que es un lenguaje de tipado dinámico, él se encarga de reconocer y trabajar con las variables almacenadas, es posible cambiar el tipo de dato durante la ejecución. Si quieres crear una variable, solo tienes que escribir un nombre válido para la variable y asignarle algún valor mediante el operador de asignación

---

## Tabla de Contenido

- [Alcance de Variables (Local vs Global)](#alcance-de-variables-local-vs-global)
- [Tipo de Variables](#tipo-de-variables)
- [Casteo de datos o casting](#casteo-de-datos-o-casting)
  - [Tipos de Casting que Existen](#tipos-de-casting-que-existen)
- [Variables Constantes](#variables-constantes)
- [Asignación de múltiples variables](#asignación-de-múltiples-variables)
- [Intercambio de variables](#intercambio-de-variables)
- [Variables de marcador de posición](#variables-de-marcador-de-posición)
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

## Intercambio de variables

Intercambiar variables es una operación común en la que se intercambian los valores de dos variables. Python ofrece una forma sencilla y elegante de intercambiar variables sin necesidad de una variable temporal, a diferencia de muchos otros lenguajes de programación.

- **Método tradicional (usando una variable temporal):**
  
  ```python
  a = 10
  b = 20
  temp = a
  a = b
  b = temp
  print(a)  # Salida: 20
  print(b)  # Salida: 10
  ```

- **Forma Asignación simultánea:

  ```python
  a = 10
  b = 20
  a, b = b, a
  print(a)  # Salida: 20
  print(b)  # Salida: 10
  ```

  Los valores de ``b`` y ``a`` se asignan simultáneamente a ``a`` y ``b``, respectivamente. Este enfoque es más legible y **no requiere ninguna variable adicional**.

---

## Variables de marcador de posición

Una variable de marcador de posición es una variable que se utiliza para contener un valor temporalmente, a menudo durante la ejecución de un bloque de código específico. Las variables de marcador de posición se utilizan comúnmente en situaciones en las que es necesario realizar operaciones sobre un valor sin cambiar la variable original.
Una convención común para las variables de marcador de posición es utilizar un guion bajo ``_`` como nombre de la variable.

- **Uso de un guion bajo simple _:**
  En este ejemplo, ``_`` se utiliza como un marcador de posición porque la variable del bucle no es necesaria en el cuerpo del mismo.

  ```python
  for _ in range(5):
    print("Looping")
  # Salida:
  # Looping
  # Looping
  # Looping
  # Looping
  # Looping
  ```

- **Uso de múltiples guiones bajos simples:**
  En los casos en los que tienes múltiples valores y solo necesitas algunos de ellos, puedes usar el carácter de guion bajo varias veces como variables de marcador de posición independientes.
  **Por ejemplo:**
  Aquí, _ se utiliza para ignorar el segundo, tercer y cuarto elemento de la tupla.

  ```python
  data = (1, 2, 3, 4, 5)
  first, _, _, _, last = data
  print(first)  # Salida: 1
  print(last)   # Salida: 5
  ```

---

## Ejemplo Practico

- [Ejemplo Variables](/01-Fundamentos/03-Variables/02_Ejemplo_Variables.py)
- [Asignacion de variables](/01-Fundamentos/03-Variables/03_Asignación_múltiples_variables.py)

---

[Inicio](#3-variables)

---

[Tabla de contenido principal](/Tabla_Contenido.md)

---
