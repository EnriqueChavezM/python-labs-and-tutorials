# 1. Definimos nuestra propia excepción personalizada
class MenorDeEdadError(Exception):
    pass

# 2. Creamos una función que usa nuestra excepción
def registrar_usuario(edad):
    if edad < 18:
        # Si es menor de edad, lanzamos nuestro error personalizado
        raise MenorDeEdadError(f"Acceso denegado. Tienes {edad} años y el mínimo es 18.")
    else:
        print("¡Registro completado con éxito! Bienvenido.")

# 3. Probamos el código usando bloques try-except
try:
    edad_usuario = int(input("Ingrese su edad: "))
    registrar_usuario(edad_usuario)

except MenorDeEdadError as error:
    # Atrapamos nuestra excepción específica y mostramos su mensaje
    print(f"❌ Error del sistema: {error}")
