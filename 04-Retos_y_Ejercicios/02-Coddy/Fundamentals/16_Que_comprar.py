"""*****************************************************************************************

Desafío:

Escribe un programa que reciba tres entradas (dadas):
    1. Una lista de precios
    2. Una lista de nombres de artículos
    3. Un presupuesto por artículo

El programa debe imprimir:
    1. Una lista de artículos que puedes costear dentro de tu presupuesto
    2. Cuánto presupuesto necesitarías si compraras todos los artículos asequibles
    3. Cuántos artículos no pudiste costear

*******************************************************************************************"""
prices = input("Ingrese costo de productos separado por comas\n→\t").split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input("Ingrese nombre de productos separado por comas\n→\t").split(",")
budget_per_item = int(input("Ingrese presupuesto con el que cuenta\n→\t"))

affordable_items = []
cant_afford = 0
total_needed = 0


# Escribe tu código debajo
for i in range(len(prices)):
    if prices[i] <= budget_per_item:
        affordable_items.append(items[i])
        total_needed += prices[i]

cant_afford = len(items) - len(affordable_items)

print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)
