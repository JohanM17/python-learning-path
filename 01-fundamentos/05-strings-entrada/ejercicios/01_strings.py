def generar_carnet(nombre:str, carrera:str, costo:float):
    print("Ingresa tu nombre")
    nombre = input().strip().upper()
    print("Ingresa tu carrera")
    carrera = input().strip().lower().title()
    print("Ingresa el costo, solo numeros")
    costo = float(input())
    if costo is not int:
        return "Error: El costo debe ser un número"

    carnet = f"""
    ======================
    Universidad Colombiana
    ======================
    Nombre: {nombre}
    Carrera: {carrera}
    Costo: ${costo:.2f}
    """
    return carnet

print(generar_carnet("Johan","Ing.Software", 6000000))
