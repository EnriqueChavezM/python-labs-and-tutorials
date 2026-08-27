# Archivo: operaciones.py

# 1. Importar el módulo completo
import operaciones

# Usar funciones y variables del módulo usando la sintaxis: modulo.funcion()
print(operaciones.MENSAJE_BIENVENIDA)

resultado_suma = operaciones.sumar(10, 5)
print(f"La suma es: {resultado_suma}")


# 2. Oportunidad alternativa: Importar solo lo que necesitas
from operaciones import restar, saludar

print(saludar("Carlos"))
print(f"La resta es: {restar(20, 8)}")


# 3. Oportunidad alternativa: Usar un alias corto
import operaciones as op

print(f"Suma con alias: {op.sumar(100, 200)}")