#Uso de Tuplas #
print("Uso de tuplas")
coordenadas = (10.0, 20.0)
print("Tupla Coordenadas:", coordenadas)  # Imprime (10.0, 20.0)
print("\nAcceso a elementos de la tupla:")
print("Coordenada X:", coordenadas[0])  # Imprime 10.0
print("Coordenada Y:", coordenadas[1])  # Imprime 20.0

#Uso de metodos de tuplas #
print("\nUso de metodos de tuplas")
punto = (1, 2, 3, 2, 4, 2)
print("Tupla punto:", punto)  # Imprime (1, 2, 3, 2, 4, 2)
print("Número de veces que aparece el número 2:\n", punto.count(2))  # Imprime 3
print("Índice de la primera aparición del número 2:\n", punto.index(2))  # Imprime 2
print("Índice de la primera aparición del número 2 apartir de la pocicion 2:\n", punto.index(2, 2))  # Imprime 1
print("Índice de la primera aparición del número 2apartir de la pocicion 2 hasta la posicion 5:\n", punto.index(2, 1, 5))  # Imprime 3
print("Longitud de la tupla:\n", len(punto))  # Imprime 6

