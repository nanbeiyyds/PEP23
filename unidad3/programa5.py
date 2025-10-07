"""
 Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables 
en Python (globales, no locales y locales)
"""
x = "variable global"

def externa():
    y = "variable local de externa"
    
    def interna():
        nonlocal y  
        global x  
        
        y = "modificada por nonlocal"
        x = "modificada por global"
        
        z = "variable local de interna"
        print("Dentro deinterna:")
        print("x =", x) 
        print("y =", y)
        print("z =", z)
        print("-------------------------")

    print("Antes de llamar a interna:")
    print("x =", x)
    print("y =", y)
    print("-------------------------")

    interna()

    print("Después de llamar a interna:")
    print("x =", x)
    print("y =", y)
    print("-------------------------")


print("Antes de llamar a externa:")
print("x =", x)
print("-------------------------")

externa()

print("Después de llamar a externa:")
print("x =", x)
print("-------------------------")
