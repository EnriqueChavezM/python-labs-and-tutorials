#uso de diccionarios #
print("Uso de diccionarios")
persona = {
    "nombre", "Juan",
    "edad", 30,
    "ciudad", "Madrid"
}
print("Diccionario persona:", persona)  # Imprime {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}   
print("Acceso a valores del diccionario:")
print("Nombre:", persona["nombre"])  # Imprime "Juan"
print("Edad:", persona["edad"])  # Imprime 30
print("Ciudad:", persona["ciudad"])  # Imprime "Madrid"

#Uso de metodos de diccionarios #
print("\nUso de métodos de diccionarios")
persona = {
    "nombre", "Juan",
    "edad", 30,
    "ciudad", "Madrid"
}
print("Diccionario persona:", persona)  # Imprime {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
print(persona.keys())  # Imprime dict_keys(['nombre', 'edad', 'ciudad'])
print(persona.values())  # Imprime dict_values(['Juan', 30, 'Madrid'])
print(persona.items())  # Imprime dict_items([('nombre', 'Juan'), ('edad', 30), ('ciudad', 'Madrid')])
persona.update({"profesion": "Ingeniero"})
print("Diccionario persona actualizado:", persona)  # Imprime {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}
