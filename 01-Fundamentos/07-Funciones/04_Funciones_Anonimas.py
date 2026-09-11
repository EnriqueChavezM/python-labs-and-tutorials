"""******************************************************

Comparación: Función normal vs Función lambda
Para entenderlo mejor, mira cómo se escribe una misma operación de dos formas distintas:

******************************************************"""
# 1. Función tradicional con 'def'
def duplicar(x):
    return x * 2

# 2. Equivalente en una función 'lambda'
duplicar_lambda = lambda x: x * 2

print(f"Función normal: {duplicar(5)}")        # Muestra: 10
print(f"Función lambda: {duplicar_lambda(5)}") # Muestra: 10

"""*******************************************************

Ejemplo 1: Calcular un impuesto o porcentaje rápidamente
Imagina que estás automatizando el cálculo de costos para una lista de precios y necesitas aplicar un descuento del 10% a todos los productos.

*******************************************************"""

print("\nEJEMPLO 1. Aplicando un descuento del 10%\n")
# Definimos la función lambda para calcular el precio con 10% de descuento
aplicar_descuento = lambda precio: precio * 0.90

# La usamos directamente
precio_original = 100
precio_final = aplicar_descuento(precio_original)
print(f"Precio original: ${precio_original}")
print(f"Precio con descuento: ${precio_final}")  # Muestra: 90.0

"""*******************************************************

Ejemplo 2: Limpiar espacios en una lista de textos
Cuando extraes datos de archivos o de internet, a menudo te quedan textos con espacios de más al inicio o al final.
Puedes combinar map() con un lambda para limpiar una lista completa en una sola línea

*******************************************************"""

print("\nEJEMPLO 2. Limpiar espacios en una lista de textos\n")
nuestras_rutas = ["  /var/log/ ", "/home/user/ ", " /var/www/html "]

# Aplicamos .strip() a cada elemento usando lambda
rutas_limpias = list(map(lambda ruta: ruta.strip(), nuestras_rutas))

print(f"Lista original: {nuestras_rutas}")
print(f"Lista limpia: {rutas_limpias}") # Muestra: ['/var/log/', '/home/user/', '/var/www/html']

"""*******************************************************

Ejemplo 3: Filtrar datos de forma rápida
Supongamos que tienes una lista con los tiempos de respuesta (en milisegundos) de un servidor y solo quieres conservar los valores que superan los 100 ms para registrar una alerta. 
Puedes usar filter() junto con un lambda:

*******************************************************"""

print("\nEJEMPLO 3. Filtrar tiempos de respuesta mayores a 100 ms\n")
tiempos_respuesta = [45, 120, 80, 250, 95, 310]

# Filtramos solo los tiempos mayores a 100 ms
alertas_lentas = list(filter(lambda t: t > 100, tiempos_respuesta))

print(f"Tiempos de respuesta: {tiempos_respuesta}")
print(f"Alertas lentas: {alertas_lentas}")