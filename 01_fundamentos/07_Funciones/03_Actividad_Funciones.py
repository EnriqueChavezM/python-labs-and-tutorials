"""
Caso:
    Conversor de monedas 
    Programa que permita calcular el valor de dólares o euros a: 
        - Pesos colombianos
        - Yuanes  
        - Libras esterlinas. 
    
    Tablas de equivalencias de monedas:
    - 1 dólar = 3750 pesos colombianos
    - 1 dólar = 6.37 yuanes
    - 1 dólar = 0.76 libras esterlinas

    - 1 euro = 4000 pesos colombianos
    - 1 euro = 6.93 yuanes
    - 1 euro = 0.83 libras esterlinas

    La función principal tendrá como parámetros:
        - El nombre de la moneda actual
        - El valor de la moneda actual
        - El nombre de la moneda a convertir
        dentro de la función principal estarán dos subfunciones dolarTo() y euroTo(), 
            las cuales se encargarán de ejecutar las condiciones que permitirán obtener 
            el valor equivalente a la moneda actual.
        
    Ecuaciones de conversión:
        Equivalencia = Moneda_actual * Valor_equivalente
"""
#Mensaje de bienvenida al usuario
print("Bienvenido al conversor de monedas 🌐💱 \n")

#Funcion principal de conversión de monedas
def convertir_monedas(moneda_actual, valor_actual, moneda_a_convertir):

    #Mensaje de respuesta al usuario
    print(f"\nObteniendo equivalencias de la moneda actual ...")
    print(f"Calculando equivalencias ...")

    #Subfuncion para convertir de dólares a otras monedas
    def dolarTo():
        if moneda_a_convertir == "1":
            print("\nEl valor de la equivalencia es...")
            print(f"${valor_actual} dólares equivalen a ${valor_actual * 3750} pesos colombianos")

        elif moneda_a_convertir == "2":
            print("\nEl valor de la equivalencia es...")
            print(f"${valor_actual} dólares equivalen a ¥{valor_actual * 6.37} yuanes")

        elif moneda_a_convertir == "3":
            print("\nEl valor de la equivalencia es...")
            print(f"${valor_actual} dólares equivalen a £{valor_actual * 0.76} libras esterlinas")

        else:
            print("\nMoneda no válida")

    #Subfuncion para convertir de euros a otras monedas
    def euroTo():
        if moneda_a_convertir == "1":
            print("\nEl valor de la equivalencia es...")
            print(f"€{valor_actual} euros equivalen a ${valor_actual * 4000} pesos colombianos")

        elif moneda_a_convertir == "2":
            print("\nEl valor de la equivalencia es...")
            print(f"€{valor_actual} euros equivalen a ¥{valor_actual * 6.93} yuanes")

        elif moneda_a_convertir == "3":
            print("\nEl valor de la equivalencia es...")
            print(f"€{valor_actual} euros equivalen a £{valor_actual * 0.83} libras esterlinas")

        else:
            print("\nMoneda no válida")

    #Condiciones para determinar la conversión según la moneda actual
    if moneda_actual == "1":
        resultado = dolarTo()

    elif moneda_actual == "2":
        resultado = euroTo()
        
    else:
        print("\nMoneda actual no válida")

# Solicitar al usuario la moneda actual, el valor y la moneda a convertir
moneda_actual = input("Ingrese la moneda actual 💰: \n1 para dólares \n2 para euros \n→ ")
valor_actual = float(input("Ingrese el valor de la moneda actual 🪙: \n→ "))
moneda_a_convertir = input("Ingrese la moneda a convertir 💱:\n1 para pesos colombianos \n2 para yuanes \n3 para libras esterlinas \n→ ")

# Llamar a la función principal con los valores ingresados por el usuario
convertir_monedas(moneda_actual, valor_actual, moneda_a_convertir)

"""
Resultado:
¿Cuánto equivale 50 dólares en pesos colombianos? 
    $50.0 dólares equivalen a $187500.0 pesos colombianos

¿Cuánto equivale 30 euros en yuanes?
    €30.0 euros equivalen a ¥207.89999999999998 yuanes

¿Cuánto equivale 15 euros en libras esterlinas?
    €15.0 euros equivalen a £12.45 libras esterlinas
"""