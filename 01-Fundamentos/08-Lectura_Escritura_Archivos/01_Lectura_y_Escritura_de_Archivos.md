# 8. Lectura y Escritura de Archivos

---

## Tabla de Contenido

- [Lectura de Archivos](#lectura-de-archivos)
  - [Modos Principales de Lectura](#modos-principales-de-lectura)
- [Escritura de Archivos](#escritura-de-archivos)
  - [Modos Principales de Escritura](#modos-principales-de-escritura)
- [Ejemplos Practicos](#ejemplos-practicos)

---

## Lectura de Archivos

Para leer el contenido de un archivo forma segura y recomendada es utilizar la sentencia ``with open(...)``, en modo de lectura (``"r"``). Luego, podemos leer el contenido del archivo utilizando métodos como ``read()`` o ``readlines()``.
La principal ventaja de usar *with* es que Python cierra el archivo automáticamente cuando termina el bloque de código, incluso si ocurre un error durante la lectura.

***Sintaxis*** 

```python
with open("Nombre_archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
```

- **"nombre_del_archivo.txt":** La ruta o nombre del archivo que quieres abrir.
- **"r":** Significa modo lectura (*read*). Es el modo por defecto.
- **encoding="utf-8":** Asegura que se lean correctamente acentos, letras como la ñ y caracteres especiales.
- **as archivo:** Nombre de la variable temporal con la que manipularás el archivo dentro del bloque.

### Modos Principales de Lectura

Dependiendo del tamaño del archivo o de lo que quieras hacer, existen tres métodos principales para obtener los datos:

| Método | Descripción | Ideal para |
| :---: | :--- | :--- |
|``read()`` | Lee todo el contenido del archivo de golpe y lo devuelve como un solo texto (*string*). | Archivos pequeños. |
| ``readline()`` | Lee únicamente una línea a la vez. Cada vez que lo llamas, avanza a la siguiente línea. | Archivos enormes donde no quieres cargar todo en memoria. |
| ``readlines()`` | Lee todas las líneas y las devuelve en una lista, donde cada elemento es una línea. | Procesar o iterar sobre una lista de líneas. |

---

## Escritura de Archivos

Para escribir datos en un archivo, la mejor forma es abrirlo en modo de escritura (``"w"``) utilizando el bloque ``with open(...)``. Si el archivo no existe, se creará automáticamente. Si el archivo ya existe, su contenido se sobrescribirá.

***Sintaxis***

```python
with open("Nombre_archivo.txt", "modo", encoding="utf-8") as archivo:
    archivo.write("Texto a escribir\n")
```

- **write("texto"):** El método que inserta el texto.
- **"modo":** Define cómo interactúas con el archivo.
- **encoding="utf-8":** sirve para indicar con qué formato exacto debe traducir e interpretar el texto que se estás escribiendo antes de guardarlo en el disco duro.
- ***\n:*** Representa un salto de línea (enter). Si no se pones, todo el texto se escribirá en una sola línea corrida.

### Modos Principales de Escritura

| Modo | Nombre | ¿Qué hace con el archivo? |
| :---: | :--- | :--- |
| ``“w”`` | Write (Escribir) | Crea el archivo si no existe. Si ya existe, borra todo su contenido anterior y lo reemplaza por el nuevo. |
| ``“a”`` | Append (Añadir) | Crea el archivo si no existe. Si ya existe, agrega el contenido al final sin borrar nada de lo anterior. |
| ``“x”`` | Exclusive creation | Crea el archivo solo si no existe. Si el archivo ya existe, da un error *(FileExistsError)*. Útil para evitar sobreescribir datos por accidente. |

---

## Ejemplos Practicos

- [Ejemplo Lectura de Archivos](/01-Fundamentos/08-Lectura_Escritura_Archivos/02_Lectura_Archivos.py)
- [Ejemplo Escritura de Archivos](/01-Fundamentos/08-Lectura_Escritura_Archivos/03_Escritura_Archivos.py)

---

[Inicio](#8lectura-y-escritura-de-archivos)

---

[Tabla de contenido principal](/Tabla_Contenido.md)

---
