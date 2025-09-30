"""
Escribe un programa  que lea por teclado un número real entre 1 y 10, simulando una 
nota numérica, y muestre un mensaje indicando la calificación obtenida teniendo en 
cuenta los siguientes rangos:
 • Insuficiente: [0, 5)
 • Suficiente: [5, 6)
 • Bien: [6, 7)
 • Notable: [7, 9)
 • Sobresaliente: [9, 10
 Si el número introducido no está en ninguno de los rangos anteriores debe mostrar un 
mensaje de error indicando que la nota no es válida.
 Hay que usar la estructura match.
"""

nota = float(input("Introduce una nota [0 - 10]: "))

if 0 <= nota < 5:
    clave = "insuf"
elif 5 <= nota < 6:
    clave = "suf"
elif 6 <= nota < 7:
    clave = "bien"
elif 7 <= nota < 9:
    clave = "not"
elif 9 <= nota <= 10:
    clave = "sob"
else:
    clave = "invalida"

match clave:
    case "insuf":
        print("Insuficiente")
    case "suf":
        print("Suficiente")
    case "bien":
        print("Bien")
    case "not":
        print("Notable")
    case "sob":
        print("Sobresaliente")
    case _:
        print("Nota no válida")
