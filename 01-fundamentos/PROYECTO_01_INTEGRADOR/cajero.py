from funciones_cajero import *
saldo: float = 2500.0
salir:bool = False

while salir != True:
    print("Bienvenido al cajero")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    opcion= int(input("Ingrese el numero de la opción que desea realizar"))

    #Usar una lista y la not in para saber si no esta en la lista - correccion de IA
    if opcion not in [1,2,3,4]:
        print("Opcion invalida, digite un numero del 1 al 4 porfavor")
        salir = False

    if opcion == 1:
        mostrar_saldo(saldo)

    elif opcion == 2:
        saldo = depositar(saldo)

    elif opcion == 3:
        saldo = retirar(saldo)

    elif opcion == 4:
        salir = True
        print("""Gracias por usar el cajero.
        Su saldo final es de ${saldo},
        Hasta luego""")
