"""
Modifica el programa anterior par que pida en primer lugar el número de jugadores que 
van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la 
banca.
"""

import random

banca = random.randrange(17, 22)
print("La banca sacó:", banca)

n_jug = int(input("Número de jugadores: "))
for j in range(1, n_jug + 1):
    print("--- Jugador", j, "---")
    suma = 0
    while True:
        sacar = input("Jugador {}, ¿sacar carta (s/n)? ".format(j)).lower()
        if sacar != "s":
            break
        carta = random.randrange(1, 6)
        suma += carta
        print("Sacaste:", carta, "Suma:", suma)
        if suma > 21:
            print("Te pasaste. Pierdes.")
            break
    if suma <= 21:
        if suma > banca:
            print("Jugador", j, "GANA a la banca con", suma)
        else:
            print("Jugador", j, "PIERDE frente a la banca con", suma)
