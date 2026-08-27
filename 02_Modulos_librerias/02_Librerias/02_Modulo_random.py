import random

# 1. Simular el tiro de un dado (entero del 1 al 6)
dado = random.randint(1, 6)
print(f"Resultado del dado: {dado}")

# 2. Elegir un ganador al azar de una lista
participantes = ["Ana", "Carlos", "Beatriz", "David", "Elena"]
ganador = random.choice(participantes)
print(f"El ganador es: {ganador}")

# 3. Mezclar una baraja de cartas o lista
colores = ["Rojo", "Azul", "Verde", "Amarillo"]
random.shuffle(colores)
print(f"Lista mezclada: {colores}")

# 4. Seleccionar un equipo de 2 personas sin repetir
equipo = random.sample(participantes, k=2)
print(f"Integrantes del equipo: {equipo}")