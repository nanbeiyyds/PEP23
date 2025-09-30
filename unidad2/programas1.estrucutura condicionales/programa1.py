"""
Escribe un programa que pida primero un número par y luego un número impar (positivos 
o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o 
impar respectivamente), se mostrará un aviso.
"""

a = int(input("Introduce un número par: "))
b = int(input("Introduce un número impar: "))

if a % 2 != 0:
    print("Error: el primer número no es par.")
if b % 2 == 0:
    print("Error: el segundo número no es impar.")
if a % 2 == 0 and b % 2 != 0:
    print("Correcto: primer número par y segundo número impar.")
