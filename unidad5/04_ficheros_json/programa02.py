"""
- Escribir los datos en formato JSON con json.dump()
- Usar los parametros ensure_ascli = Flase y indent=4 para mejorar la legibilidad
- Mostrar el mensaje : 'Archivo capitales.jon creado correctamente'
"""
import json
import os as strerror

print("Programa 02: Escritura con json.dump()")

capitales = [
  {"país": "Francia", "capital": "París"},
  {"país": "Australia", "capital": "Canberra"},
  {"país": "Kenia", "capital": "Nairobi"},
  {"país": "Brasil", "capital": "Brasilia"}
]
try:
    #abrir para escritura ('w)
    with open("capitales.json","w",encoding="UTF-8") as fichero:
        #usar json.dump() con ensure_ascii = false (para tiledes)
        # y indent = 4 (para formato)
        json.dump(
            capitales,
            fichero,
            ensure_ascii=False,
            indent=4
        )
    print("Archivo 'capitales.json' creado correctamente")
except Exception as exc:
    print(f"ERROR : {strerror(exc.errno)}")