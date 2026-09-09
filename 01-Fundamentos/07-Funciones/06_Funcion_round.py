"""
Ejemplos prácticos
    1. Sin especificar decimales (redondeo a entero)
"""
print(round(3.7))   # Muestra: 4
print(round(3.2))   # Muestra: 3
print(round(2.5))  # Muestra: 2 (2 es el par más cercano)
print(round(3.5))  # Muestra: 4 (4 es el par más cercano)
print(round(-8.95)) # Muestra: -9

"""
    2. Especificando posiciones decimales
"""
pi = 3.14159

print(round(pi, 2))  # Muestra: 3.14
print(round(pi, 3))  # Muestra: 3.142