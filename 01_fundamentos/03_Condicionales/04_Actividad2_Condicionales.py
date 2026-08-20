"""
Criterio para descuento
        comra(USD)          porcentaje
          comrpa <  80           0%
    80 <= compra <  150         10%
    150<= compra <= 300         15%
    300 < compra <  500         20%
          compra >= 500         25%

valores de entrada 
    - Nombre del cliente
    - valor de la compra sin descuento

Resultado de salida
    - Nombre del cliente
    - Valor de la compra sin descuento
    - Valor de la compra con descuento

Calculos 
    descuento = valor_compra * porcentaje
    precio_final = valor_compra - descuento

Interrogantes
    Angel Mario Villa Lopez realizó una compra de 455 usd.
    Rosa Diaz realizó una compra de 105 usd.
    Dilan Gonzalez realizó una compra de 250 usd.
    Kell Daza realizó una compra de 430 usd.

Respuesta
    Angel Mario Villa Lopez realizó una compra de 455 usd.
        Hola, Angel Mario Villa Lopez. El valor a pagar es: $450.0
        Compra sin descuento: 450.0
        Compra con descuento: 360.0
    Rosa Diaz realizó una compra de 105 usd.
        Hola, Rosa Diaz. El valor a pagar es: $105.0
        Compra sin descuento: 105.0
        Compra con descuento: 94.5
    Dilan Gonzalez realizó una compra de 250 usd.
        Hola, Dilan Gonzalez. El valor a pagar es: $250.0
        Compra sin descuento: 250.0
        Compra con descuento: 212.5
    Kell Daza realizó una compra de 430 usd.
        Hola, Kell Daza. El valor a pagar es: $430.0
        Compra sin descuento: 430.0
        Compra con descuento: 344.0
"""
#Solicitar informacion
nombre = input("Ingrese el nombre del  cliente: ")
valor_compra = float(input("Ingrese el valor de la compra: $"))
pórsentaje = 0

#condiciones de descuento
if valor_compra < 80:
    porsentaje = 0
elif valor_compra < 150:
    porsentaje = 0.1
elif valor_compra <= 300:
    porsentaje = 0.15
elif valor_compra < 500:
    porsentaje = 0.20
else:
    porsentaje = 0.25
     
descuento = valor_compra *  porsentaje
precio_final = valor_compra - descuento
print(f"Hola, {nombre}. El valor a pagar es: ${valor_compra}")
print(f"Compra sin descuento: {valor_compra}") 
print(f"Compra con descuento: {precio_final}")