"""
Ejemplo practico
    La forma estándar de aplicar encapsulamiento es marcar el atributo como privado (__atributo)
        y proporcionar métodos Getter (para leer) y Setter (para validar y modificar).

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular          # Atributo público
        self.__saldo = saldo_inicial    # Atributo privado

    # Getter: Permite leer el valor privado
    def obtener_saldo(self):
        return self.__saldo

    # Setter: Permite modificar el valor previo control/validación
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a 0.")


# --- Uso de la clase ---
cuenta = CuentaBancaria("Ana", 1000)

# 1. Intentar acceder directamente al atributo privado (Dará error)
# print(cuenta.__saldo)  
# -> AttributeError: 'CuentaBancaria' object has no attribute '__saldo'

# 2. Leer mediante el método Getter
print(cuenta.obtener_saldo())  # Imprime: 1000

# 3. Modificar mediante el método Setter
cuenta.depositar(500)  # Imprime: Depósito exitoso. Nuevo saldo: $1500

"""

"""
Ejemplo 2 (Decorador @property)
    En Python se prefiere usar el decorador @property en lugar de crear métodos como obtener_saldo() o depositar(). 
    Esto permite acceder a los atributos como si fueran públicos, pero manteniendo las validaciones internas.
"""
class Persona:
    def __init__(self, edad):
        self.__edad = edad

    # Getter con @property
    @property
    def edad(self):
        return self.__edad

    # Setter con @edad.setter
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("Error: La edad no puede ser negativa.")

# Uso:
p = Persona(25)
print(p.edad)      # Se lee como una variable normal -> Imprime: 25
p.edad = 30        # Se asigna como variable normal -> Cambia el valor
p.edad = -5        # Pasa por la validación -> Imprime error