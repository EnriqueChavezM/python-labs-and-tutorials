"""
Ejemplo 1: Crear o sobrescribir un archivo ("w")

# Abre el archivo (si existe, borra su contenido anterior)
with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Lista de tareas:\n")
    archivo.write("1. Aprender lectura de archivos\n")
    archivo.write("2. Aprender escritura de archivos\n")
"""

"""
Ejemplo 2: Añadir nuevas líneas sin borrar lo anterior ("a")
 
# Agrega una nueva línea al final del archivo existente
with open("notas.txt", "a", encoding="utf-8") as archivo:
    archivo.write("3. Practicar ejercicios en Python\n")
"""

"""
Ejemplo 3: Escribir varias líneas de golpe con writelines()
"""
lineas = [
    "Lista de Compras.\n"
    "\tComprar café\n",
    "\tRevisar correo\n",
    "\tHacer ejercicio\n"
]

with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas)