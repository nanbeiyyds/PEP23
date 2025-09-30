""" 
Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor 
o que indique que son iguales.
"""

a = float(input("Primer número: "))
b = float(input("Segundo número: "))

if a < b:
    print(a, "es menor que", b)
elif a > b:
    print(a, "es mayor que", b)
else:
    print("Los números son iguales.")
