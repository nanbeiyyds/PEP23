"""
Programa02:Lectura con csv.DicReader()
Crea un programa que lea el archivo ciudades.csv usando csv.DictReader().
Debe :
    - Mostrar los nombre de las columnas (fieldnames)
    - Recorrer las filas e imprimir información como : 
        {Ciudad ({Pais}) tiene una poblacion aproxima de {poblacion(millones)} millones
    - Si el archivo no incluye cabecera, define manualmente los campos necesarios
"""
import csv
import os as strerror
print ("\n Programa 02 : Lectura con csv.DictReader()")

try:
    with open("ciudades.csv","r",encoding="UTF-8") as fichero:
        #DictReader usa la primera linea como claves de diccionario
        lector_dict = csv.DictReader(fichero)

        #mostrar los nombres de las columnas
        print("Nombres de las columnas : ", lector_dict.fieldnames)

        #recorrer las filas
        for fila in lector_dict:
            #accedemos a los datos usando el nombre de la columna
            ciudad = fila['Ciudad']
            pais = fila['Pais']
            poblacion = fila['Población (millones)']

            print(f"{ciudad}({pais}) tiene una poblacion aproximada de {poblacion} millones.")
except FileNotFoundError:
    print("ERROR. EL fichero no se encuentra")
except Exception as exc:
    print(f"ERROR. {strerror(exc.errno)}")    