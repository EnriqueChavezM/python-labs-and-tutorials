""""
Dada una lista de numeros separados por comas, imprimir una lista de índices de los números que cumplan cualquiera de estas condiciones:
    - El número es menor que 50
    - el numero es diviible por 5

"""
lista = list(map(int, input("Ingrese una lista de números separados por comas: ").split(",")))
lista_indices = []
for indice, numero in enumerate(lista):
    if numero < 50 or numero % 5 == 0:
        lista_indices.append(indice)
print("Los índices de los números que cumplen las condiciones son:", lista_indices)