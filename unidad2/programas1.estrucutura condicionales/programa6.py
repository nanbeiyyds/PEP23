"""
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
"""

dia = int(input("Día: "))
mes = int(input("Mes: "))
year = int(input("Año: "))

valida = True

if mes < 1 or mes > 12:
    valida = False
else:
    
    if mes in (1, 3, 5, 7, 8, 10, 12):
        maximo= 31
    elif mes in (4, 6, 9, 11):
        maximo = 30
    else: 
        # comprobamos bisiesto simple:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            maximo = 29
        else:
            maximo= 28
    if dia < 1 or dia > maximo:
        valida = False

if valida:
    print("Fecha correcta")
else:
    print("Fecha incorrecta.")
