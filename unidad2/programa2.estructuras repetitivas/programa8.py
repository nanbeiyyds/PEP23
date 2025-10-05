"""
 Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación 
solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido. El programa 
termina cuando se acierta el número.
 Puedes generar el número usando la función random.randrange(1, 21) para 
obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio 
del programa).
 Mejora el programa de forma que el usuario tenga solo 3 intentos.
"""

import random

secreto = random.randrange(1, 21)
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    intento = int(input("Adivina el número (1-20): "))
    intentos += 1
    if intento == secreto:
        print("¡Correcto! Has adivinado en", intentos, "intentos.")
        break
    elif intento < secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

if intento != secreto:
    print("Lo siento. Se acabaron los intentos. El número era:", secreto)
