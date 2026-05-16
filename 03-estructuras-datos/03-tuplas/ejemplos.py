"""
MÓDULO: Estructuras de Datos Avanzadas - Tuplas
FASE 3: Inmutabilidad y Desempaquetado
---------------------------------------------------------
Las tuplas son la forma ideal de agrupar datos relacionados
que no deben ser modificados por accidente.
"""

# =======================================================
# SECCIÓN 1: Creación y el "Error" de Inmutabilidad
# =======================================================

# Definición de una coordenada GPS (Latitud, Longitud)
ubicacion: tuple[float, float] = (4.7110, -74.0721)

print("--- 1. Acceso y Seguridad ---")
print(f"Latitud: {ubicacion[0]}")

# Descomenta la siguiente línea para ver el error:
# ubicacion[0] = 5.0  # TypeError: 'tuple' object does not support item assignment


# =======================================================
# SECCIÓN 2: Desempaquetado (Unpacking)
# =======================================================

# Imagina que una función nos devuelve los datos de un servidor
def obtener_status_servidor() -> tuple[str, int, bool]:
    return ("produccion-01", 8080, True)

# Desempaquetamos los valores en variables individuales
nombre, puerto, esta_activo = obtener_status_servidor()

print("\n--- 2. Unpacking ---")
print(f"Servidor: {nombre} | Puerto: {puerto} | Online: {esta_activo}")

# Tip: Unpacking con el operador "*"
numeros = (1, 2, 3, 4, 5)
primero, *medio, ultimo = numeros
print(f"Primero: {primero}, Medio: {medio}, Último: {ultimo}")


# =======================================================
# SECCIÓN 3: Tuplas como Claves de Diccionarios
# =======================================================
# Las listas NO pueden ser llaves, las tuplas SÍ.

configuracion_pixeles: dict[tuple[int, int], str] = {
    (0, 0): "Rojo",
    (0, 1): "Verde",
    (1, 0): "Azul"
}

print("\n--- 3. Tuplas como Claves ---")
color = configuracion_pixeles.get((0, 1))
print(f"Color en (0,1): {color}")


# =======================================================
# SECCIÓN 4: Métodos Disponibles (Solo 2!)
# =======================================================
# Las tuplas solo tienen dos métodos porque no se pueden modificar.

mi_tupla = (1, 2, 3, 2, 4, 2)

print("\n--- 4. Métodos ---")
print(f"¿Cuántas veces está el 2?: {mi_tupla.count(2)}")
print(f"¿En qué índice está el 4?: {mi_tupla.index(4)}")
