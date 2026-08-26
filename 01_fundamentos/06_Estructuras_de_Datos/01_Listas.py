
frutas = ["manzana", "banana", "naranja"]
print("lista original: ", frutas)  # Imprime ["manzana", "banana", "naranja"]

print("\nAcceso a la lista por indices")
print(f"Indice 0: {frutas[0]}")
print(f"Indice 2: {frutas[2]}")

print("\nAcceso a la lista por indices negativos")
print(f"Indice -1: {frutas[-1]}")
print(f"Indice -2: {frutas[-2]}")

print("\nUso de metodos de listas")
frutas.append("pera")
print("Metodo append: ",frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]

frutas.insert(1, "uva")
print("Metodo insert: ",frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

indice = frutas.index("banana")
print("Indice de banana en la lista: " + str(indice))

frutas.remove("banana")
print("Metodo remove: ",frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

fruta_eliminada = frutas.pop(2)
print("Lista despues de : ",frutas)  # Imprime ["manzana", "uva", "pera"]
print("Eliminada por pop: ",fruta_eliminada)  # Imprime "naranja"

fruta_eliminada = frutas[0]
print("Eliminada por del : ",fruta_eliminada)  # Imprime "naranja"
del frutas[0]
print("Lista despues de del: ",frutas)  # Imprime ["manzana", "uva", "pera"]

frutas.sort()
print("Metodo sort: ",frutas)  # Imprime ["manzana", "pera", "uva"]

frutas.reverse()
print("Metodo reverse: ",frutas)  # Imprime ["uva", "pera", "manzana"]


Contarb = frutas.count("pera")
print("Numero de veces que aparece pera en la lista: " + str(Contarb))

frutas.clear()
print("Esta es la lista despues del  metodo clear:" + str(frutas))

#Uso de listas por comprensión #
print("\nuso de listas por comprensión")
print("Cuadrados de los números del 1 al 5:")
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros if x % 2 == 0]  # Crea una nueva lista con los cuadrados de los números pares
print("cuadrados de los números impares:", cuadrados)  # Imprime [4, 16]
