"""******************************************************************************************

Desafío 1:

Escribe un programa que reciba dos entradas independientes del usuario y muestre el resultado redondeado:
    1. La primera entrada debe ser un número (flotante). 
    2. La segunda entrada debe ser el número de posiciones decimales al que se debe redondear (entero).

Ejemplo:
    Si las entradas son 3.14159 y 2, el programa debería mostrar 3.14.

*******************************************************************************************"""
"""# Toma una entrada float del usuario
numero = float(input("Ingrese un numero con punto decimal:\n→\t"))

# Toma una entrada entera del usuario para el número de decimales
redondeo = int(input("Ingrese a  cuantos decimales desea redondear el  numero:\n→\t"))

# Imprime el número redondeado
print(round(numero,redondeo)) """

"""******************************************************************************************

Desafío 2:

Crea una función llamada "calculate_discount" que acepte dos parámetros:
    1. "price": El precio original de un artículo (float)
    2. "discount_percentage": El porcentaje de descuento (float)

La función debe:
    1. Calcular el importe del descuento
    2. Restar el importe del descuento del precio original
    3. Redondear el resultado a 2 decimales
    4. return el precio final con descuento

Por ejemplo:
    Si el precio original es de $100 y el descuento es del 20%, la función debe devolver $80.00.


*******************************************************************************************"""
# Funcion calculo de descuento
def calculate_discount(price, discount_percentage):
    
    monto_final = price - ((discount_percentage * price) / 100 )
    return round(monto_final, 2)

# Entrada de usuario
precio =  float(input("Ingrese precio del articulo:\n→ "))
descuento = float(input("Ingrese porsentaje del descuento:\n→ "))

# Llamar funcion e imprimir resultado
print(f"Precio con descuento:\n→ ${calculate_discount(precio, descuento)}")
