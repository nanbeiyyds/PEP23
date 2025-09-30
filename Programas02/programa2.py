#  Escribe un programa que 
# Cree una variable que almacene el número entero 6. 
# Muestre por pantalla el tipo del objeto que contiene el número 6, y el tipo del objeto al que apunta la variable (deben ser iguales)
# Cree otra variable a la que se asigne la primera variable.
# Muestre por pantalla el tipo del objeto que contiene el número 6 y el tipo del objeto al que apunta la variable (deben ser iguales)
# Utilice los operadores de identidad (is e is not)  para comprobar y mostrar por pantalla que los dos variables apuntan al mismo objeto y por lo tanto a la misma posición de memoria.
# Asigne la cadena “Hola” a la primera variable.
# Muestre por pantalla el tipo del objeto que contiene la cadena “Hola” y el tipo del objeto al que apunta la variable (deben ser iguales) (y diferentes al objeto 6).
# Utilice la función isinstance() para comprobar y mostrar por pantalla que el objeto al que apunta la primera variable es de tipo int y el de la segunda es de tipo str.
x = 6
print("Valor x : ",x,"Tipo: ",type(x))
y = x
print("Valor y:", y, "Tipo:", type(y)) 

#is,is not
print("x is y:", x is y)
print("x is not y ", x is not y )

#cambiar el variable x
x = "Hola" 
print("Nuevo valor x:", x, "Tipo:", type(x)) 

#isinstance
print("isinstance(x, int):", isinstance(x, int)) 
print("isinstance(x, str):", isinstance(x, str))