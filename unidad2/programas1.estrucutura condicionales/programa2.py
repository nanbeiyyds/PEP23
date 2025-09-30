"""
Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no 
es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o 
negativo) y si el valor no es correcto, mostrará un aviso.
"""
a = int(input("Introduce un número par: "))
if a % 2 != 0:
    print("Error: no es par. Fin.")
else:
    b = int(input("Introduce ahora un número impar: "))
    if b % 2 == 0:
        print("Error: no es impar.")
    else:
        print("Correcto: par seguido de impar.")
