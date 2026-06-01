"""
EJERCICIO 01: Calculadora de Ticket de Compra
=============================================
OBJETIVO: Practicar operadores aritméticos, de asignación
          y de comparación en un contexto real.

CONTEXTO:
Eres el programador de una tienda. Debes calcular el ticket
final de un cliente aplicando descuentos e impuestos.

DATOS DE ENTRADA (declara estas variables tal como se indican):
  nombre_cliente     = "Laura M."
  precio_camisa      = 85000      (int, en pesos)
  precio_pantalon    = 120000     (int, en pesos)
  precio_zapatos     = 200000     (int, en pesos)
  porcentaje_iva     = 0.19       (float, 19%)
  porcentaje_descuento = 0.10     (float, 10% de descuento por temporada)

CÁLCULOS QUE DEBES HACER (guarda cada resultado en su variable):
  1. subtotal       → suma de los 3 productos
  2. descuento      → subtotal * porcentaje_descuento
  3. subtotal_con_descuento → subtotal - descuento
  4. valor_iva      → subtotal_con_descuento * porcentaje_iva
  5. total_final    → subtotal_con_descuento + valor_iva
  6. es_compra_grande → True si total_final supera $300.000 (usa un operador de comparación)

SALIDA ESPERADA:
  ============================================
   TICKET DE COMPRA - Laura M.
  ============================================
  Camisa          : $85000
  Pantalón        : $120000
  Zapatos         : $200000
  --------------------------------------------
  Subtotal        : $405000
  Descuento (10%) : $40500.0
  Subtotal c/desc : $364500.0
  IVA (19%)       : $69255.0
  ============================================
  TOTAL FINAL     : $433755.0
  ¿Compra grande? : True
  ============================================

RESTRICCIONES:
  1. Nunca hagas cálculos dentro del print(). Usa tus variables.
  2. Usa operadores de asignación compuesta donde tenga sentido.
     Pista: en vez de escribir subtotal = subtotal - descuento,
     puedes usar subtotal_con_descuento -= descuento. Piénsalo.
  3. El tipo de dato de es_compra_grande DEBE ser bool (usa ==, >, <, etc).
  4. Usa f-strings para la salida (como aprendiste en el ejercicio anterior).

Cuando termines, pega tu código aquí para revisarlo. 💪
"""

# TU CÓDIGO AQUÍ 👇

nombre_cliente:str = "Laura M."
precio_camisa:int = 85000
precio_pantalon:int = 120000
precio_zapatos:int = 200000
porcentaje_iva:float = 0.19
porcentaje_descuento:float = 0.10

subtotal = precio_camisa + precio_pantalon + precio_zapatos
descuento = subtotal * porcentaje_descuento
subtotal_con_descuento = subtotal - descuento
valor_iva = subtotal_con_descuento * porcentaje_iva
total_final = subtotal_con_descuento + valor_iva

es_compra_grande:bool = total_final > 300000

print(f"""
============================================
  TICKET DE COMPRA - {nombre_cliente}
============================================
Camisa          : ${precio_camisa}
Pantalón        : ${precio_pantalon}
Zapatos         : ${precio_zapatos}
--------------------------------------------
Subtotal        : ${subtotal}
Descuento (10%) : ${descuento}
Subtotal c/desc : ${subtotal_con_descuento}
IVA (19%)       : ${valor_iva}
============================================
TOTAL FINAL     : ${total_final}
¿Compra grande? : {es_compra_grande}
============================================
""")
