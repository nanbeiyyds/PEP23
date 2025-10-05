"""
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la 
suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza 
la instrucción break y otra no.
"""

# Versión con break
suma = 0
count = 0
while True:
    n = float(input("Introduce un número (0 para terminar): "))
    if n == 0:
        break
    suma += n
    count += 1

if count > 0:
    print("Suma:", suma, "Media:", suma / count)
else:
    print("No se introdujeron números.")

# Versión sin break
suma = 0
count = 0
n = None
while True:
    n = float(input("Introduce un número (0 para terminar): "))
    if n == 0:
        break
    suma += n
    count += 1

suma = 0
count = 0
n = float(input("Introduce un número (0 para terminar): "))
while n != 0:
    suma += n
    count += 1
    n = float(input("Introduce un número (0 para terminar): "))

if count > 0:
    print("Suma:", suma, "Media:", suma / count)
else:
    print("No se introdujeron números.")
