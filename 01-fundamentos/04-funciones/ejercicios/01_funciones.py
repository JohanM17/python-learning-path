def calcular_descuento(precio:int):
    descuento = 2
    return precio - descuento

def calcular_precio_entrada(edad:int,dia_semana:str):
    precio_1:int = 10
    precio_2:int = 5

    if edad >= 12:
        valor=print(f"El precio es de {precio_1}$")
        if dia_semana == "miercoles":
            valor=calcular_descuento(precio_1)
    else:
        valor=print(f"El precio es de {precio_2}$")
        if dia_semana == "miercoles":
            valor=calcular_descuento(precio_2)
    return valor

print(calcular_precio_entrada(12, "miercoles"))
print(calcular_precio_entrada(12, "jueves"))
print(calcular_precio_entrada(10, "miercoles"))
print(calcular_precio_entrada(10, "jueves"))
