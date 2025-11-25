"""
Crea un fichero llamado paises.json con el siguiente contenido
....
Escribe un programa que : 
    - Abra el archivo y lo lea con json.load()
    - Muestre por pantalla cada pais con un formato como:
        Japón está en Asia y tiene 125.7 millones de habitantes
    - Controle posibles errores con try/except
"""
import json
import os as strerror

print("Programa 01: Lectura con json.load()")

try:
    #abrir para lectura ('r')
    with open("paises.json","r",encoding="UTF-8") as fichero:
        #json.load() lee el objeto completo del archivo
        datos_paises = json.load(fichero)

        #mostrar la informacion
        for pais in datos_paises:
            nombre = pais["nombre"]
            continente = pais["continente"]
            poblacion = pais["poblacion"]
            print(f"{nombre} esta en {continente} y tiene {poblacion} millones de habitantes")
except FileNotFoundError:
    print("ERROR : El fichero no se encuentra")
except json.JSONDecodeError:
    print("ERROR : el fichero no tiene formato JSON valido")
except Exception as exc:
    print(f"ERROR : {strerror(exc.errno)}")
