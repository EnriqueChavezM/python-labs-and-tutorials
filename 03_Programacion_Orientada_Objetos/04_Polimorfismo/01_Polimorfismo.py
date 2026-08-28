"""
Ejemplo 1

# 1. Definición de diferentes clases con el MISMO método
class Gato():
    def sonido(self):
        print("MIAU!!!")

class Perro():
    def sonido(self):
        print("GUAU!!!")

# 2. Función polimórfica (no le importa de qué clase es el objeto, solo que sepa procesar_pago)
def escucharSonido(animal):
    # Llama al método sonido sin importar qué tipo de animal sea
    animal.sonido()

# --- Uso del polimorfismo ---
gato1 = Gato()
perro1 = Perro()

# Pasamos objetos distintos a la misma función:
escucharSonido(gato1)   #Imprime MIAU!!!
escucharSonido(perro1)  #Imprime GUAU!!!
"""

"""
Ejemplo 2
Imagina que estás desarrollando un sistema de pagos. 
Tienes distintas formas de cobro (Tarjeta, PayPal, Efectivo),
y todas saben cómo procesar_pago(), pero cada una lo hace de manera distinta.
"""
# 1. Definición de diferentes clases con el MISMO método

class PagoTarjeta:
    def procesar_pago(self, monto):
        return f"Procesando ${monto} con Tarjeta de Crédito (conectando al banco...)"

class PagoPayPal:
    def procesar_pago(self, monto):
        return f"Procesando ${monto} vía PayPal (enviando token de seguridad...)"

class PagoEfectivo:
    def procesar_pago(self, monto):
        return f"Procesando ${monto} en Efectivo (generando recibo para caja...)"


# 2. Función polimórfica (no le importa de qué clase es el objeto, solo que sepa procesar_pago)

def realizar_cobro(metodo_pago, monto):
    # Llama al método procesar_pago sin importar qué tipo de pago sea
    print(metodo_pago.procesar_pago(monto))


# --- Uso del polimorfismo ---

tarjeta = PagoTarjeta()
paypal = PagoPayPal()
efectivo = PagoEfectivo()

# Pasamos objetos distintos a la misma función:
realizar_cobro(tarjeta, 150)  # Imprime: Procesando $150 con Tarjeta de Crédito (conectando al banco...)

realizar_cobro(paypal, 80)    # Imprime: Procesando $80 vía PayPal (enviando token de seguridad...)

realizar_cobro(efectivo, 25)  # Imprime: Procesando $25 en Efectivo (generando recibo para caja...)