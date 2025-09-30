# Escribe un programa que reciba una cantidad de minutos y muestre por pantalla a 
# cuantas horas y minutos corresponde.

minutos = int(input("Escribir una cantidad de minutos : "))

#calcula la hora
horas = int(minutos/60)
resto = minutos % 60

print(minutos, "son " , horas , " horas y " , resto , " minutos ")