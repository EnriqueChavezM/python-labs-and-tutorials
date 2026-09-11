"""****************************************************************************************

Crea un programa que ayude a rastrear las recompensas por fidelidad de una empresa de mudanzas.
Lee la entrada en este orden, un valor por línea:
    → Importe total de la compra (un número decimal)
    → Índice inicial (un número entero, basado en 0)
    → Número de cajas n (un número entero)
    → N etiquetas de cajas, una por línea (una etiqueta puede contener espacios)
    → Calcula los puntos de fidelidad: 
        → 1 punto por cada $10 gastados, redondeando hacia abajo.

Imprime los puntos de fidelidad en la primera línea y luego imprime cada etiqueta de caja desde el índice inicial hasta el final de la lista, cada una en una línea diferente.

****************************************************************************************"""

# Leer el importe total de la compra
purchase_amount = float(input("Ingrese inporte: "))

# TODO: Calcular los puntos de fidelidad (1 punto por cada 10 $ gastados, redondeado hacia abajo)
points = 0
points = int(purchase_amount // 10)

# Leer el índice de inicio
start_index = int(input("Ingrese Indice inicio: "))

# Leer el número de cajas y luego las etiquetas de las cajas (una por línea)
n = int(input("Ingrese numero de cajas: "))
boxes = []

# TODO: Leer n etiquetas con input() y añadir cada una a las cajas
for box in range(n):
    etiqueta = input("Ingrese etiqueta " + str(box + 1) + ": ")
    boxes.append(etiqueta)

# TODO: Imprimir los puntos de fidelidad en la primera línea
print(f"Puntos de fidelidad obtenidos: {points}")
# TODO: Imprimir todas las cajas desde el índice de inicio hasta el final, una por línea
x = boxes[start_index:]
for i in x:
    print(i)