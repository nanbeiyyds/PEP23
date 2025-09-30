#Escribe un programa que calcule la calificación de estudiante en un módulo. La 
#calificación se obtiene de la calificación parcial en cada RA (RA1 20%, RA2, 60% y RA3 
#20%).
ra1 = float(input("Nota RA1 : "))
ra2 = float(input("Nota RA2 : "))
ra3 = float(input("Nota RA3 : "))

final = (ra1 * 0.2) + (ra2 * 0.6) + (ra3 * 0.2)

print("Nota final : " , final)
