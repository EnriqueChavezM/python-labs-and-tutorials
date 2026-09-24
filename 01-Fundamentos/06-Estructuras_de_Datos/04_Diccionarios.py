#uso de diccionarios #
print("Uso de diccionarios")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print("Diccionario persona:", persona)  # Imprime {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}   
print("Acceso a valores del diccionario:")
print("Nombre:", persona["nombre"])  # Imprime "Juan"
print("Edad:", persona["edad"])  # Imprime 30
print("Ciudad:", persona["ciudad"])  # Imprime "Madrid"

#Uso de métodos de diccionarios #
print("\nUso de métodos de diccionarios")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print("Diccionario persona:", persona)  # Imprime {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
print(persona.keys())  # Imprime dict_keys(['nombre', 'edad', 'ciudad'])
print(persona.values())  # Imprime dict_values(['Juan', 30, 'Madrid'])
print(persona.items())  # Imprime dict_items([('nombre', 'Juan'), ('edad', 30), ('ciudad', 'Madrid')])
persona.update({"profesión": "Ingeniero"})
print("Diccionario persona actualizado:", persona)  # Imprime {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid', 'profesión': 'Ingeniero'}
print("Valor a eliminar con del: "+ persona["ciudad"])
del persona ["ciudad"]

print("Diccionario persona actualizado:", persona)  # Imprime {'nombre': 'Juan', 'edad': 30, 'profesión': 'Ingeniero'}

# Uso de Diccionarios Anidados
print("\nUso de Diccionarios Anidados")
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"}
}
print(f"Diccionario original: {students}")
# acceder a valor necesario
print(f"Edad de Alice: {students["Alice"]["age"]}")  # Salida: 20
print(f"Grado de Bob: {students["Bob"]["grade"]}")  # Salida: 20

# agregar un nuevo par key-valor al diccionario interno
students["Alice"]["Materia"] = "Matemáticas"
print(f"Nuevo valor de Materia en Diccionario de Alice {students["Alice"]["Materia"]}")  # Salida: {'age': 20, 'grade': 'A', 'major': 'Math'}
print(f"Diccionario final: {students}")