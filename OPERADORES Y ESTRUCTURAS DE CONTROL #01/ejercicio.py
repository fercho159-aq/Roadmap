"""/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */"""

# Operadores aritméticos
a = 10
b = 3

print(f"Suma: {a + b}")         # 13
print(f"Resta: {a - b}")        # 7
print(f"Multiplicación: {a * b}")# 30
print(f"División: {a / b}")      # 3.3333...
print(f"División entera: {a // b}")  # 3
print(f"Módulo: {a % b}")       # 1
print(f"Exponente: {a ** b}")   # 1000

# Operadores de comparación
x = 5
y = 10

print(f"Igual a: {x == y}")         # False
print(f"Diferente de: {x != y}")    # True
print(f"Mayor que: {x > y}")        # False
print(f"Menor que: {x < y}")        # True
print(f"Mayor o igual: {x >= y}")   # False
print(f"Menor o igual: {x <= y}")   # True

# Operadores lógicos
p = True
q = False

print(f"AND: {p and q}")    # False
print(f"OR: {p or q}")      # True
print(f"NOT: {not p}")      # False

# Operadores de asignación
num = 5
num += 3      # num = num + 3
print(num)    # 8
num -= 2      # num = num - 2
print(num)    # 6
num *= 2      # num = num * 2
print(num)    # 12

# Operadores de identidad
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(f"lista1 is lista2: {lista1 is lista2}")       # False
print(f"lista1 is lista3: {lista1 is lista3}")       # True

# Operadores de pertenencia
print(f"2 in lista1: {2 in lista1}")                 # True
print(f"5 not in lista1: {5 not in lista1}")         # True

# if, elif, else
edad = 18

if edad < 13:
    print("Eres un niño")
elif edad < 20:
    print("Eres un adolescente")
else:
    print("Eres un adulto")

    # Bucle for
for i in range(3):
    print(f"Iteración {i}")

# Bucle while
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

    # try, except, else, finally
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
else:
    print("La división se realizó correctamente")
finally:
    print("Este bloque siempre se ejecuta")
            
print("Numeros pares entre 10 y 55 que no son 16 ni multiplos de 3")
for i in range(10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(f"Numero: {i}")