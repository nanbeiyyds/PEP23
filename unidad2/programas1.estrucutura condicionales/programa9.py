"""
Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer 
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle 
qué opción desea elegir. Por ejemplo:
 1. Piedra
 2. Papel
 3. Tijera
 Seleccione una opción (1, 2 o 3):
 Después de leer la opción seleccionada por el usuario el programa generará un número 
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha 
ganado o ha perdido dependiendo del resultado.
 Ten en cuenta que:
 • La piedra gana a la tijera pero pierde contra el papel.
 • El papel gana a la piedra pero pierde contra la tijera.
 • La tijera gana al papel pero pierde contra la piedra.
"""
import random

print("1. Piedra\n2. Papel\n3. Tijera")
jugador = int(input("Selecciona (1,2,3): "))
pc = random.randrange(1, 4)

print("Tú elegiste:", jugador, "  PC eligió:", pc)

if jugador == pc:
    print("Empate.")
else:
    # reglas: 1 gana a 3; 2 gana a 1; 3 gana a 2
    if (jugador == 1 and pc == 3) or (jugador == 2 and pc == 1) or (jugador == 3 and pc == 2):
        print("Has ganado.")
    else:
        print("Has perdido.")
