"""
Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el 
ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia 
continue
"""

print("For sin continue:")
for i in range(0, 11):
    if i % 2 == 0:
        print(i, end=" ")
print()

print("For con continue:")
for i in range(0, 11):
    if i % 2 != 0:
        continue
    print(i, end=" ")
print()

print("While sin continue:")
i = 0
while i <= 10:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print()

print("While con continue:")
i = 0
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1
print()
