# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.  El tiempo 
#de viaje hasta llegar a otra ciudad B es de N segundos. Escribie un programa que 
#determine la hora de llegada a la ciudad B.

hh = int(input("Hora de salida (HH) : "))
mm = int(input("Minuto de salida (MM) : "))
ss = int(input("Segundo de salida (SS) : "))
n = int(input("Duraion del viaje en segundos : "))

totalSegundo = (hh*3600) + (mm * 60) + ss + n

hora=int((totalSegundo/3600))%24
minuto =int((totalSegundo % 3600)/60)
segundo = totalSegundo % 60

print("Hora de llegada : " , hora , " : " , minuto , " : " , segundo)