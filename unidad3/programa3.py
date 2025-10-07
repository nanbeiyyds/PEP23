"""
 Escribe un programa en Python que muestre un menú que permita al usuario seleccionar 
qué operación desea realizar. Las operaciones que puede realizar serán calcular el área 
de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será 
similar al siguiente:
 1. Calcular el área de un círculo
 2. Calcular el área de un triángulo
 3. Calcular el área de un rectángulo
 4. Salir
 Introduce una opción (1-4):
 El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la 
opción 4.
 Hay que diseñar y definir la siguientes funciones: :
 • calcular_area_circulo: recibe como parámetro de entrada el radio del círculo y 
retorna su área.
 • calcular_area_triangulo: recibe como parámetros de entrada  la base y la altura 
del triangulo y retorna su área.
 • calcular_area_rectangulo: recibe como parámetros de entrada  la base y la altura 
del rectángulo y retorna su área.
 • mostrar_menu: muestra el menú por pantalla con todas las opciones disponibles.
 • main(): lee por teclado la opción seleccionada por el usuario, valida que la opción 
está entre 1 y 4, y una vez que ha leído una opción válida llamará a la función 
correspondiente en función de la opción seleccionada.
 • opcion1: lee por teclado el valor del radio del círculo, valida que el radio siempre 
sea mayor que 0 y una vez que ha validado el radio llamará a la función 
calcular_area_circulo.
 • opcion2: descripción: lee por teclado el valor de la base y la altura del triángulo, 
valida que los dos datos son mayores que 0 y una vez que los ha validado llamará 
a la función calcular_area_triangulo.
 • opcion3: lee por teclado el valor de la base y la altura del rectángulo, valida que 
los dos datos son mayores que 0 y una vez que los ha validado llamará a la función 
calcular_area_rectangulo.
"""
import math

def opcion1():
    while True:
            radio = float(input("Introduce el radio del circulo :"))
            if radio > 0:
                area = areaCirculo(radio)
                print(f"El area del circulo es : {area:.2f}")
                break

def opcion2():
    while True:
            base = float(input("Introduce la base del triangulo : "))
            altura = float(input("Introduce la altura del triangulo : "))
            if base > 0 and altura > 0:
                area = areaTriangulo(base,altura)
                print(f"El area del triangulo es :  {area:.2f}")


def opcion3():
    while True:
            base = float(input("Introduce la base del rectangulo : "))
            altura = float(input("Introduce la altura del rectangulo : "))
            if base > 0 and altura > 0:
                area = areaRectangulo(base,altura)
                print(f"El area del rectangulo es :  {area:.2f}")


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