"""
Programa4: añadir texto sin borrar el anterior
Modifica el ejercicio anterior para que , en lugar de sobrescribir, añade nuevas líneas cada cez que se ejecute
- Usa el modo 'a'
- Al final, el fichero debe acumular todas las ejecuciones anteriores
-
"""
with open("saludo.txt", "a", encoding="UTF-8") as fichero:
    fichero.write("Nueva Hola\n")
    fichero.write("Nueva buenos días\n")
    fichero.write("Nueva hasta luego\n")
