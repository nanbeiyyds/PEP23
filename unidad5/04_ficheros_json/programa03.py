"""
Programa 03 : cargar un objeto desde una cadena JSON
- convierte la cadena en un objeto Python con json-loads()
- muestra el tipo de dato se obtiene
- imprime cada pais con su moneda
"""
import json
import os as strerror
print("Programa 03: cargar objeto desde cadena")
#la cadena JSON (debe ser una string en Python)
cadena_json = """
[
    {"nombre":"Chile","moneda":"Peso chileno"},
    {"nombre":"Egipto","moneda":"Libra egipcia"}
]
"""

try:
    #json.loads() convierte la cadena JSON en un objeto Python (una lista de diccionario)
    datos_paises = json.loads(cadena_json)

    #mostrar el tipo de dato
    print("Tipo de dato : ", type(datos_paises))

    #imprimir cada país con su moneda
    for pais in datos_paises:
        print(f"{pais['nombre']} usa la moneda : {pais['moneda']}")
except json.JSONDecodeError:
    print("ERROR : La cadena JSON no es valido")
except Exception as exc:
    print(f"ERROR : {strerror(exc.errno)}")