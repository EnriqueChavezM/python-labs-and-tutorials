"""
#Declaracion try
try:
    # 1. El programa INTENTA ejecutar este código
    numerador = int(input("ingrese numerador"))
    denominador = int(input("ingrese denominador")) 
    
    resultado = numerador / denominador
    print(f"El resultado es: {resultado}")

except ZeroDivisionError:
    # 2. Si ocurre un error de "división por cero", se ejecuta esto
    print("¡Error! No se puede dividir un número entre cero.")

"""

"""
#Declaracion except
try:
    # Intentamos pedir los datos y hacer la operación
    numerador = int(input("Introduce el primer número: "))
    denominador = int(input("Introduce el segundo número: "))
    
    resultado = numerador / denominador
    print(f"El resultado de la división es: {resultado}")

except ValueError:
    # PRIMER EXCEPT: Se activa si el usuario escribe texto (ej. "hola")
    print("❌ Error: Debes introducir un número entero válido, no letras.")

except ZeroDivisionError:
    # SEGUNDO EXCEPT: Se activa si el segundo número es 0
    print("❌ Error: Matemáticamente no se puede dividir entre cero.")
"""

#Declaracion finally
try:
    print("1. Intentando abrir y escribir en el archivo...")
    # Abrimos un archivo llamado 'notas.txt'
    archivo = open("notas.txt", "w")
    
    # Forzamos un error matemático a propósito para interrumpir el proceso
    error = 10 / 2  
    
    # Esta línea nunca se ejecutará por culpa del error de arriba
    archivo.write("Esta linea no se guardara.")

except ZeroDivisionError:
    print("2. ❌ Ocurrió un error: ¡Intentaste dividir entre cero!")

finally:
    # No importa que la división fallara, el archivo debe cerrarse de forma segura
    archivo.close()
    print("3. 🔒 Bloque Finally ejecutado: El archivo se ha cerrado de forma segura.")
