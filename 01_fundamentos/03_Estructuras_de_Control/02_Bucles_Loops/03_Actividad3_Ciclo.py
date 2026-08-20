"""
Caso
    Imagina que culminaste el 5º semestre de la universidad, en el cual viste las siguientes asignaturas: 
        - Seguridad Informática = 5.0 
        - Ingeniería Web = 4.5
        - Inteligencia Artificial = 3.6
        - Programación Móvil = 3.9
        - Redes = 4.3

Requisitos
    - Solicitar nombre completo del estudiante
    - Solicitar el nombre de la materia y la calificacion
    - Calcular el promedio de las calificaciones
    - Mostrar el promedio de las calificaciones
        - Promedio = (Nota1 + Nota2 + Nota3 + Nota4 + Nota5 ) / 5

Resultado de salida
    - Nombre del estudiante
    - Promedio del semestre

Resultado
    ***RESULTADOS***
    Hola, Enrique Chavez. Tienes un promedio de: 4.26 en el 5to semestre.
"""
#Informacion de entrada
nombre = input("Nombre completo: ")

#Variables
materias = 5
contador = 1
suma_calificaciones = 0.0

#Ciclo para solicitar las calificaciones de las materias
while contador <= materias:

    nombre_materia = input(f"Ingrese el nombre de la {contador} materia: ")
    calificacion = float(input(f"Ingrese la calificación para la materia {nombre_materia}: "))

    #Calcular la suma de las calificaciones y aumentar el contador
    suma_calificaciones += calificacion
    contador += 1

#Calculo del promedio
promedio = suma_calificaciones / materias

#Salida de resultados
print(f"***RESULTADOS***")
print(f"Hola, {nombre}. Tienes un promedio de: {promedio} en el 5to semestre.")