"""
Escribe un programa que reciba un número de bytes y muestre por pantalla cuantos 
GBytes, MBytes, KBytes y Bytes son. Tanto para el sistema decimal como el binario.
 La salida debe ser algo así:
 1000000000 bytes en sistema decimal (SI): 1 GB, 0 MB, 0 KB, 0 bytes
 1000000000 bytes en sistema binario (IEC): 0 GiB, 953 MiB, 690 KiB, 512 bytes
 Unidad Sistema decimal (SI) Sistema binario (IEC)
 1 KB / KiB  1.000 bytes  1.024 bytes
 1 MB / MiB  1.000 KB     1.024 KiB
 1 GB / GiB  1.000 MB     1.024 MiB
 1 TB / TiB  1.000 GB     1.024 GiB
 1 PB / PiB  1.000 TB     1.024 TiB
 1 EB / EiB  1.000 PB     1.024 PiB
 Decimal (SI, 1000) → lo usan fabricantes de discos, redes, marketing de 
almacenamiento.
 Binario (IEC, 1024) → lo usan sistemas operativos, memoria RAM, tamaños de 
archivos
"""
# programa14 corregido

bytes = int(input("Introduce el número de bytes: "))

# Sistema decimal (1000)
gb = int(bytes / 1000000000)
mb = int((bytes % 1000000000) / 1000000)
kb = int((bytes % 1000000) / 1000)
b = bytes % 1000

print(bytes, "bytes en decimal (SI):", gb, "GB,", mb, "MB,", kb, "KB,", b, "bytes")

# Sistema binario (1024)
gib = int(bytes / (1024 ** 3))
mib = int((bytes % (1024 ** 3)) / (1024 ** 2))
kib = int((bytes % (1024 ** 2)) / 1024)
bb = bytes % 1024

print(bytes, "bytes en binario (IEC):", gib, "GiB,", mib, "MiB,", kib, "KiB,", bb, "bytes")
