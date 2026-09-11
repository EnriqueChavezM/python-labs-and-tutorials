"""****************************************************************************************

                    Ejemplos prácticos

1. Filtrar números pares de una lista
Supongamos que tienes una lista de números y quieres conservar únicamente los pares:

****************************************************************************************"""
print("EJEMPLO 1. Filtrar números pares de una lista\n")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usamos una función lambda para verificar si el número es divisible por 2
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(f"Números originales: {numeros}")
print(f"Números pares: {pares}")  # Muestra: [2, 4, 6, 8, 10]

"""****************************************************************************************

2. Filtrar registros vacíos o nulos en automatización
Cuando procesas datos o líneas leídas de archivos de texto (logs o CSV), a menudo te encuentras con cadenas vacías causadas por saltos de línea. 

****************************************************************************************"""
print("\nEJEMPLO 2. Filtrar registros vacíos o nulos\n")

lineas_registro = ["Error 404", "", "Proceso completado", "   ", "Advertencia de red"]

# Filtramos cadenas que no estén vacías (pasando None como función elimina valores 'falsy' como "" o 0)
# O bien usando una lambda para limpiar espacios:
lineas_validas = list(filter(lambda linea: linea.strip() != "", lineas_registro))

print(f"Registros originales: {lineas_registro}")
print(f"Registros válidos: {lineas_validas}")  # Muestra: ['Error 404', 'Proceso completado', 'Advertencia de red']