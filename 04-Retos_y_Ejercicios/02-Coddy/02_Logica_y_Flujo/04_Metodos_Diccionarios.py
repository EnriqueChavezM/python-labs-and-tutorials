"""******************************************************************************************

Desafío 1:

1. Crea un diccionario llamado "grades" con estos pares clave-valor iniciales:
    - "Alice": 85
    - "Bob": 90
    - "Charlie": 78
2. Imprime todos los nombres y las calificaciones de los estudiantes usando exactamente estas instrucciones:
    - print("Students:", grades.keys())
    - print("Grades:", grades.values())
3. Añade un nuevo estudiante, "Diana", con una calificación de 92.
4. Usa el método "get()" para obtener la calificación de Bob, guárdala en una variable llamada" bobs_grade" e imprímela usando:
    - print("Bob's grade:", bobs_grade)
5. Elimina a "Charlie" del diccionario usando el método pop() y después imprime el diccionario actualizado usando:
    - print("Updated grades:", grades)

Importante: 
    Sigue la secuencia exacta y usa exactamente las instrucciones de impresión que se muestran arriba para obtener el resultado esperado.

Resultado esperado:
    Students: dict_keys(['Alice', 'Bob', 'Charlie'])
    Grades: dict_values([85, 90, 78])
    Bob's grade: 90
    Updated grades: {'Alice': 85, 'Bob': 90, 'Diana': 92}

*******************************************************************************************"""
# Paso 1: Crear el diccionario de calificaciones
grades = {
    # Agrega las calificaciones iniciales de los estudiantes aquí
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Paso 2: Acceder a todas las claves y valores
# Imprimir todos los estudiantes y calificaciones
print("Students:", grades.keys())
print("Grades:", grades.values())

# Paso 3: Agregar un nuevo estudiante
# Agregar a Diana con una calificación de 92
grades["Diana"] = 92

# Paso 4: Recuperar la calificación de un estudiante
# Obtener la calificación de Bob usando el método get()
bobs_grade = grades.get("Bob")
print("Bob's grade:", bobs_grade)

# Paso 5: Eliminar a un estudiante
# Eliminar a Charlie usando el método pop()
# Imprimir el diccionario actualizado
grades.pop("Charlie")
print("Updated grades:", grades)