from os import remove
from prettytable import PrettyTable


from humanize import naturalsize
import psutil
import subprocess
import pathlib
import os
import sys

#############################################################################S

x = PrettyTable()

uso_disco = psutil.disk_usage("/")

print(uso_disco)
print(type(uso_disco))

def transforma_gb(bytes):
    "Convierte bytes a gigabytes."
    return bytes / 1024**3
print("Espacio total: {:.2f} GB.".format(transforma_gb(uso_disco.total)))
print("Espacio libre: {:.2f} GB.".format(transforma_gb(uso_disco.free)))
print("Espacio usado: {:.2f} GB.".format(transforma_gb(uso_disco.used)))
print("Porcentaje de espacio usado: {}%.".format(uso_disco.percent))


if uso_disco.free >= 37.15:
    print("ALERTA POCO ESPACIO")
else:
    print("NO HAY PROBLEMA, ESPACIO DISPONIBLE")


##########################################################







tamaño = 0
  
dir_clean= '/var/log/'
  
for path, dirs, files in os.walk(dir_clean): 
    for f in files: 
        fp = os.path.join(path, f) 
        tamaño += os.path.getsize(fp) 
  
print("Folder size: " + str(tamaño)) 
remove("archivo.txt")


 #in linux 
def del_log():
    contenido = os.listdir('/var/log/')
    print(contenido)

size = os.stat('lorem.txt').st_size

print(size)
print(naturalsize(size))
    
del_log()


