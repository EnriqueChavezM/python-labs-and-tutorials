# 6. Estructuras de Datos

Las estructuras de datos nos permiten organizar y almacenar datos de manera eficiente en nuestros programas.

---

## Tabla de Contenido

- [Listas](#listas)
  - [Creación y Acceso de Listas](#creación-y-acceso-de-listas)
  - [Métodos de listas](#métodos-de-listas)
  - [Listas de Comprensión](#listas-de-comprensión)
- [Tuplas](#tuplas)
  - [Creación y Acceso de Tuplas](#creación-y-acceso-de-tuplas)
  - [Métodos de Tuplas](#métodos-de-tuplas)
- [Diccionarios](#diccionarios)
  - [Creación y Acceso de Diccionarios](#creación-y-acceso-de-diccionarios)
  - [Métodos de Diccionarios](#métodos-de-diccionarios)
- [Conjuntos](#conjuntos)
  - [Creación y Operaciones Básicas](#creación-y-operaciones-básicas)
  - [Métodos de Conjuntos](#métodos-de-conjuntos)
- [Ejemplos Practicos](#ejemplos-practicos)

---

## Listas

Es una estructura de datos mutable y ordenada que permite almacenar una colección de elementos. Los elementos de una lista pueden ser de diferentes tipos de datos y se encierran entre corchetes ``[]``, separados por comas.

### Creación y Acceso de Listas

Para crear una lista, simplemente encierra los elementos entre corchetes:

***Sintaxis***

```python
Nombre_lista = [dato1, dato2, ..., daton]
```

Para acceder a los elementos de una lista, se utiliza el índice del elemento entre corchetes. Los índices comienzan desde 0.

**Ejemplo**

```python
print(Nombre_lista[0])  #Imprie el dato del indice 0
print(Nombre_lista[1])  #Imprie el dato del indice 1
...
print(Nombre_lista[n])  #Imprie el dato del indice n
```

También puedes acceder a los elementos desde el final de la lista utilizando índices negativos. El índice -1 representa el último elemento, -2 representa el penúltimo, y así sucesivamente.

**Ejemplo**

```python
print(Nombre_lista[-1])  #Imprie el dato del indice -1
print(Nombre_lista[-2])  #Imprie el dato del indice -2
...
print(Nombre_lista[-n])  #Imprie el dato del indice -n
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
Nueva_lista = [exprecion for elemento in Nombre_lista if condicion]
```

**Ejemplo:** Se crea una nueva lista llamada cuadrados, que contiene los cuadrados de los números pares de la lista numeros. La expresión x ** 2 eleva cada elemento al cuadrado, y la condición if x % 2 == 0 filtra solo los números pares.

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros if x % 2 == 0]  # Crea una nueva lista con los cuadrados de los números pares
print("cuadrados de los números impares:", cuadrados)  # Imprime [4, 16]
```

---

## Tuplas

Es una estructura de datos inmutable y ordenada que permite almacenar una colección de elementos. Los elementos de una tupla se encierran entre paréntesis ``()``, separados por comas.

### Creación y Acceso de Tuplas

Para crear una tupla, encierra los elementos entre paréntesis:

***Sintaxis***

```python
Nombre_Tupla = (dato1, dato2, ..., daton)
```

Para acceder a los elementos, se utiliza el índice del elemento entre corchetes. Los índices comienzan desde 0.

**Ejemplo**

```python
print(Nombre_Tupla[0])  #Imprie el dato del indice 0
print(Nombre_Tupla[1])  #Imprie el dato del indice 1
...
print(Nombre_Tupla[n])  #Imprie el dato del indice n
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

Un diccionario es una estructura de datos mutable y no ordenada que permite almacenar pares de clave-valor. Cada elemento en un diccionario consiste en una clave única y su valor correspondiente. Los diccionarios se encierran entre llaves ``{}`` o utilizando la el constructor ``dict()``, y los pares clave-valor se separan por comas

### Creación y Acceso de Diccionarios

Para crear un diccionario, utiliza llaves o constructor ``dict`` y separa las claves y valores con dos puntos.

***Sintaxis***

```python
#Opcion 1
Nombre_diccionario1 = {
  clave1 : valor1
  ...
  claven : valorn
}
# Opcion 2
Nombre_diccionario2 = dict(
  clave1 = valor1
  ...
  claven = valorn
)
# Opcion 3
Nombre_diccionario3 = dict([
  (clave1 , valor1),
  ...
  (claven , valorn),
])
```

Para acceder a los valores de un diccionario, utiliza la clave correspondiente entre corchetes:

**Ejemplo**

```python
print(Nombre_diccionario[0])  #Imprie el dato del indice 0
print(Nombre_diccionario[1])  #Imprie el dato del indice 1
...
print(Nombre_diccionario[n])  #Imprie el dato del indice n
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
  - ***Sintaxis:*** `Nombre_diccionario.updat({clave, valor})`
- *del diccionario:* Borra la clave y su valor asociado directamente. Si la clave no existe, lanza un error (KeyError).
  - ***Sintaxis:*** `del Nombre_diccionario[clave]`

---

## Conjuntos

### Creación y Operaciones Básicas

Para crear un conjunto, utiliza llaves o la función `set()`:

***Sintaxis***

```python
Nombre_conjunto1 = {valor1, valor2, ..., valorn}
Nombre_conjunto2 = set([valor1, valor2, ..., valorn])
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

## Ejemplos Practicos

- [Ejemplo Listas](/01-Fundamentos/06-Estructuras_de_Datos/02_Listas.py)
- [Ejemplo Tuplas](/01-Fundamentos/06-Estructuras_de_Datos/03_Tuplas.py)
- [Ejemplo Diccionarios](/01-Fundamentos/06-Estructuras_de_Datos/04_Diccionarios.py)
- [Ejemplo Conjuntos](/01-Fundamentos/06-Estructuras_de_Datos/05_Conjuntos.py)
