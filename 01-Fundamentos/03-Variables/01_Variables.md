# 3. Variables

En Python, no es necesario declarar una variable (especificando el tipo de datos) antes de usar, ya que es un lenguaje de tipado dinámico, él se encarga de reconocer y trabajar con las variables almacenadas, es posible cambiar el tipo de dato durante la ejecución. Si quieres crear una variable, solo tienes que escribir un nombre válido para la variable y asignarle algún valor mediante el operador de asignación

---

## Tabla de Contenido

- [Alcance de Variables (Local vs Global)](#alcance-de-variables-local-vs-global)
- [Tipo de Variables](#tipo-de-variables)
- [Casteo de datos o casting](#casteo-de-datos-o-casting)
  - [Tipos de Casting que Existen](#tipos-de-casting-que-existen)
- [Ejemplo practico](/01-Fundamentos/03-Variables/02_Ejemplo_Variables.py)

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
