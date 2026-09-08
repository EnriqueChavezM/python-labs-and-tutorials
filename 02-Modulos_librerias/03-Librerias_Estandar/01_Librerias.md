# 3. Librerias Estándar

La biblioteca estándar de Python ofrece una amplia gama de módulos con funciones y clases útiles.

---

## Tabla de Contenido

- [Módulo Math](#módulo-math)
- [Módulo random](#módulo-random)
- [Módulo datetime](#módulo-datetime)
- [Ejemplos Practicos](#ejemplos-practicos)

---

## Módulo Math

El módulo *math* es una librería integrada en Python que proporciona funciones y constantes para realizar operaciones matemáticas avanzadas (trigonometría, logaritmos, redondeo, raíces, etc.).

| Categoría | Descripcion | Sintaxis |
| :---: | :--- | :---: |
| *Constantes* | Valor de pi ($\pi \approx 3.14159$). | `math.pi` |
| *Constantes* | Valor de Euler ($e \approx 2.71828$). | `math.pi` |
| *Redondeo* | Redondea hacia arriba al entero más cercano. | `math.ceil(x)` |
| *Redondeo* | Redondea hacia abajo al entero más cercano. | `math.floor(x)` |
| *Potencias y Raíces* | Devuelve la raíz cuadrada de x. | `math.sqrt(x)` |
| *Potencias y Raíces* | Eleva x a la potencia y ($x^y$). | `math.pow(x, y)` |
| *Avanzadas* | Devuelve el factorial de un número entero. | `math.factorial(x)` |
| *Avanzadas* | Devuelve el Máximo Común Divisor entre a y b. | `math.gcd(a, b)` |

## Módulo random

El módulo *random* en Python se utiliza para generar elementos o números aleatorios.

| Función | Descripcion | Sintaxis |
| :---: | :--- | :---: |
| *randint(a, b)* | Genera un número entero aleatorio entre a y b **(ambos incluidos)**. | `random.randint(a, b)` |
| *random()* | Genera un número decimal aleatorio entre 0.0 y 1.0 **(excluyendo el 1.0)**. | `random.random()` |
| *choice(secuencia)* | Elige un solo elemento al azar de una lista, tupla o texto. | `random.choice(lista)` |
| *choices(secuencia, k=n)* | Selecciona *n* elementos al azar **(puede repetir elementos)**. | `random.choices(lista, k=n)` |
| *shuffle(secuencia)* | Mezcla/desordena los elementos de una lista directamente. | `random.shuffle(lista)` |
| *sample(secuencia, k=n)* | Selecciona *n* elementos al azar sin repetirlos. | `random.sample(lista, k=n)` |

## Módulo datetime

El módulo *datetime* en Python sirve para trabajar con fechas, horas e intervalos de tiempo. Permite realizar operaciones como obtener la fecha actual, calcular diferencias entre días o cambiar el formato en que se muestran las fechas.

| Clase | ¿Para qué sirve? | Ejemplo de uso |
| :---: | :--- | :--- |
| *date* | Trabaja solo con fechas (año, mes, día). | Para cumpleaños, fechas de entrega. |
| *time* | Trabaja solo con horas (hora, minuto, segundo, microsegundo). | Para horarios de alarmas o citas. |
| *datetime* | Combina fecha y hora juntas. | Registros de logs, marcas de tiempo. |
| *timedelta* | Representa una duración o diferencia de tiempo (días, horas, minutos). | Sumar o restar días a una fecha. |
| *strftime* | Convierte un objeto de tipo fecha **(datetime)** a un texto **(string)** con el formato elegido. | Dar formato especifico a fecha. |
| *strptime* | Convierte una cadena de texto **(string)** a un objeto de tipo fecha **(datetime)**. | Convertir texto en formato de fecha. |

---

## Ejemplos Practicos

- [Modulo *math.py*](/02-Modulos_librerias/03-Librerias_Estandar/02_Modulo_math.py)
- [Modulo *random.py*](/02-Modulos_librerias/03-Librerias_Estandar/03_Modulo_random.py)
- [Modulo *datetime.py*](/02-Modulos_librerias/03-Librerias_Estandar/04_Modulo_datetime.py)

---

[Inicio](#3-librerias-estándar)

---

[Tabla de contenido principal](/Tabla_Contenido.md)

---
