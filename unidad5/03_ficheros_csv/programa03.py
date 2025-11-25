"""
Programa03: Escrituta de un CSV con csv.writer()
Crea un programa que genere un fichero nuevo llamado capitales.csv con los siguientes datos:
....
El programa debe:
    - Escribir la cabecera y los datos con writerow() y writerows()
    - Usar un bloque try/except con os.trerror() para capturar errores de E/S
    - Confirmar con mensaje final: archivo 'capitales.csv' creado correctamente
"""
import csv
import os as strerror

#datos a escribir
cabecera = ["ciudad","Pais","Continente"]
datos = [
    ["Paris","Francia","Europa"],
    ["Canberra","Australia","Oceania"],
    ["Nairobi","Kenia","Africa"],
    ["Ottowa","Canada","America"],
]

try:
    #usamos 'w' para escritura y 'newline = para enviar lineas vacias extra en windows'
    with open("capitales.csv","w",encoding="UTF-8",newline="") as fichero:
        escritor_csv = csv.writer(fichero)

        #escribir la cabecera con writerow()
        escritor_csv.writerow(cabecera)

        #escribir los datos con writerows() (más de una fila)
        escritor_csv.writerows(datos)
    print("Archivo 'capitales.csv creado correctamente'")
except Exception as exc:
    #capturar errores de E/S con os.strerror()
    print(f"ERROR de E/S : {strerror(exc.errno)}")
 
