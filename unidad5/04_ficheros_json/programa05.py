"""
Programa 05: Listado u filtrado de paises
Crea un programa que :
    - Lea el archivo paises.json del ejercicio 1
    - Pida al usaurio el nombre de un continente
    - Muestre solo los países pertenecientes a ese continente
    - Guarde esos resultados en un nuevo archivo JSON llamado paises_filtrados.json
"""
import json
import os as strerror

print("Programa 5 : listado  y filtrado de paises")

#leer el archivo paises.json
try:
    with open("paises.json","r",encoding="UTF-8") as fichero:
        datos_paises = json.load(fichero)
except FileNotFoundError:
    print("ERROR: El fichero paises.json no se encuentra")
except json.JSONDecodeError:
    print("ERROR: El fichero paises.json no tiene formato json valido")
except Exception as exc:
    print(f"ERROR: {strerror(exc.errno)}")

#solo continuamos si los datos se cargaron bien
if datos_paises is not None:
    #pedir al usuario el nombre de un continente
    continente_buscado = input("Introduce el nombre de un continente : ")
    #filtrar los paises
    paises_filtrado = []
    #recorremos la lista de diccionarios
    for pais in datos_paises:
        #hacemos una comparacion 
        if pais.get("continente","").lower() == continente_buscado.strip().lower():
            paises_filtrado.append(pais)
    #mostrar los paises encontrados
    print(f"Paises encontrados en {continente_buscado} : ")
    if paises_filtrado:
        for pais in paises_filtrado:
            print(f"- {pais['nombre']}({pais['poblacion']} millones)")
        
        # guardar los resultados en un nuevo archivo Json
        try:
            with open("paises_filtrados.json","w",encoding="UTF-8") as fichero_salida:
                json.dump(
                    paises_filtrado,
                    fichero_salida,
                    indent=4,
                    ensure_ascii=False
                )
            print("Resultados guardados en 'paises_filtrados,json'")
        except Exception as exc:
            print(f"ERROR al guardar : {strerror(exc.errno)}")
    else:
        print("No se encontrado paises en ese continente")