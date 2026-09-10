"""
Crear un programa que reciba una lista como entrada, e imprima una nueva lista que contenga solo las palabras mas largas que 5 caracteres
"""
lista = input("ingrese una lista de palabras separadas por comas: ").split(",")
nueva_lista = [palabra for palabra in lista if len(palabra) > 5]
print("Las palabras con más de 5 caracteres son:", nueva_lista)
