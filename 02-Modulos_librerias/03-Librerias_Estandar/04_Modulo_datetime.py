"""
Ejemplos prácticos
    1. Obtener la fecha y hora actual

from datetime import datetime, date

# Fecha y hora exacta actual
ahora = datetime.now()
print(f"Fecha y hora actual: {ahora}")

# Obtener componentes individuales
print(f"Año: {ahora.year}, Mes: {ahora.month}, Día: {ahora.day}")
print(f"Hora: {ahora.hour}, Minutos: {ahora.minute}")

# Solo la fecha actual (sin hora)
hoy = date.today()
print(f"Solo la fecha: {hoy}")
"""

"""
    Formatear fechas como texto (strftime) y viceversa (strptime)
    - strftime (String Format Time): Convierte una fecha a un formato de texto legible.
    - strptime (String Parse Time): Convierte un texto a un objeto de fecha.


from datetime import datetime

ahora = datetime.now()

# 1. De Fecha a Texto (strftime)
# %d = día, %m = mes, %Y = año (4 dígitos), %H = hora, %M = minuto
fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M")
print(f"Fecha legible: {fecha_formateada}")

# 2. De Texto a Fecha (strptime)
texto_fecha = "25/12/2026"
fecha_objeto = datetime.strptime(texto_fecha, "%d/%m/%Y")
print(f"Objeto datetime creado: {fecha_objeto}")
"""

"""
    3. Sumar/Restar días y calcular diferencias (timedelta)
"""
from datetime import date, timedelta

hoy = date.today()

# Sumar 10 días a la fecha actual
futuro = hoy + timedelta(days=10)
print(f"En 10 días será: {futuro}")

# Calcular cuántos días faltan para un evento
fin_de_ano = date(2026, 12, 31)
dias_faltantes = fin_de_ano - hoy
print(f"Faltan {dias_faltantes.days} días para fin de año.")