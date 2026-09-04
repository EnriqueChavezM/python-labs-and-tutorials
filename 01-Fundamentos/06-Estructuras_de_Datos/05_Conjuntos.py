#Uso de conjuntos #
print("Uso de conjuntos")
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
print("Conjunto 1:", conjunto1)  # Imprime {1, 2, 3}
print("Conjunto 2:", conjunto2)  # Imprime {3, 4, 5}    

union = conjunto1 | conjunto2
print("operación unión:", union)  # Imprime {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2
print("operación intersección:", interseccion)  # Imprime {3}

diferencia = conjunto1 - conjunto2
print("operación diferencia:", diferencia)  # Imprime {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2
print("operación diferencia simétrica:", diferencia_simetrica)  # Imprime {1, 2, 4, 5}

#uso metodos de conjuntos
print("Uso de métodos de conjuntos")
frutas = {"manzana", "banana", "naranja"}
print("Conjunto original:", frutas)  # Imprime {"manzana", "banana", "naranja"}

frutas.add("pera")
print("Conjunto después de add:", frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas.remove("banana")
print("Conjunto después de remove:", frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.discard("uva")
print("Conjunto después de discard:", frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.pop()
print("Conjunto después de pop:", frutas)   #Elimina un elemento random

resultado = frutas.union(union)
print("Conjunto despues de union:", resultado)
frutas.clear()
print("Conjunto después de clear:", frutas)  # Imprime set()