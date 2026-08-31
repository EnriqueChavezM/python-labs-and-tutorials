# =====================================================================
# PROGRAMA: CAFETERÍA AUTOMATIZADA PythonCafé
# =====================================================================

# 1. USO DE TRUCOS VISUALES EN PRINT (Multiplicación de texto y comillas triples)
print("=" * 45)
print("""
  ¡BIENVENIDO A PYTHON-CAFÉ!
  Elige tus productos y personaliza tu orden.
""")
print("=" * 45)
print() # Print vacío para dejar una línea de espacio

# 2. INPUT BÁSICO + LIMPIEZA DE TEXTO (.strip y .title)
# Borra espacios accidentales y pone la primera letra en mayúscula
nombre_cliente = input("¿A nombre de quién dejamos la orden?: ").strip().title()

# 3. PRINT CON F-STRING (La forma moderna y recomendada)
print(f"\n¡Perfecto, {nombre_cliente}! Vamos a configurar tu café.")

# 4. INPUT CON CONVERSIÓN DE TIPO (int) + VALIDACIÓN AVANZADA (try/except)
# Evita que el programa se rompa si el usuario no escribe un número
while True:
    try:
        cantidad_cafes = int(input("¿Cuántos cafés vas a llevar? (Escribe el número): "))
        if cantidad_cafes > 0:
            break
        print("❌ Por favor, pide al menos 1 café.")
    except ValueError:
        print("❌ Error: Debes ingresar un número entero válido.")

# 5. INPUT CON CONVERSIÓN DE TIPO (float)
precio_base = float(input("¿De qué precio es el café que elegiste? (Ej: 3.50): "))

# 6. INPUT MÚLTIPLE EN UNA SOLA LÍNEA (.split)
# El usuario debe escribir dos ingredientes separados por un espacio (Ej: Canela Vainilla)
print("\nEscribe dos extras para tu café (Ej: Canela Chispas):")
extra1, extra2 = input("Extras: ").split()

# 7. PARÁMETROS OCULTOS DE PRINT (sep y end)
# Usamos 'end' para que el texto no salte de línea y simule una carga
print("Procesando tu pedido", end="... ")
print("¡Orden lista!")

# --- CÁLCULOS ---
subtotal = cantidad_cafes * precio_base
impuesto = subtotal * 0.16
total = subtotal + impuesto

# 8. PRINT CON FORMATO AVANZADO (Control de decimales :.2f y métodos de texto)
print("\n" + "#" * 15 + " RESUMEN DE COMPRA " + "#" * 15)

# Formateo de decimales y uso de .upper() dentro del f-string
print(f"Cliente: {nombre_cliente.upper()}")
print(f"Detalle: {cantidad_cafes} cafés con {extra1} y {extra2}.")
print(f"Subtotal: ${subtotal:.2f}")

# 9. PRINT TRADICIONAL CON COMAS (Añade espacio automáticamente)
print("Impuestos (16%):", "$", impuesto)

print("-" * 49)
# 10. PRINT CON CONCATENACIÓN (+)
# Ojo: Obligatorio transformar los números a texto con str() para que no dé error
print("TOTAL A PAGAR: $" + str(total))
print("-" * 49)

# 11. INPUT VACÍO (Para pausar el programa antes de cerrar)
input("\nPresiona ENTER para finalizar el pago y salir...")
print("¡Gracias por tu compra! Vuelve pronto.")
