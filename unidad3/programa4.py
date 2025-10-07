"""
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo 
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así 
que pida muestre un aviso y vuelva a pedir el valor. 
"""
import math

def opcion1():
    while True:
        try:
            radio = float(input("Introduce el radio del circulo :"))
            if radio > 0:
                area = areaCirculo(radio)
                print(f"El area del circulo es : {area:.2f}")
                break
            else:
                print("El radio debe ser mayor que 0")
        except ValueError:
            print("Por favor, introduce un numero valido")

def opcion2():
    while True:
        try: 
            base = float(input("Introduce la base del triangulo : "))
            altura = float(input("Introduce la altura del triangulo : "))
            if base > 0 and altura > 0:
                area = areaTriangulo(base,altura)
                print(f"El area del triangulo es :  {area:.2f}")
            else:
                print("El numero no valido")
        except ValueError:
                print("Por favor, introduce numero valido ")

def opcion3():
    while True:
        try: 
            base = float(input("Introduce la base del rectangulo : "))
            altura = float(input("Introduce la altura del rectangulo : "))
            if base > 0 and altura > 0:
                area = areaRectangulo(base,altura)
                print(f"El area del rectangulo es :  {area:.2f}")
            else:
                print("El numero no valido")
        except ValueError:
                print("Por favor, introduce numero valido ")

def menu():
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")

def main():
    while True:
        menu()
        opcion = int(input("Introduce una opción (1-4):"))
        if opcion == 1:
            opcion1()
        elif opcion == 2:
            opcion2()
        elif opcion == 3:
            opcion3()
        elif opcion == 4:
            print("finally,hasta luego")
            break
        else:
            print("Opcion no válida")

def areaCirculo(radio):
    return math.pi *radio ** 2

def areaTriangulo(base,altura):
    return (base*altura)/2

def areaRectangulo(base,altura):
    return base * altura


main()