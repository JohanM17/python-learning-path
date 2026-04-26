precio_base:float = 150.0
es_cliente_fiel:bool = True
codigo_promocion:bool = False
descuento_hoy:float = 0.90

precio_base = precio_base * descuento_hoy

descuento_extra:bool = True if es_cliente_fiel is True or codigo_promocion is True else False

es_ganga:bool = True if precio_base < 100 else False

print(f"El precio final es {precio_base}")
print(f"Tiene descuento extra?: {descuento_extra}")
print(f"¿Es una ganga?: {es_ganga}")
