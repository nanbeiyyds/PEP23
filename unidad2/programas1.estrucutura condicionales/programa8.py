"""
Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que 
saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya 
sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
 Puedes pedir el valor de cada tirada de dados por teclado o usar la  la función 
random.randrange(1, 7) para obtener un número aleatorio entre 1 y 6 (para ello 
debes poner import random al inicio del programa)
"""


print("Jugador 1:")
d11 = int(input("Dado 1 del jugador1 (1-6): "))
d12 = int(input("Dado 2 del jugador1 (1-6): "))
print("Jugador 2:")
d21 = int(input("Dado 1 del jugador2 (1-6): "))
d22 = int(input("Dado 2 del jugador2 (1-6): "))

s1 = d11 + d12
s2 = d21 + d22

if s1 > s2:
    print("Gana Jugador 1 con", s1, "puntos.")
elif s2 > s1:
    print("Gana Jugador 2 con", s2, "puntos.")
else:
    # mismos totales -> mirar el dado mayor de cada jugador
    maximo1 = max(d11, d12)
    maximo2 = max(d21, d22)
    if maximo1 > maximo2:
        print("Empate en total, pero gana Jugador 1 por dado más alto.")
    elif maximo2 > maximo1:
        print("Empate en total, pero gana Jugador 2 por dado más alto.")
    else:
        print("Empate total. Empatan ambos jugadores.")
