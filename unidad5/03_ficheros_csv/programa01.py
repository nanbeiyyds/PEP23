import csv
import os as strerror
'''Programa01 : lectura básica con csv.reades()
Crea un fichero llamado ciudades.csv con el siguiente contenido....
Escribe un programa que : 
    - Lea el fichero usando csv.reader()
    - Muestre en pantalla frases como :
        - La ciudad de Tokio está en Japón y tiene 37.4 millones de habitantes
        - Controle las posibles excepciones
'''
print("\n CSV Programa 01 : Lectura con csv.reader()")

try:
    with open("ciudades.csv", "r",encoding="UTF-8") as fichero:
        lector_csv = csv.reader(fichero)
        #saltamos la cabecera para empezar con los datos
        next(lector_csv)

        for fila in lector_csv:
            ciudad = fila[0]
            pais = fila[1]
            poblacion = fila[2]
            print (f"La ciudad de {ciudad} está en {pais} y tiene {poblacion} millones de habitantes")
except FileNotFoundError:
    print("ERROR. El fichero no encontrado")
except Exception as exc:
    #usamos strerror para mostrar el error
    print(f"ERROR. {strerror(exc.errno)}")    
