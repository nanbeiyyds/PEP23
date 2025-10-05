"""
 Escribe un programa para jugar a una versión muy simplificada del black jack. En primer 
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A 
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando 
para obtener su puntuación,  hasta que el quiera. Si se pasa de 21 pierde, si obtiene una
 puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la 
banca gana.
"""

import random

banca = random.randrange(17, 22)
print("La banca ha sacado:", banca)

suma = 0
while True:
    sacar = input("¿Quieres sacar una carta (1-5)? (s/n): ")
    if sacar != "s":
        break
    carta = random.randrange(1, 6)
    suma += carta
    print("Has sacado:", carta, "Suma actual:", suma)
    if suma > 21:
        print("Te has pasado (>21). Pierdes.")
        break

if suma <= 21:
    if suma > banca:
        print("Has ganado. Tu", suma, "vs banca", banca)
    else:
        print("Has perdido. Tu", suma, "vs banca", banca)
