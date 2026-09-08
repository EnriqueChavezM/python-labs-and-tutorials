"""
Importar módulo completo

import math

# Usamos la función sqrt (raíz cuadrada) del módulo math
resultado = math.sqrt(25)
print(resultado)  # Imprime: 5.0
"""

"""
Importar funcion específica

from math import sqrt, pi

# Las usas directamente sin poner "math." adelante
print(sqrt(16))  # Imprime: 4.0
print(pi)        # Imprime: 3.141592653589793
"""

"""
Importar con un apodo/alias
"""
import datetime as dt

# Usamos el alias "dt" en lugar de "datetime"
hoy = dt.date.today()
print(hoy)