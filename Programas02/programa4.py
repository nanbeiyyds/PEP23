# Escribe un programa que pregunte la base y altura de una rectángulo y calcule su área y perímetro.
base = float(input("¿Cuál es la base?"))
altura = float(input("¿Y cuál es la altura de una rectangulo?"))

#calcula resultado
area = base * altura
perimetro = 2 * (base + altura)

#imprimir el resultado
print("Área : " , area)
print("Perímetro : " , perimetro)