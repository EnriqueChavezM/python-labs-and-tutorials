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

**Ejemplo**
Se crea una nueva lista llamada cuadrados, que contiene los cuadrados de los números pares de la lista numeros. La expresión x ** 2 eleva cada elemento al cuadrado, y la condición if x % 2 == 0 filtra solo los números pares.

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros if x % 2 == 0]  # Crea una nueva lista con los cuadrados de los números pares
print("cuadrados de los números impares:", cuadrados)  # Imprime [4, 16]
```

---

## Tuplas



### Creación y Acceso de Tuplas
### Métodos de Tuplas

---

## Diccionarios
### Creación y Acceso de Diccionarios
### Métodos de Diccionarios

---

## Conjuntos
### Creación y Operaciones Básicas
### Métodos de Conjuntos

---

## Ejemplos Practicos]