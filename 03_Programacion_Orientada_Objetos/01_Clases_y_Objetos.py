"""
Ejemplo 1

class Perro:
    # 1. Constructor: define los atributos iniciales
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    # 2. Métodos: acciones que puede hacer el perro
    def ladrar(self):
        return f"¡Guau! Me llamo {self.nombre}."

    def cumplir_anos(self):
        self.edad += 1
        return f"¡{self.nombre} ahora tiene {self.edad} años!"

# --- Crear objetos (Instanciación) ---

# Crear el primer objeto
mi_perro = Perro("Firulais", "Labrador", 3)

# Crear un segundo objeto independiente
otro_perro = Perro("Rocky", "Bulldog", 5)

# --- Usar los atributos y métodos ---

print(mi_perro.nombre)         # Imprime: Firulais
print(mi_perro.ladrar())       # Imprime: ¡Guau! Me llamo Firulais.

print(otro_perro.ladrar())     # Imprime: ¡Guau! Me llamo Rocky.
print(otro_perro.cumplir_anos()) # Imprime: ¡Rocky ahora tiene 6 años!
"""

"""
Ejemplo 2

class Bisicleta:
    #Metodo Atributos
    def __init__(self, color, cambios, rin):
        self.color = color
        self.cambios = cambios
        self.rin = rin

    #Metodo Comportamientos
    def frenar (self):
        return("La bicicleta esta frenando.")

    def avanzar (self):
        return("La bicicleta esta en movimiento.")

    def girar(self, g):

        if g:
            return("La bicicleta esta girando a la izquierda.")
        else:
            return("La bicicleta esta girando a la derecha.")

#Objeto(Istancias)
urbana = Bisicleta("roja", 8, 27.5)
hibrida = Bisicleta("Azul", 1, 29)

print("El color de la  bisicleta urbana es: " + str(urbana.color))
print(urbana.girar(True))

print("El rin de la bisicleta hibrida es: " + str(hibrida.rin))
print(hibrida.frenar())

"""

"""
Ejemplo 3
"""

class Animal:
    #Metodo Atributos
    def __init__(self, nombre,  edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    #Metodo comportamiento
    def caminar(self):
        return "Caminando"

    def comer(self):
        return "Comiendo"

    def dormir(self):
        return "Dormido"

gato = Animal("Manchas", 1, 4)
perro = Animal("Tony", 2, 20)
lobo = Animal("Apolo", 5, 25)

revisar = input("""
Que animal desea revisar:
   → Gato 
   → Perro
   → Lobo
""").strip().lower()

if revisar == "gato":
    print(f"Nombre:\t{gato.nombre}")
    print(f"Edad:\t{gato.edad}")
    print(f"Peso:\t{gato.peso}")
    print("Se encuentra " + str(gato.dormir()))
elif revisar == "perro":
    print(f"Nombre:\t{perro.nombre}")
    print(f"Edad:\t{perro.edad}")
    print(f"Peso:\t{perro.peso}")
    print("Se encuentra " + str(perro.caminar()))
elif revisar == "lobo":
    print(f"Nombre:\t{lobo.nombre}")
    print(f"Edad:\t{lobo.edad}")
    print(f"Peso:\t{lobo.peso}")
    print("Se encuentra " + str(lobo.comer()))
else:
    print("Animal no registrado")
