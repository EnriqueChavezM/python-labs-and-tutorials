"""
Implementa un programa con una clase llamada Persona que contenga dos atributos que serán ingresados por teclado: nombre y edad. Además, que contenga un método llamado imprimir que devuelva el nombre y la edad.
Después, crea otra clase llamada Ciudadano que herede de la clase Persona y agregue un atributo llamado depósito que será ingresado por teclado. Además, contendrá el método llamado imprimir para mostrar el depósito. 
Así mismo, crea otro método llamado impuestos y si el depósito es superior a 4000 USD muestre que SI debe pagar, caso contrario no deberá pagar. 
Los datos para este ejercicio son los siguientes:

        Nombre      |   Edad    |   Depósito
    Manuel Chima    |    25     |     6700
    Fayle García    |    56     |     3500
    Lesly Rodríguez |    34     |     9000
    Mario Herrera   |    45     |     2500

"""
class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre:\n→ ")
        self.edad = input("Ingrese la edad:\n→ ")

    def imprime(self):
        print("Nombre:\t ", self.nombre)
        print("Edad:\t ", self.edad)

class Ciudadano(Persona):
    def __init__(self):
        super().__init__()
        self.deposito = float(input("Ingrese el dinero a depositar:\n→ "))

    def imprimir(self):
        super().imprime()
        print("Depósito:", self.deposito)

    def impuestos(self):
        if self.deposito > 4000:
            print(f"El ciudadano {self.nombre} debe pagar impuestos")
        else:
            print(f"El ciudadano {self.nombre} no debe pagar impuestos")

#Instancias
continuar = True
consulta = 1
print("BIENVENIDO ASESOR!!!\nIngrese su primer consulta")
while continuar:

    if consulta == 1:
        ciudadano1 = Ciudadano()
        ciudadano1.imprimir()
        ciudadano1.impuestos()
        consulta = int(input("\n¿Quiere realizar otra consulta?\n 1 = Si\n 0 = No\n→ "))
    else:
        continuar = False


"""
        Nombre      |   Edad    |   Depósito    |   Pagar impuestos
    Manuel Chima    |    25     |     6700      |        Si
    Fayle García    |    56     |     3500      |        No
    Lesly Rodríguez |    34     |     9000      |        Si
    Mario Herrera   |    45     |     2500      |        No
"""