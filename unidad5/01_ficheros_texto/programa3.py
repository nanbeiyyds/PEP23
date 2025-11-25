"""
Programa3:Estrucura básica
Escribe un programa que cree un fichero saludo.txt y escriba tres frases dentro
- usa el modo 'w'
- Comprueba que al ejecutar el programa dos veces, el archivo se sobrescribe
"""


with open ("saludo.txt","w",encoding="UTF-8") as fichero:
    fichero.write("Hola\n")
    fichero.write("Buenos días\n")
    fichero.write("Hasta luego\n")