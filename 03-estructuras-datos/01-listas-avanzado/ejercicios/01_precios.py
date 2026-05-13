"""
EJERCICIO: El Analista de Precios (List Comprehension)
---------------------------------------------------------
Consigna:
1. Lista base: precios_brutos = [1200, 2500, 800, 4500, 1500, 3200, 600, 5000]
2. Crear 'precios_con_iva' (precio * 1.19).
3. Crear 'solo_caros' (precios con IVA > 3000).
4. Crear 'etiquetas' ("Lujo" si > 4000, "Estandar" si no).

Escribe tu solución usando List Comprehension.
"""

precio_brutos:list = [1200, 2500, 800, 4500, 1500, 3200, 600, 5000]

precios_con_iva:list = [n*1.19 for n in precio_brutos]

solo_caros:list = [n for n in precios_con_iva if n > 3000]

etiquetas:list = ["Lujo" if n > 4000 else "Estandar" for n in precios_con_iva]
