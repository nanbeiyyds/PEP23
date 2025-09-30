# Escribe un programa que dado un número de dos cifras, diseñe un algoritmo que permita 
#obtener el número invertido.
numero = int(input("Número de dos cifras : "))
decena = int(numero / 10)
unidad = numero % 10
invertido = unidad * 10 + decena
print("Número invertido : ", invertido)
