# 1. Importar el módulo completo
import Paquete.operaciones
import Paquete.texto

# Usar funciones y variables del módulo usando la sintaxis: modulo.funcion()
print(Paquete.texto.MENSAJE)
nombre = input("Ingrese su nombre: ")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

txt = Paquete.texto.mayusculas(nombre)
resultado_suma = Paquete.operaciones.sumar(a, b)
print(f"La suma es: {resultado_suma}")


# 2. Oportunidad alternativa: Importar solo lo que necesitas
from Paquete.operaciones import restar
from Paquete.texto import saludar

print(saludar(txt))
print(f"La resta es: {restar(a, b)}")


# 3. Oportunidad alternativa: Usar un alias corto
import Paquete.operaciones as op

print(f"Suma con alias: {op.sumar(resultado_suma, a)}")