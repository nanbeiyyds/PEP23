import csv
import os as strerror

"""Programa 04 : Escritura desde diccionarios con csv.DictWriter()
Crea un programa que escriba un archivo patrimonios.csv con información sobre ciudades con lugares Patrimonio de la Humanidad
....
El programa debe:
    - Usar DictWriter con fieldnames = [ciudad,pais,lugar emblematico]
    - Escribir la cabecera con writeheader() y las filas con writerows()
    - Cambiar el delimitador a
    - Mostrar un mensaje final: archivo patrimonio.csv generado correcctamente"""

print("Programa 04 : escritura con csv.DictWriter()")

#lista de diccionarios con los datos
patrimonios = [
    {"Ciudad": "Roma","Pais":"Italia","Lugar emblematico":"Coliseo"},
    {"Ciudad":"El Cairo","Pais":"Egipto","Lugar emblematico":"Pitamides de Guiza"},
    {"Ciudad": "Kioto","Pais":"Japón","Lugar emblematico":"Templos historicos"},
]

fieldnames = ["Ciudad","Pais","Lugar emblematico"]

try:
    #Usamos 'w', newline="" y especificamos el delimitado ';'
    with open("patrimonios.csv","w",encoding="UTF-8",newline="") as fichero:
        escritor_dict = csv.DictWriter(
            fichero,
            fieldnames=fieldnames,
            delimiter=';' #cambiamos el delimitador a punto y coma
        )
        #escribir la cabecera usando writeheader()
        escritor_dict.writeheader()

        #escribir los filas con writerows()
        escritor_dict.writerows(patrimonios)
    print("Archivo 'patrimonios.csv' generado correctamente")
except Exception as exc:
    print(f"ERROR: {strerror(exc.errno)}")