"""
Imagina que tienes un archivo llamado notas.txt con este contenido:
    Comprar leche
    Estudiar Python
    Hacer ejercicio
"""
# Abrimos el archivo en modo lectura
with open("notas.txt", "r", encoding="utf-8") as archivo:
    # Recorremos cada línea directamente con un ciclo for
    for linea in archivo:
        # strip() remueve el salto de línea sobrante al final
        print(linea.strip())