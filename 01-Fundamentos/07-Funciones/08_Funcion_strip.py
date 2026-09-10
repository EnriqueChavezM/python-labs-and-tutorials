"""
Ejemplos prácticos
    1. Limpieza de espacios en blanco por defecto
    Nota:
        .strip() solo elimina los caracteres de los extremos. Los espacios que están en el centro del texto (entre las palabras) no se modifican.
"""
print("\nEJEMPLO 1 Limpieza de espacios en blanco por defecto\n")
texto = "   Hola Mundo \n"

# Elimina los espacios antes de 'Hola' y el salto de línea al final
texto_limpio = texto.strip()

print(f"Original: '{texto}'")
print(f"Limpio:   '{texto_limpio}'")

# Salida:
# Original: '   Hola Mundo 
# '
# Limpio:   'Hola Mundo'

"""
EJEMPLO 2 Limpieza de caracteres específicos
Si le pasas un argumento a .strip(), eliminará cualquier combinación de esos caracteres que se encuentre en los extremos:
"""
print("\nEJEMPLO 2 Limpieza de caracteres específicos\n")
url = "https://www.ejemplo.com/"
print(f"Original: '{url}'")
# Elimina 'https://' y la barra '/' al final
url_limpia = url.strip("htps:/")

print(f"Limpia:   '{url_limpia}'")  # Muestra: www.ejemplo.com

"""
EJEMPLO 3 Divide una cadena en una lista: 
"""
print("\nEJEMPLO 3 Divide una cadena en una lista:\n")
text = "apple banana cherry"
fruits = text.split()  # Split by whitespace
print(f"Cadena original: '{text}'")
print(f"Lista resultante: {fruits}")  # ['apple', 'banana', 'cherry']

data = "john,25,new york"
info = data.split(',')  # Split by comma
print(f"\nCadena original: '{data}'")
print(f"Lista resultante: {info}")  # ['john', '25', 'new york']