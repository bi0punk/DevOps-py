import psutil

uso_disco = psutil.disk_usage("/")

print(uso_disco)
print(type(uso_disco))