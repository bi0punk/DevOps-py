


import subprocess



def menuA():
    correcto=False
    
    while(not correcto):
        try:
            op=0
            op = int(input("Introduce opcion: "))
            correcto=True
        except ValueError:
            print('')  
    return op
salir = False
opcion = 0
 
while not salir:

    print("\n        +-+-+-+-+") 
    print("        |C|A|A|P|")
    print("        +-+-+-+-+")
    print("CONSOLE ANSIBLE AUTOMATION PACK\n")
    
    print("1.- ---- Realizar Ping ----")
    print("2.- ---- SSH status ----")
    print("3.- ---- Eliminación de Logs ----")
    print("4.- ---- Listar Máquinas ----")
    print("5.-       * Salir *")
    opcion = menuA()
    if opcion == 1:
        def ping():
            subprocess.call(['ansible', '-i', 'ineventario', 'all', '-m', 'ping'])
        ping()

    elif opcion == 2:
        def ssh_st():
            subprocess.call(['sudo', 'service', 'ssh', 'status'])
        ssh_st()


    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        print("Opcion 3\n")
    elif opcion == 5:
        salir = True
    else:
        print ("\nOpcion")
 

