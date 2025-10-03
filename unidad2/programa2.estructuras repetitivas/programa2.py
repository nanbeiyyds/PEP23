"""
 Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de 
pedir el número hasta que no se introduzca correctamente
"""
n= int(input("Introduce un nñumero entre 1 y 10 : "))
while n<1 or n>10:
    print("Numero no válido. Intenta de nuevo : ")
    n = int(input("Introduce un número entre 1 y 10"))
print("Número correcto: " , n)