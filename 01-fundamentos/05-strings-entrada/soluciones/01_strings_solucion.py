def generar_carnet(nombre: str, carrera: str, costo: float) -> str:
    """Recibe datos del estudiante, los limpia y genera un carnet."""
    # 1. Limpiamos los datos
    nombre_limpio = nombre.strip().upper()
    carrera_limpia = carrera.strip().title()
    
    # 2. Construimos el carnet usando f-strings multilínea
    carnet = f"""
    ======================
    Universidad Colombiana
    ======================
    Nombre: {nombre_limpio}
    Carrera: {carrera_limpia}
    Costo: ${costo:.2f}
    ======================
    """
    
    # 3. Retornamos el resultado
    return carnet

if __name__ == "__main__":
    # PEDIMOS LOS DATOS AFUERA DE LA FUNCIÓN
    # Podemos poner el texto directamente dentro de la función input()
    nombre_usuario = input("Ingresa tu nombre: ")
    carrera_usuario = input("Ingresa tu carrera: ")
    costo_usuario = float(input("Ingresa el costo de matrícula (solo números): "))

    # LLAMAMOS A LA FUNCIÓN PASÁNDOLE LOS DATOS QUE RECIÉN PEDIMOS
    resultado = generar_carnet(nombre_usuario, carrera_usuario, costo_usuario)
    
    # IMPRIMIMOS EL RESULTADO FINAL
    print(resultado)
