"""
Escribe un programa que muestre una lista de números del 1 al 10. Resuelve el ejercicio 
de dos formas distintas, utilizando los bucles for y while. Cuando utilices el bucle for 
puedes hacer uso de la función range.
"""
#con while
i = 1
while i <= 10:
    print(i,end=" ")
    i += 1
print()

#con for
for i in range(1,11):
    print(i,end=" ")
print()     
