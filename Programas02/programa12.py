#Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número de 
#millas y un número de Km, muestre respectivamente el número de millas y kilómetros. Los 
#resultados deben estar redondeados a 2 decimales.
millas = float(input("Número de millas : "))
kms = float(input("Número de km : "))

print(millas , " millas son ", round(millas * 1.61,2), "km")
print(kms , "km son ", round(kms/1.61,2), " millas")