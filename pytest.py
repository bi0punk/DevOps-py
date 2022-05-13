import socket

def obtener_info_equipo():
    hostname = socket.gethostname()
    ip_host = socket.gethostbyname(hostname)
    print(hostname)
    print(ip_host)

if __name__ == '__main__':
		 obtener_info_equipo()