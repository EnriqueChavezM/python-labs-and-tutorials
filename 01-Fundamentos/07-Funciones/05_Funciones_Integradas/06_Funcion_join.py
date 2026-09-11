"""
Ejemplos prácticos
1. Unir una lista de palabras con espacios
"""
print("\nEJEMPLO 1 Unir una lista de palabras con espacios\n")
palabras = ["Hola", "mundo", "desde", "Python"]

# Usamos un espacio " " como separador
resultado = " ".join(palabras)
print(f"Lista original: {palabras}")
print(f"Resultado: {resultado}")  # Muestra: Hola mundo desde Python

"""
2. Crear formatos de datos (CSV) o guiones
"""
print("\nEJEMPLO 2 Crear formatos de datos (CSV) o guiones\n")
datos = ["Juan", "25", "México", "Desarrollador"]

# Usamos coma y espacio ", " como separador
linea_csv = ", ".join(datos)
print(f"Lista original: {datos}")
print(f"Línea CSV: {linea_csv}")  # Muestra: Juan, 25, México, Desarrollador

# Usamos un guion "-"
codigo = "-".join(["4000", "A12", "99"])
print(f"\nLista original: {['4000', 'A12', '99']}")
print(f"Código: {codigo}")     # Muestra: 4000-A12-99

"""
3. Formatear listas de líneas de texto (saltos de línea)
"""
print("\nEJEMPLO 3 Formatear listas de líneas de texto (saltos de línea)\n")
pasos = [
    "1. Cargar archivo",
    "2. Procesar datos",
    "3. Guardar resultados"
]

# Usamos el salto de línea '\n' para unir la lista
reporte = "\n".join(pasos)
print(f"Lista original: {pasos}")
print(f"Reporte:\n{reporte}")
# Salida:
# 1. Cargar archivo
# 2. Procesar datos
# 3. Guardar resultados