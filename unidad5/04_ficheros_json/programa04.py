"""
Programa 04: escribir un objeto Python en una cadena JSON
- convierte el diccionario en una cadena JSON con json.dumps()
- usa los parametros ident=2 y sort_keys=true
- Imprime la cadena generada
"""
import json
print("Programa 4 : escribir un objeto Python en una cadena JSON")

#el diccionario python
pais = {
  "nombre": "Islandia",
  "capital": "Reikiavik",
  "idiomas": ["Islandés", "Inglés"],
  "superficie_km2": 103000
}

#json.dumps() convierte el objeto Python en una cadena json
#usar indent = 2 y sort:keys=true
cadena_json = json.dumps(
    pais,
    indent=2,
    sort_keys=True, #ordenar las claves alfabeticamente
    ensure_ascii=False
)

#imprimir la cadena generada
print("Cadena Json generada : ")
print(cadena_json)