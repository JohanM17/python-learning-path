"""
EJERCICIO: El Gestor de Inventario Inteligente
---------------------------------------------------------
Consigna:
1. Crea un diccionario 'precios_productos' con al menos 5 productos y sus precios.
2. Tienes la siguiente lista de ventas del día:
   ventas_dia = ["laptop", "mouse", "laptop", "teclado", "mouse", "mouse", "monitor"]

3. Tu objetivo es:
   a) Crear un diccionario 'conteo_ventas' que cuente cuántas unidades se vendieron de cada producto.
   b) Calcular el 'ingreso_total' sumando los precios de cada producto vendido.
   c) Crear un set 'productos_vendidos' con los nombres de los productos que tuvieron al menos una venta.

REQUISITOS:
- Usa Type Hints.
- Implementa una función para calcular el total.
- Sigue estándares PEP8.
"""

# 1. Define tu diccionario de precios
precios_productos: dict[str, float] = {
    "laptop": 1500.0,
    "mouse": 25.0,
    "teclado": 45.0,
    "monitor": 300.0,
    "headset": 80.0
}

# 2. Lista de ventas
ventas_dia: list[str] = ["laptop", "mouse", "laptop", "teclado", "mouse", "mouse", "monitor"]

# --- ESCRIBE TU SOLUCIÓN ABAJO ---
