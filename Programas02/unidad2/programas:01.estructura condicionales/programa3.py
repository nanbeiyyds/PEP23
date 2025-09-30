"""
 Escribe un programa que pida dos numero y muestre su división. Se deben tener en 
cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.
"""

x = float(input("Introduce el numerador: "))
y = float(input("Introduce el denominador: "))

if y == 0:
    print("Error: división por 0 no permitida.")
else:
    print("Resultado:", x / y)
