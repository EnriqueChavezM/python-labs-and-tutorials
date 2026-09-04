# 4. Operadores

---

## Tabla de Contenido

- [Aritméticos](#aritméticos)
  - [Aritméticos de Asignación](#aritméticos-de-asignación)
- [Lógicos](#lógicos)
- [Relacionales](#relacionales)
- [Ejemplo Practico](/01-Fundamentos/04-Operadores/02_Ejemplo_Operadores.py)

---

## Aritméticos

Los operadores son símbolos especiales que representan cálculos simples, como la suma y la multiplicación.

| Símbolo | Descripción | Descripción | Ejemplo |
| :---: | :---: | :--- | :---: |
| + | Suma | Agrega dos números | V = 4.5 + 3 = 7.5 |
| - | Resta | Resta el segundo al primer número | V = 4.5 – 3 = 1.5 |
| * | Multiplicación | Multiplica dos números | V = 5 * 3 = 15 |
| / | División | Divide el primer número entre el segundo y da decimales | V = 5 / 2 = 2.5 |
| // | División Entera | Divide y deja solo la parte entera, borrando los decimales | V = 5 / 2 = 2 |
| % | Modulo | Da el residuo o resto de una división | V = 7 % 3 = 1 |
| ** | Potencia | Eleva el número a la potencia | V = 2 ** 3 = 8 |

### Aritméticos de Asignación

Los operadores de asignación son aquellos que se utilizan para asignar un valor a una variable.

| Operador | Ejemplo | Equivalencia |
| :---: | :---: | :---: |
| = | X = 2 | X = 2 |
| += | X += 2 | X = X + 2 |
| -= | X -= 2 | X = X - 2 |
| *= | X *= 2 | X = X * 2 |
| /= | X /= 2 | X = X / 2 |
| //= | X //= 2 | X = X // 2 |
| %= | X %= 2 | X = X % 2 |
| **= | X **= 2 | X = X ** 2 |

---

## Lógicos

Los operadores lógicos nos permiten trabajar con valores de tipo booleano. Se utilizan para combinar expresiones y evaluar múltiples condiciones

| Símbolo | Descripción |
| :---: | :--- |
| ``and`` | Es una “y” lógica que devuelve un resultado *True* solo si todos sus operadores son *True* |
| ``or`` | Es una “o” lógica que devuelve un resultado *True* solo si alguno sus operadores son *True* |
| ``not`` | Es una negación que devuelve un resultado *True* si su argumento es *False* |

---

## Relacionales

Los operadores relacionales se utilizan para comparar dos valores, que pueden ser números, caracteres, cadenas de caracteres, constantes o variables.

| Símbolo | Descripción | Ejemplo | Resultado |
| :---: | :---: | :---: | :---: |
| == | Igual que | X = (‘a’ == ‘b’) | X = False |
| != | Distinto que | X = (‘a’ != ‘b’) | X = True |
| < | Menor que | X = (1 < 10) | X = True |
| > | Mayor que | X = (11 > 22) | X = False |
| <= | Menor o igual que | X = (12 <= 15) | X = True |
| >= | Mayor o igual que | X = (12 >= 15) | X = False |

---
