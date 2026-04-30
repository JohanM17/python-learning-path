def calcular_precio_entrada(edad: int, dia_semana: str) -> int:
    """Calcula el precio final de la entrada al cine dependiendo de la edad y el día."""
    
    # 1. Calculamos primero el precio base según la edad
    if edad >= 12:
        precio_base = 10
    else:
        precio_base = 5
        
    # 2. Revisamos si aplica el descuento
    # Usamos .lower() por si el usuario escribe "Miercoles" o "MIERCOLES"
    if dia_semana.lower() == "miercoles":
        precio_base = precio_base - 2 
        
    # 3. Retornamos el valor final sin usar prints internos
    return precio_base

# Casos de prueba (Se imprimen afuera, como pedía el ejercicio)
if __name__ == "__main__":
    print(f"12 años, miércoles (debería ser 8): {calcular_precio_entrada(12, 'miercoles')}")
    print(f"12 años, jueves (debería ser 10): {calcular_precio_entrada(12, 'jueves')}")
    print(f"10 años, miércoles (debería ser 3): {calcular_precio_entrada(10, 'miercoles')}")
    print(f"10 años, jueves (debería ser 5): {calcular_precio_entrada(10, 'jueves')}")
