
def menuA():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')  
    return num
salir = False
opcion = 0
 
while not salir:

    print("\n        +-+-+-+-+") 
    print("        |C|A|A|P|")
    print("        +-+-+-+-+")
    print("CONSOLE ANSIBLE AUTOMATION PACK\n")
    
    print("1.- ---- Realizar Ping ----")
    print("2.- ---- Instalación Mariadb ----")
    print("3.- ---- Eliminación de Logs ----")
    print("4.- ---- Listar Máquinas ----")
    print("5.-       * Salir *")
      
    opcion = menuA()
 
    if opcion == 1:
        def ping():
            print ("Opcion 1")

            
    elif opcion == 2:
        print ("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        print("Opcion 3\n")
    elif opcion == 5:
        salir = True
    else:
        print ("\nIntroduce un numero entre 1 y 5")
 