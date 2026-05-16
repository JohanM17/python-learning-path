"""
EJERCICIO: El Navegador Estelar
---------------------------------------------------------
Consigna:
1. Crea una lista llamada 'estrellas' que contenga tuplas.
   Cada tupla debe representar una estrella con: (nombre, coord_x, coord_y, coord_z).
   Agrega al menos 3 estrellas (ej: "Sirius", "Alpha Centauri", "Proxima").

2. Crea una función 'calcular_distancia_origen' que:
   - Reciba una tupla de estrella.
   - Use UNPACKING para obtener las coordenadas.
   - Calcule la distancia al origen (0,0,0) usando la fórmula: 
     distancia = sqrt(x^2 + y^2 + z^2)
   - Retorne el nombre de la estrella y su distancia.

3. Itera sobre la lista y muestra los resultados con un formato limpio.

REQUISITOS:
- Usa el módulo 'math' para la raíz cuadrada (math.sqrt).
- Usa Type Hints (tuple[str, float, float, float]).
- Sigue estándares PEP8.
"""
import math

# 1. Define tu lista de estrellas
estrellas: list[tuple[str, float, float, float]] = [
    ("Sirius", 1.2, 3.4, 5.6),
    ("Alpha Centauri", -2.0, 4.5, 1.1),
    ("Proxima Centauri", 0.5, -1.2, 8.0)
]

# --- ESCRIBE TU FUNCIÓN Y LÓGICA ABAJO ---
