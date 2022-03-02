import psutil

uso_disco = psutil.disk_usage("/")

print(uso_disco)
print(type(uso_disco))



def to_gb(bytes):
    "Convierte bytes a gigabytes."
    return bytes / 1024**3

print("Espacio total: {:.2f} GB.".format(to_gb(disk_usage.total)))
print("Espacio libre: {:.2f} GB.".format(to_gb(disk_usage.free)))
print("Espacio usado: {:.2f} GB.".format(to_gb(disk_usage.used)))
print("Porcentaje de espacio usado: {}%.".format(disk_usage.percent))