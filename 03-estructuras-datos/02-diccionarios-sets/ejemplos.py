"""
MÓDULO: Estructuras de Datos Avanzadas - Diccionarios y Sets
FASE 3: Manejo de Claves, Valores y Unicidad
---------------------------------------------------------
En este archivo exploramos cómo manipular diccionarios de forma
eficiente y cómo utilizar los sets para manejar datos únicos.
"""

# =======================================================
# SECCIÓN 1: Diccionarios - Acceso y Modificación
# =======================================================

usuario: dict[str, any] = {
    "nombre": "Johan",
    "rol": "Software Engineer",
    "nivel": 5,
    "tecnologias": ["Python", "FastAPI", "SQL"]
}

# 1.1 Acceso Seguro con .get()
# Si la clave no existe, devuelve el valor por defecto en lugar de un KeyError
empresa = usuario.get("empresa", "Freelance")

# 1.2 Actualización
usuario["nivel"] = 6
usuario.update({"activo": True, "idioma": "Español"})

print("--- 1. Diccionarios Básicos ---")
print(f"Usuario: {usuario['nombre']} - Rol: {usuario['rol']}")
print(f"Estado: {empresa}")


# =======================================================
# SECCIÓN 2: Diccionarios - Iteración Avanzada
# =======================================================

precios = {
    "laptop": 1200,
    "mouse": 25,
    "monitor": 300
}

print("\n--- 2. Iteración ---")
# .items() nos da tanto la clave como el valor
for producto, precio in precios.items():
    print(f"Producto: {producto.capitalize():<10} | Precio: ${precio:>5}")


# =======================================================
# SECCIÓN 3: Dictionary Comprehension
# =======================================================
# Al igual que las listas, podemos crear diccionarios en una sola línea.

# Queremos aplicar un 10% de descuento a todos los productos
precios_con_descuento = {k: v * 0.9 for k, v in precios.items()}

print("\n--- 3. Dict Comprehension (Descuento 10%) ---")
print(precios_con_descuento)


# =======================================================
# SECCIÓN 4: Sets (Conjuntos) - Unicidad y Operaciones
# =======================================================

tags_proyecto_a = {"python", "backend", "api"}
tags_proyecto_b = {"javascript", "frontend", "api"}

# 4.1 Unión (Todos los tags sin repetir)
todos_los_tags = tags_proyecto_a | tags_proyecto_b

# 4.2 Intersección (Tags en común)
tags_comunes = tags_proyecto_a & tags_proyecto_b

# 4.3 Diferencia (Tags que están en A pero no en B)
solo_backend = tags_proyecto_a - tags_proyecto_b

print("\n--- 4. Sets (Conjuntos) ---")
print(f"Todos:        {todos_los_tags}")
print(f"En común:     {tags_comunes}")
print(f"Solo Backend: {solo_backend}")

# 4.4 Limpieza de duplicados rápida
lista_sucia = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
lista_limpia = list(set(lista_sucia))
print(f"Lista limpia: {lista_limpia}")
