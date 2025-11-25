"""
Programa1: lectura completa de un fichero
Escribe un programa en Python que abra un fihcero llamado datos.txt, lea todo su
obtenido con read() y lo muestre por pantalla.
El fichero debe contener al menos tres líneas de texto.
"""

fichero = open("datos.txt","rt",encoding="UTF-8")
contenido = fichero.readlines()
print(contenido)
fichero.close()
