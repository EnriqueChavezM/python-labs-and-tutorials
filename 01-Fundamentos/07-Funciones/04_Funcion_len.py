"""
Ejemplos prácticos Funcion len()

1. Con cadenas de texto (str)
    Cuenta cuántos caracteres tiene una cadena (incluyendo espacios, símbolos y acentos).
"""

texto = "Python"
print(len(texto))  # Muestra: 6

mensaje = "Hola mundo"
print(len(mensaje))  # Muestra: 10 (incluye el espacio)

"""
2. Con colecciones (listas, tuplas, conjuntos, diccionarios)
    Devuelve el número de elementos contenidos dentro de la estructura de datos.
"""

# Lista de elementos
frutas = ["manzana", "banana", "cereza"]
print(len(frutas))  # Muestra: 3

# Diccionario (cuenta la cantidad de claves)
usuario = {"nombre": "Carlos", "edad": 25, "ciudad": "Madrid"}
print(len(usuario))  # Muestra: 3
