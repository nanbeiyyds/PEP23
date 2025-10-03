"""
Escribe un programa que pida un número y muestre una lista de números desde 1 al 
número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se 
pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto. 
"""

n = int(input("Introduce un número entre 1 y 10: "))
while n < 1 or n > 10:
    print("Número fuera de rango. Intenta otra vez.")
    n = int(input("Introduce un número entre 1 y 10: "))

for i in range(1, n+1):
    print(i, end=" ")
print()
