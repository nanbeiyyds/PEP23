"""
 Escriba un programa que pida un año y que escriba si es bisiesto o no. Un año es bisiesto 
si es múltiplos de 4 pero no múltiplos de 100, aunque si los múltiplos de 400.
"""

year = int(input("Introduce un año: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "es bisiesto.")
else:
    print(year, "no es bisiesto.")
