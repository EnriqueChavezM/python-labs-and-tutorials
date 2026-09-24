# 6. Estructuras de Datos

Las estructuras de datos nos permiten organizar y almacenar datos de manera eficiente en nuestros programas.

---

## Tabla de Contenido

- [6. Estructuras de Datos](#6-estructuras-de-datos)
  - [Tabla de Contenido](#tabla-de-contenido)
  - [Listas](#listas)
    - [Creación y Acceso de Listas](#creación-y-acceso-de-listas)
    - [Métodos de Listas](#métodos-de-listas)
    - [Listas de Comprensión](#listas-de-comprensión)
    - [Segmentación de Listas (*Slicing*)](#segmentación-de-listas-slicing)
  - [Tuplas](#tuplas)
    - [Creación y Acceso de Tuplas](#creación-y-acceso-de-tuplas)
    - [Métodos de Tuplas](#métodos-de-tuplas)
  - [Diccionarios](#diccionarios)
    - [Creación y Acceso de Diccionarios](#creación-y-acceso-de-diccionarios)
    - [Añadir Nuevo Par *clave-valor*](#añadir-nuevo-par-clave-valor)
    - [Métodos de Diccionarios](#métodos-de-diccionarios)
    - [Diccionarios Anidados](#diccionarios-anidados)
  - [Conjuntos](#conjuntos)
    - [Creación y Operaciones Básicas](#creación-y-operaciones-básicas)
    - [Métodos de Conjuntos](#métodos-de-conjuntos)
  - [Casting de Datos](#casting-de-datos)
    - [Casting de listas](#casting-de-listas)
  - [Ejemplos Prácticos](#ejemplos-prácticos)

---

## Listas

Es una estructura de datos mutable y ordenada que permite almacenar una colección de elementos. Los elementos de una lista pueden ser de diferentes tipos de datos y se encierran entre corchetes ``[]``, separados por comas.

### Creación y Acceso de Listas

Para crear una lista, simplemente encierra los elementos entre corchetes:

***Sintaxis***

```python
Nombre_lista = [dato1, dato2, ..., dato_n]
```

Para acceder a los elementos de una lista, se utiliza el índice del elemento entre corchetes. Los índices comienzan desde 0.

- **Ejemplo**

```python
print(Nombre_lista[0])  #Imprime el dato del indice 0
print(Nombre_lista[1])  #Imprime el dato del indice 1
...
print(Nombre_lista[n])  #Imprime el dato del indice n
```

También puedes acceder a los elementos desde el final de la lista utilizando índices negativos. El índice -1 representa el último elemento, -2 representa el penúltimo, y así sucesivamente.

- **Ejemplo**

```python
print(Nombre_lista[-1])  #Imprime el dato del indice -1
print(Nombre_lista[-2])  #Imprime el dato del indice -2
...
print(Nombre_lista[-n])  #Imprime el dato del indice -n
```

### Métodos de Listas

Las listas tienen varios métodos incorporados que nos permiten manipular y modificar los elementos de la lista.
Algunos métodos comunes son:

- *.append(elemento)*: agrega un elemento al final de la lista.
  - ***Sintaxis:*** `Nombre_lista.append(elemento)`
- *.insert(indice, elemento)*: inserta un elemento en una posición específica de la lista.
  - ***Sintaxis:*** `Nombre_lista.insert(indice, elemento)`
- *.remove(elemento)*: elimina la primera aparición de un elemento en la lista.
  - ***Sintaxis:*** `Nombre_lista.remove(elemento)`
- *.pop(indice)*: elimina y devuelve el elemento en una posición específica de la lista.
  - ***Sintaxis:*** `Nombre_lista.pop(indice)`
- *.sort()*: ordena los elementos de la lista en orden ascendente.
  - ***Sintaxis:*** `Nombre_lista.sort()`
- *.reverse()*: invierte el orden de los elementos en la lista.
  - ***Sintaxis:*** `Nombre_lista.reverse()`
- *.clear()*: Elimina todos los elementos de una lista
  - ***Sintaxis:*** `Nombre_lista.clear()`
- *.count(elemento)*:  Entrega el numero de veces que se repite un elemento en la lista
  - ***Sintaxis:*** `Nombre_lista.count(elemento)`
- *.index(elemento)*: Sirve para buscar la primer coincidencia de un elemento y saber en qué posición (índice) se encuentra
  - ***Sintaxis:*** `Nombre_lista.index(elemento)`
- *del Lista [elemento]*:  Borra un elemento en un índice específico o corta secciones enteras.
  - ***Sintaxis:*** `del Nombre_lista`

### Listas de Comprensión

Las listas de comprensión son una forma concisa de crear nuevas listas basadas en una secuencia existente. Permiten filtrar y transformar los elementos de una lista en una sola línea de código.

***Sintaxis***

```python
Nueva_lista = [excreción for elemento in Nombre_lista if condición]
```

**Ejemplo:** Se crea una nueva lista llamada cuadrados, que contiene los cuadrados de los números pares de la lista números. La expresión x ** 2 eleva cada elemento al cuadrado, y la condición if x % 2 == 0 filtra solo los números pares.

```python
números = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in números if x % 2 == 0]  # Crea una nueva lista con los cuadrados de los números pares
print("cuadrados de los números impares:", cuadrados)  # Imprime [4, 16]
```

### Segmentación de Listas (*Slicing*)

Es una técnica fundamental que te permite extraer una sublista (o fragmento) a partir de una lista existente, indicando los índices de inicio, fin y paso.

Es una herramienta imprescindible para la automatización, ya que permite filtrar lotes de datos, procesar registros (logs) en bloques o ignorar encabezados de archivos de forma muy eficiente.

***Sintaxis***

```python
lista[inicio : fin : paso]
```

- *inicio*: El índice donde comienza la extracción **(incluido)**. Si se omite, toma por defecto 0.
- *fin*: El índice donde termina la extracción **(excluido; no toma este elemento)**. Si se omite, va hasta el final de la lista.
- *paso*: El salto entre elementos **(opcional, por defecto es 1)**.

---

## Tuplas

Es una estructura de datos inmutable y ordenada que permite almacenar una colección de elementos. Los elementos de una tupla se encierran entre paréntesis ``()``, separados por comas.

### Creación y Acceso de Tuplas

Para crear una tupla, encierra los elementos entre paréntesis:

***Sintaxis***

```python
Nombre_Tupla = (dato1, dato2, ..., dato_n)
```

Para acceder a los elementos, se utiliza el índice del elemento entre corchetes. Los índices comienzan desde 0. También puedes acceder a los elementos desde el final de la lista utilizando índices negativos. El índice -1 representa el último elemento, -2 representa el penúltimo, y así sucesivamente.

- **Ejemplo**

```python
print(Nombre_Tupla[0])  #Imprime el dato del indice 0
print(Nombre_Tupla[1])  #Imprime el dato del indice 1
...
print(Nombre_Tupla[n])  #Imprime el dato del indice n
```

A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas. No se pueden agregar, eliminar o cambiar elementos en una tupla existente.
Las tuplas son útiles cuando necesitas almacenar una colección de elementos que no deben modificarse, como coordenadas o datos de configuración.

### Métodos de Tuplas

Aunque las tuplas son inmutables, Python proporciona varios métodos útiles para trabajar con ellas:

- *.count(elemento):* devuelve el número de veces que aparece un elemento en la tupla.
  - ***Sintaxis*** `Nombre_tupla.count(elemento)`
- *.index(elemento):* devuelve el índice de la primera aparición de un elemento en la tupla. Opcionalmente, se puede especificar el inicio y fin de la búsqueda.
  - ***Sintaxis*** `Nombre_tupla.index(elemento)`
- *len(tupla):* aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.
  - ***Sintaxis*** `len(Nombre_tupla)`

---

## Diccionarios

Un diccionario es una estructura de datos mutable y no ordenada que permite almacenar pares de **clave-valor**. Cada elemento en un diccionario consiste en una clave única y su valor correspondiente. Los diccionarios se encierran entre llaves ``{}`` o utilizando la el constructor ``dict()``. Cada par **clave-valor** se escribe como ``key: value``, y varios pares se separan mediante comas.

### Creación y Acceso de Diccionarios

Para crear un diccionario, utiliza llaves o constructor ``dict`` y separa las claves y valores con dos puntos.

***Sintaxis***

```python
#Opción 1
Nombre_diccionario1 = {
  clave1 : valor1,
  ...
  claven : valor_n
}
# Opción 2
Nombre_diccionario2 = dict(
  clave1 = valor1
  ...
  claven = valor_n
)
# Opción 3
Nombre_diccionario3 = dict([
  (clave1 , valor1),
  ...
  (claven , valor_n),
])
```

Para acceder a los valores de un diccionario, utiliza la clave correspondiente entre corchetes:

- **Ejemplo**

```python
print(Nombre_diccionario[0])  #Imprime el dato del indice 0
print(Nombre_diccionario[1])  #Imprime el dato del indice 1
...
print(Nombre_diccionario[n])  #Imprime el dato del indice n
```

### Añadir Nuevo Par *clave-valor*

Puedes añadir nuevos pares clave-valor o actualizar los existentes.

- **Añadir un nuevo par clave-valor:**
  
  ```python
  my_dict = {}              # Comenzar con un diccionario vacío
  my_dict["name"] = "Alice" # Añadir un nuevo par clave-valor
  my_dict["age"] = 30       # Añadir un nuevo par clave-valor
  print(my_dict)            # Salida: {'name': 'Alice'}
  ```
  
- **Actualizar un valor existente:**
  
  ```python
  my_dict["age"] = 31       # Actualizar la edad
  print(my_dict)            # Salida: {'name': 'Alice', 'age': 31}
  ```

### Métodos de Diccionarios

Los diccionarios en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

- *.keys():* devuelve una vista de todas las claves del diccionario.
  - ***Sintaxis:*** `Nombre_diccionario.keys()`
- *.values():* devuelve una vista de todos los valores del diccionario.
  - ***Sintaxis:*** `Nombre_diccionario.values()`
- *.items():* devuelve una vista de todos los pares clave-valor del diccionario.
  - ***Sintaxis:*** `Nombre_diccionario.items()`
- *.update(clave, valor):* actualiza el diccionario con los pares clave-valor de otro diccionario.
  - ***Sintaxis:*** `Nombre_diccionario.update({clave, valor})`
- *get(key, default):* Devuelve el valor para la clave especificada. Si no se encuentra la clave, devuelve el valor predeterminado (o None si no se especifica ningún valor predeterminado).
  - ***Sintaxis:*** `Nombre_diccionario.get(clave)`
- *.pop():*  elimina un par clave-valor y devuelve el valor eliminado.
  - ***Sintaxis:*** `Nombre_diccionario.pop(clave)`
- *del diccionario:* Borra la clave y su valor asociado directamente. Si la clave no existe, lanza un error (KeyError).
  - ***Sintaxis:*** `del Nombre_diccionario[clave]`

### Diccionarios Anidados

Un diccionario anidado es un diccionario dentro de otro diccionario. Te permite organizar estructuras de datos complejas, lo que facilita trabajar con información relacionada.

Los diccionarios anidados son **útiles cuando** necesitas agrupar información relacionada, como almacenar detalles sobre estudiantes, empleados o productos.

---

## Conjuntos

### Creación y Operaciones Básicas

Para crear un conjunto, utiliza llaves o la función `set()`:

***Sintaxis***

```python
Nombre_conjunto1 = {valor1, valor2, ..., valor_n}
Nombre_conjunto2 = set([valor1, valor2, ..., valor_n])
```

Los conjuntos admiten operaciones matemáticas de conjuntos como:

- Unión (``|``)
- Intersección (``&``)
- Diferencia (``-``)
- Diferencia simétrica (``^``).

### Métodos de Conjuntos

Los conjuntos en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

- *.add(elemento):* Agrega un elemento al conjunto.
  - ***Sintaxis*** `Nombre_conjunto.add(elemento)`
- *.remove(elemento):* Elimina un elemento del conjunto. Si el elemento no existe, genera un error.
  - ***Sintaxis*** `Nombre_conjunto.remove(elemento)`
- *.discard(elemento):* Elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
  - ***Sintaxis*** `Nombre_conjunto.discard(elemento)`
- *.pop():* Elimina un elemento aleatorio del conjunto
  - ***Sintaxis*** `Nombre_conjunto.pop()`
- *.union():* Realiza una fusión entre 2 conjuntos
  - ***Sintaxis*** `Nombre_conjunto.union(Nombre_conjunto2)`
- *.clear():/ Elimina todos los elementos del conjunto.
  - ***Sintaxis*** `Nombre_conjunto.clear()`

---

## Casting de Datos

Hace referencia a forzar o convertir explícitamente una estructura de datos de un tipo de dato a otro.

### Casting de listas

Puedes usar la función ``list()`` para convertir iterables como tuplas, cadenas o rangos en listas. Esto es útil para trabajar con elementos en un **formato modificable**.

- Convertir una tupla en una lista:
  
  ```python
  my_tuple = (1, 2, 3)
  my_list = list(my_tuple)
  print(my_list)  # [1, 2, 3]
  ```

- Convertir una cadena la divide en caracteres individuales:
  
  ```python
  my_string = "hello"
  my_list = list(my_string)
  print(my_list)  # ['h', 'e', 'l', 'l', 'o']
  ```

- Convertir un rango a una lista devuelve todos los números a la vez:

  ```python
  my_range = range(5)
  my_list = list(my_range)
  print(my_list)  # [0, 1, 2, 3, 4]
  ```

---

## Ejemplos Prácticos

- [Ejemplo Listas](/01-Fundamentos/06-Estructuras_de_Datos/02_Listas.py)
- [Ejemplo Tuplas](/01-Fundamentos/06-Estructuras_de_Datos/03_Tuplas.py)
- [Ejemplo Diccionarios](/01-Fundamentos/06-Estructuras_de_Datos/04_Diccionarios.py)
- [Ejemplo Conjuntos](/01-Fundamentos/06-Estructuras_de_Datos/05_Conjuntos.py)
- [Ejemplo Casting de Datos](/01-Fundamentos/06-Estructuras_de_Datos/06_Casting_Estructura_Datos.py)

---

[Inicio](#6-estructuras-de-datos)

---

[Tabla de contenido principal](/Tabla_Contenido.md)

---
