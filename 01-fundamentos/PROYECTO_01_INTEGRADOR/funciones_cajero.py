def mostrar_saldo(saldo):
    print(f"Su saldo disponible es de ${saldo}")

def depositar(saldo):
            print(f"Su saldo disponible es de ${saldo}")
            deposito= float(input("Digite el valor que desea depositar:"))
            if deposito <= 0:
                print("No se puede realizar el depósito, el valor debe ser mayor a 0")
                return saldo
            else:
                nuevo_saldo = saldo + deposito
                print(f"Su deposito se ha relaizado correctamente, su saldo ahora es de ${nuevo_saldo}")
                return nuevo_saldo

def retirar(saldo):
            print(f"Su saldo disponible es de ${saldo}")
            retiro = float(input("Digite la cantidad que desea retirar:"))
            if retiro <= 0:
                print("No se puede realizar el retiro, el valor debe ser mayor a 0")
                return saldo
            elif retiro > saldo:
                print("No se puede retirar una cantidad mayor a su saldo")
                return saldo
            else:
                nuevo_saldo = saldo - retiro
                print(f"Su retiro se ha relaizado correctamente, su saldo ahora es de ${nuevo_saldo}")
                return nuevo_saldo