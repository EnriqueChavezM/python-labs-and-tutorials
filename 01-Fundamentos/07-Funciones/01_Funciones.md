# 7. Funciones

Las funciones son bloques de código reutilizables que nos permiten encapsular tareas específicas y ejecutarlas cuando sea necesario. Las funciones nos ayudan a organizar nuestro código, evitar la repetición y hacer que nuestros programas sean más modulares y fáciles de mantener.

---

## Tabla de Contenido

- [Funciones de Usuario](#funciones-de-usuario)
  - [Parámetros y Argumentos](#parámetros-y-argumentos)
  - [Funciones con número variable de argumentos](#funciones-con-número-variable-de-argumentos)
    - [`*args`](#args)
    - [`**kwargs`](#kwargs)
- [Ejemplos Practicos](#ejemplos-practicos)

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

## Ejemplos Practicos

- [Ejemplo Funciones](/01-Fundamentos/07-Funciones/02_Funciones.py)
- [Ejemplo Funciones Posicionales](/01-Fundamentos/07-Funciones/03_Funciones_posicionales.py)

---

[Inicio](#7-funciones)

---

[Tabla de contenido principal](/Tabla_Contenido.md)

---
