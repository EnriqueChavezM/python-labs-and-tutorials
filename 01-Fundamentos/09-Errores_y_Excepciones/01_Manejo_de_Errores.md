# 9. Manejo de errores y excepciones

---

## Tabla de Contenido

- [Errores Comunes](#errores-comunes)
- [Manejo de excepciones](#manejo-de-excepciones)
  - [Declaración try](#declaración-try)
  - [Declaración except](#declaración-except)
  - [Declaración finally](#declaración-finally)
- [Excepciones de Usuario](#excepciones-de-usuario)
- [Ejemplos Practicos](#ejemplos-practicos)

---

## Errores Comunes

Estos son solo algunos ejemplos de errores comunes. Cuando ocurre un error, Python genera una excepción y muestra un mensaje de error que incluye el tipo de excepción y una descripción del problema.

- **Error de sintaxis (*SyntaxError*):** Ocurre cuando el código no sigue las reglas de sintaxis de Python, como olvidar dos puntos después de una declaración de función o un bucle.
- **Error de nombre (*NameError*):** Ocurre cuando se hace referencia a una variable o función que no ha sido definida.
- **Error de tipo (*TypeError*):** Ocurre cuando se realiza una operación con tipos de datos incompatibles, como intentar sumar un número y una cadena.
- **Error de índice (*IndexError*):** Ocurre cuando se intenta acceder a un índice fuera del rango válido de una lista o secuencia.
- **Error de indentación (*IndentationError*):** Ocurre cuando añades espacios o tabulaciones al principio de una línea sin que la estructura del código lo requiera.

---

## Manejo de excepciones

El manejo de excepciones nos permite capturar y manejar errores de manera controlada

### Declaración try

Permite que el programa intente ejecutar una acción que podría fallar sin que el programa se detenga por completo o se cierre con un error en la pantalla.

***Sintaxis***

```python
try:
    # Código que intenta ejecutar
    # (Puede generar un error)
    pass
except Tipo_Error:
    #Código que se ejecuta SOLO si ocurre ese error específico
    pass
```

### Declaración except

El bloque *except* especifica el tipo de excepción que se desea capturar y manejar. Puedes tener múltiples bloques *except* para manejar diferentes tipos de excepciones.
 Trabaja siempre de la mano con *try*. Su única función es activarse cuando algo sale mal dentro del bloque *try* para evitar que el programa se rompa o se cierre de golpe.

***Sintaxis***

```python
try:
    #Código principal a ejecutar
    pass
except Tipo_Error1:
    #Se ejecuta si ocurre el error "Tipo_Error1"
    pass
except Tipo_Error2:
    #Se ejecuta si ocurre el error "Tipo_Error2"
    pass
```

### Declaración finally

Trabaja al final de una estructura *try-except* y su única regla es que **siempre se va a ejecutar**, sin importar si el código funcionó perfectamente o si ocurrió un error catastrófico. Se usa principalmente para tareas de limpieza obligatorias, como cerrar un archivo, desconectar una base de datos o apagar un proceso, asegurando que la computadora no deje recursos abiertos por error.

***Sintaxis***

```python
try:
    #Código principal a ejecutar
    pass
except Tipo_Error1:
    #Se ejecuta si ocurre el error "Tipo_Error1"
    pass
finally:
    #Código que se EJECUTA SIEMPRE HAYA ERROR O NO
    pass
```

---

## Excepciones de Usuario

Para crear una excepción de usuario, debes crear una clase que *herede (copie las propiedades)* de la clase base exception o de una de sus subclases. Para usarla,  debe **LANZARLA** a proposito usando  la palabra clabe *raise*

***Sintaxis***

```python
class Nombre_Error(Exception):
    "Texto opcional que explica cuándo ocurre este error."
    pass
def Nombre_Funcion():
    #Codigo que puede generar una excepción personalizada
    if condicion:
        raise Nombre_Error("Mensaje personalizado de error")
try:
    Nombre_Funcion()
except Nombre_Error as error:
    print(f"Mensaje Error: {Nombre_Error}")
```

---

## Ejemplos Practicos

- [Ejemplo Errores](/01-Fundamentos/09-Errores_y_Excepciones/02_Errores.py)
- [Manejo de Excepciones](/01-Fundamentos/09-Errores_y_Excepciones/03_Manejo_de_Excepciones.py)
- [Excepciones de Usuario](/01-Fundamentos/09-Errores_y_Excepciones/04_Excepciones_Usuario.py)

---
