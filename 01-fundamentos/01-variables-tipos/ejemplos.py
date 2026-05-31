"""
Ejemplos de Variables y Tipos de Datos
Fase 1 - Tema 1
"""

# 1. Variables y Enteros (int)
cajas_mudanza = 15
libros_por_caja = 20
total_libros = cajas_mudanza * libros_por_caja

print("--- ENTEROS ---")
print("Total de cajas:", cajas_mudanza)
print("Total de libros:", total_libros)
print("Tipo de dato de 'cajas_mudanza':", type(cajas_mudanza))
print()

# 2. Flotantes (float)
peso_caja_kg = 12.5
altura_metro = 1.75

print("--- FLOTANTES ---")
print("El peso de la caja es:", peso_caja_kg, "kg")
print("Tipo de dato de 'peso_caja_kg':", type(peso_caja_kg))
print()

# 3. Cadenas de Texto (str)
nombre_cliente = "Ana Gómez"
direccion = 'Av. Siempre Viva 123'

print("--- TEXTO (STRINGS) ---")
print("Cliente:", nombre_cliente)
print("Dirección:", direccion)
print("Tipo de dato de 'nombre_cliente':", type(nombre_cliente))
print()

# 4. Booleanos (bool)
es_fragil = True
envio_express = False

print("--- BOOLEANOS ---")
print("¿La caja es frágil?:", es_fragil)
print("Tipo de dato de 'es_fragil':", type(es_fragil))
print()

# 5. Reasignación de Variables (Tipado Dinámico)
# Python permite cambiar el tipo de dato que guarda una variable,
# aunque no siempre es buena práctica.
variable_misteriosa = "Soy un texto"
print("Variable misteriosa (texto):", variable_misteriosa)

variable_misteriosa = 100
print("Variable misteriosa (ahora es número):", variable_misteriosa)
