"""
Primer ejemplo
    Crear un programa que valide la mayoria de edad  y si esta  graduado

    Condicional:
    -Si tiene mas de 18 años ya esmayor de edad
    - Solo puede graduarse si es mayor de edad

#Pedir edad  del  usuario
edad = int(input("¿Cuantos años tienes?\n"))

#Condiciones
if edad > 18:
    print("Felicidades!!! Ya eres mayor de edad")
    #Preguntar si esta graduado
    graduacion = input("¿Ya te has graduado? (si) o (no)\n")
    if graduacion == "si":
        print("Felicidades!!!! Por  tu graduacion")
    else:
        print("Sigue preparandote para la graduacion")
else:
    print("Eres menor de edad")

"""

"""
Segundo ejemplo
    Crea un programa para un sistema de creación de personajes de videojuego. 
    Los requisitos son:
    -El nivel del personaje determina las armas que puede usar:
        -Nivel 1-5: Solo puede usar armas básicas.
        -Nivel 6-10: Puede usar armas avanzadas si ha completado el entrenamiento.
        -Nivel 11: Puede usar cualquier arma.

#Solisitar nivel al usuario
nivel = int(input("Que nivel tiene el personaje:\n"))

#Variavle de mensaje
mensaje_nivel = "None"

#Condiciones
if nivel <= 0:
    mensaje_nivel = "Nivel Inválido"
elif nivel <= 5:
    mensaje_nivel = "Solo armas básicas"
elif nivel <= 10:
    #Preguntar si completo entrenamiento
    entrenamiento = input("¿Ha completado el entrenamiento? (si) o (no)\n")
    if entrenamiento == "no":
        mensaje_nivel = "Necesita entrenamiento con armas"
    else:
        mensaje_nivel = "Acceso a armas avanzadas"
else:
    mensaje_nivel = "Acceso a todas las armas"

print(mensaje_nivel)

"""

"""
Tercer ejemplo
    Escribe un programa que determine la elegibilidad para ver una película según la edad y la supervisión parental.

    Condiciones:
    - Si edad es 18 años o más, mostrar "Puedes ver cualquier película".
    - Si edad en menor a 18 años pero tiene supervicion, mostrar "Puedes ver películas PG-13".
    - si no tiene supervicion, mostrar "Solo puedes ver películas aptas para todos los públicos".
"""
#Solisitar edad al usuario
edad = int(input("¿Cuantos años tienes:?\n"))

#Variavle de mensaje 
mensaje = "None"

#Condicional
if edad >= 18:
    mensaje = "Puedes ver cualquier pelicula"

else:
    #preguntar si tiene supervicion
    Supervicion  = input("¿Tienes Supervicion? (si) o (no)\n")
    if Supervicion == "si":
        mensaje = "Puedes ver películas PG-13"
    else:
        mensaje = "Solo puedes ver películas aptas para todos los públicos"

print(mensaje)