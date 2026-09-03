# Entradas y Salidas de datos (I/O)

---

## Tabla de Contenido

- [Entrada de Datos](#entrada-de-datos)
  - [Conversión de Tipos (Casteo)](#conversión-de-tipos-casteo)
  - [Recibir múltiples datos en una sola línea](#recibir-múltiples-datos-en-una-sola-línea)
  - [Limpieza de datos (Evitar errores del usuario)](#limpieza-de-datos-evitar-errores-del-usuario)
  - [Validación con try / except (Para que no falle)](#validación-con-try--except-para-que-no-falle)
- [Salida de Datos](#salida-de-datos)
  - [Parámetros ocultos](#parámetros-ocultos)
  - [Caracteres especiales](#caracteres-especiales)
  - [Trucos visuales](#trucos-visuales)
- [Ejemplo practico](/01-Fundamentos/02-Entradas_y_Salidas/02_Ejemplo_Entradas_Salidas.py)

---

## Entrada de Datos

Para obtener información del usuario durante la ejecución del programa, podemos utilizar la función ``input()``. Esta función muestra un mensaje en la pantalla y espera a que el usuario ingrese un valor.

***Sintaxis***

```python
nombre_variable = input("Mensaje opcional")
```

### Conversión de Tipos (Casteo)

Por defecto, ``input()`` siempre te va a entregar un texto (``string``), incluso si el usuario escribe un número. Si es necesario hacer matemáticas, se tiene que transformar el tipo.

| Tipo de dato deseado | Codigo para transformar |
| :--- | :---: |
| Entero(Sin decimales) | `edad = int(input("Tu edad: "))` |
| Decimal(Flotante) | `precio = float(input("Precio: "))` |
| Booleano (True / False) | `acepta = input("¿Si o No?") == "Si"` |

### Recibir múltiples datos en una sola línea

Si quieres que el usuario escriba varias cosas separadas por un espacio o una coma, puedes usar el método ``.split()`` al final del ``input()``.

**Ejemplo:**

```python
#El usuario escribe: Juan Perez 28
nombre, apellido, edad = input("Escribe tu nombre, apellido y edad separados por espacio:").split()
```

### Limpieza de datos (Evitar errores del usuario)

Errores como presionar la barra espaciadora por accidente o usar mayúsculas cuando pediste minúsculas. Puedes encadenar métodos para "limpiar" la entrada

- ``.strip()``: Borra los espacios fantasma al inicio y al final
- ``.title()``: Pone la primera letra en mayúscula
- ``.lower()``: Convierte todo a minúsculas

**Ejemplo:**

```python
respuesta = input("¿Quieres Salir? (si/no: )").strip().lower()
```

### Validación con try / except (Para que no falle)

Si le pides un número entero al usuario usando ``int(input())`` y este escribe la palabra **"hola"**, tu programa se va a cerrar con un error de inmediato ``(ValueError)``.La forma profesional de usar ``input()`` para números es meterlo dentro de un ciclo ``while`` infinito con un detector de errores.

**Ejemplo:**

```python
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break #Si el numero es válido, rompe el ciclo y continúa
    except ValueError:
        print("❌ Ingreso un valor invaliddo. Intenta otra vez.")
print(f"Tu edad es: {edad} años")
```

---

## Salida de Datos

Para mostrar información en la pantalla, utilizamos la función ``print()``. Esta función toma uno o más argumentos y los muestra en la consola.

**Combinar Texto y Vatiables**

| Método | Características | Ejemplos |
| :---: | :--- | :---: |
| Separado por comas | Añade un espacio automático entre los elementos | `print("Hola", nombre_variable)` |
| F-strings | Lleva una f al inicio. Permite meter variables directo entre llaves o  procesar datos antes de imprimirlos | `print(f"Hola {nombre_variable}")` |
| Metodo ``.format()`` | Usa llaves como sustitutos y los llena en orden al fina | `print("Hola {}".format(nombre_variable))` |
| Concatenación | Pega los textos. Si la variable es un número, es necesario realisar un casteo a string | `print("Hola" + nombre_variable)` |

> [!WARNING]
> Las formas de separacion por comas y concatenear requiere que la variable sea string

### Parámetros ocultos

La función ``print()`` tiene *"configuraciones de fábrica"* que puedes modificar usando argumentos especiales dentro del paréntesis:

- `sep="Separador personalizado"`: Por defecto, las comas añaden un espacio. Con ``sep=`` se puedes cambiar ese espacio por lo que se ocupe (guiones, barras, saltos de línea).

    *Ejemplo*

    ```python
    print("texto1", "texto2", sep= "-") #Resultado texto1-texto2
    ```

- `end="Final de línea personalizado"`: Por defecto, cada ``print()`` da un *"salto de línea"* (como un Enter). Con ``end=`` puedes hacer que el próximo ``print()`` se quede en el mismo renglón.

    *Ejemplo*

    ```python
    print("texto1", end= "...") #Resultado texto1...
    ```

### Caracteres especiales

Puedes meter comandos ocultos dentro del texto usando la barra invertida ``\``:

- `\n`: Da un salto de línea (un Enter interno).

    *Ejemplo*

    ```python
    print("Linea 1\nLinea2\nLinean") #Imprime cada palabra en un renglón diferente
    ```

- `\t`:Agrega una tabulación (un espacio grande como de cuatro espacios).

    *Ejemplo*

    ```python
    print("Producto\tPrecio")   #Imprime: Producto  Precio
    print("Manzana\t$1.50")     #Imprime: Manzana   $1.50
    ```

### Trucos visuales

- **Multiplicar texto:** Puedes usar el signo ``*`` para repetir un carácter y crear separadores visuales rápidamente.

    *Ejemplo*

    ```python
    # Crea una línea divisoria
    print("-" * 10) 
    #Imprime: ----------
    ```

- **Textos de múltiples líneas:** Si usas comillas triples ``""" """``, puedes escribir párrafos enteros respetando los saltos de línea exactos que des en tu teclado.

    *Ejemplo*

    ```python
    # Imprime un bloque de texto libre
    print("""
    MENÚ PRINCIPAL
    1. Iniciar Juego
    2. Configuración
    3. Salir
    """) 
    ```

---
