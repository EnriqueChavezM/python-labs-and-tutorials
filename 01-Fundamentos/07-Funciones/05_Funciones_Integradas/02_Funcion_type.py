
"""
Ejemplos prácticos Funcion type()

1. Consultar el tipo de un objeto (1 argumento)
    Es su uso más común. Al pasarle un solo objeto o valor, devuelve la clase/tipo de dato al que pertenece.
"""

print(type(10))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("Hola"))      # <class 'str'>
print(type([1, 2, 3]))   # <class 'list'>
print(type({'a': 1}))    # <class 'dict'>

"""
2. Crear clases de forma dinámica (3 argumentos)
    type() también es la metaclase por defecto en Python. Puedes usarla con 3 argumentos para crear una clase en tiempo de ejecución sin usar la palabra clave class.
    
    Sintaxis:
    type(nombre_de_clase, bases, atributos_y_metodos)
        - nombre_de_clase: Cadena de texto con el nombre de la clase.
        - bases: Tupla con las clases de las cuales hereda (dejar vacía () si no hereda de ninguna).
        - atributos_y_metodos: Diccionario con los atributos y funciones de la clase.

"""
# Crear una clase llamada 'Persona' dinámicamente
Persona = type('Persona', (), {'nombre': 'Carlos', 'edad': 30})

p = Persona()
print(p.nombre)  # Imprime: Carlos
print(type(p))   # Imprime: <class '__main__.Persona'>

