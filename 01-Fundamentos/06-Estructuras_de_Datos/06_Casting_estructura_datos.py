"""******************************************************************************************

Ejemplo 1:

1. Convierte los siguientes datos en listas utilizando la función list():
    1.1. Una tupla: (10, 20, 30)
    1.2. Una cadena: "python"
    1.3. Un rango: range(1, 6)
2. Imprime las listas resultantes.

*******************************************************************************************"""
# Datos
mi_tupla = (10, 20, 30) # Tupla
cadena = "python"       # Cadena
rango = range(1,6)      # Rango

# Casting a lista
print(list(mi_tupla))   # Imprime [10, 20, 30]
print(list(cadena))     # Imprime ['p', 'y', 't', 'h', 'o', 'n']
print(list(rango))      # Imprime [1, 2, 3, 4, 5]
