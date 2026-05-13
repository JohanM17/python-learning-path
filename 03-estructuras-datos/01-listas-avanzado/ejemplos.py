"""
MÓDULO: Estructuras de Datos Avanzadas - Listas
FASE 3: List Comprehension y Manipulación
---------------------------------------------------------
La "List Comprehension" es una de las herramientas más potentes
de Python. Permite crear listas nuevas a partir de otras de
forma compacta y eficiente.
"""

# =======================================================
# SECCIÓN 1: List Comprehension Básica
# =======================================================
# SINTAXIS: [expresion for item in iterable]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Queremos el doble de cada número
dobles = [n * 2 for n in numeros]

print("--- 1. List Comprehension Básica ---")
print(f"Original: {numeros}")
print(f"Dobles:   {dobles}")


# =======================================================
# SECCIÓN 2: Filtrado con IF
# =======================================================
# SINTAXIS: [expresion for item in iterable if condicion]

# Queremos solo los números pares
pares = [n for n in numeros if n % 2 == 0]

# Queremos los cuadrados de los números mayores a 5
cuadrados_grandes = [n**2 for n in numeros if n > 5]

print("\n--- 2. Filtrado con IF ---")
print(f"Solo pares:        {pares}")
print(f"Cuadrados (>5):   {cuadrados_grandes}")


# =======================================================
# SECCIÓN 3: Transformación con IF / ELSE
# =======================================================
# SINTAXIS: [expresion_if if condicion else expresion_else for item in iterable]

# Queremos clasificar: "Par" o "Impar"
clasificacion = ["Par" if n % 2 == 0 else "Impar" for n in numeros]

print("\n--- 3. Transformación con IF/ELSE ---")
print(f"Clasificación: {clasificacion[:5]}...") # Mostramos los primeros 5


# =======================================================
# SECCIÓN 4: Manipulación de Strings
# =======================================================
nombres = ["ana", "pedro", "MARIA", "juan", "  luis  "]

# Limpiar espacios y poner en Mayúscula la primera letra
nombres_limpios = [n.strip().capitalize() for n in nombres]

print("\n--- 4. Manipulación de Strings ---")
print(f"Originales: {nombres}")
print(f"Limpios:    {nombres_limpios}")


# =======================================================
# SECCIÓN 5: Listas Anidadas (Aplanado)
# =======================================================
matriz = [[1, 2], [3, 4], [5, 6]]

# Convertir matriz en una sola lista: [1, 2, 3, 4, 5, 6]
aplanada = [num for fila in matriz for num in fila]

print("\n--- 5. Aplanado de Listas ---")
print(f"Matriz:   {matriz}")
print(f"Aplanada: {aplanada}")
