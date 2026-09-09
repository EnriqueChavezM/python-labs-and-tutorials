"""
Ejemplo 1
"""
# 1. Clase Padre (Superclase)
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def encender(self):
        return f"El vehículo {self.marca} {self.modelo} está encendido."

    def obtener_descripcion(self):
        return f"{self.marca} {self.modelo}"


# 2. Clase Hija (Subclase)
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        # Llama al constructor de Vehiculo para inicializar marca y modelo
        super().__init__(marca, modelo)
        # Añade un atributo exclusivo de Auto
        self.puertas = puertas

    # Sobrescribir un método (Overriding) y extenderlo con super()
    def encender(self):
        # Usamos el comportamiento de la clase padre y le agregamos más texto
        mensaje_padre = super().encender()
        return f"{mensaje_padre} ¡Listo para conducir con sus {self.puertas} puertas!"

    # Método propio de la clase Auto
    def tocar_bocina(self):
        return "¡Beep beep!"

# Instanciar un objeto de la clase hija
mi_auto = Auto("Toyota", "Corolla", 4)

# 1. Usa métodos heredados directamente de Vehiculo
print(mi_auto.obtener_descripcion())  # Imprime: Toyota Corolla

# 2. Usa el método modificado que aprovecha super()
print(mi_auto.encender()) 
# Imprime: El vehículo Toyota Corolla está encendido. ¡Listo para conducir con sus 4 puertas!

# 3. Usa su propio método exclusivo
print(mi_auto.tocar_bocina())  # Imprime: ¡Beep beep!