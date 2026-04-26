# --- SOLUCIÓN MAESTRA: Operadores ---

precio_base: float = 150.0
es_cliente_fiel: bool = True
codigo_promocion: bool = False

# 1. Uso de asignación compuesta (más limpio)
precio_base *= 0.90  # Equivale a: precio_base = precio_base * 0.90

# 2. Simplificación Lógica
# No necesitas el "True if ... else False" porque el operador 'or' 
# ya devuelve un valor Booleano por defecto.
# Tampoco necesitas "is True" porque la variable ya contiene esa verdad.
descuento_extra = es_cliente_fiel or codigo_promocion

# 3. Simplificación de Comparación
# La comparación 'precio_base < 100' ya es, por sí misma, un True o un False.
# Guardar el resultado directamente es lo más eficiente en Python.
es_ganga = precio_base < 100

print(f"El precio final es: {precio_base}")
print(f"¿Tiene descuento extra? {descuento_extra}")
print(f"¿Es una ganga? {es_ganga}")

# NOTA DEL PROFESOR: 
# Tu solución funcionaba perfecto, pero en Python buscamos siempre 
# la "Legibilidad". Menos palabras para decir lo mismo suele ser mejor.
