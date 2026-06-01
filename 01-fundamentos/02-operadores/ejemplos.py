"""
Ejemplos: Operadores en Python
Fase 1 - Tema 2

Lee cada sección, luego abre teoria.md si necesitas refrescar conceptos.
Puedes ejecutar este archivo y ver los resultados en la terminal.
"""

# ─────────────────────────────────────────────
# 1. OPERADORES ARITMÉTICOS
# ─────────────────────────────────────────────
print("=" * 40)
print("  OPERADORES ARITMÉTICOS")
print("=" * 40)

panes = 10
personas = 3

division_real = panes / personas       # Resultado con decimales
division_entera = panes // personas    # Solo la parte entera (sin decimales)
residuo = panes % personas             # Lo que sobra después del reparto
potencia = 2 ** 8                      # 2 elevado a la 8

print(f"Panes: {panes}, Personas: {personas}")
print(f"División real    : {division_real}")      # 3.3333...
print(f"División entera  : {division_entera}")    # 3
print(f"Residuo (módulo) : {residuo}")            # 1
print(f"2 elevado a la 8 : {potencia}")           # 256
print()


# ─────────────────────────────────────────────
# 2. OPERADORES DE ASIGNACIÓN COMPUESTA
# ─────────────────────────────────────────────
print("=" * 40)
print("  OPERADORES DE ASIGNACIÓN")
print("=" * 40)

billetera = 100
print(f"Billetera inicial: ${billetera}")

billetera += 50     # Gané 50
print(f"Después de ganar $50    : ${billetera}")  # 150

billetera -= 30     # Gasté 30
print(f"Después de gastar $30   : ${billetera}")  # 120

billetera *= 2      # Se duplicó (buena inversión!)
print(f"Después de duplicar     : ${billetera}")  # 240

billetera //= 3     # Reparto entre 3 (solo la parte entera)
print(f"Después de repartir en 3: ${billetera}")  # 80
print()


# ─────────────────────────────────────────────
# 3. OPERADORES DE COMPARACIÓN
# ─────────────────────────────────────────────
print("=" * 40)
print("  OPERADORES DE COMPARACIÓN")
print("=" * 40)

mi_edad = 20
edad_minima = 18

# Cada comparación devuelve True o False
es_mayor_de_edad = mi_edad >= edad_minima
es_igual_al_minimo = mi_edad == edad_minima
es_exactamente_20 = mi_edad == 20

print(f"Mi edad: {mi_edad}, Mínimo: {edad_minima}")
print(f"¿Soy mayor de edad?       : {es_mayor_de_edad}")      # True
print(f"¿Tengo exactamente 18?    : {es_igual_al_minimo}")     # False
print(f"¿Tengo exactamente 20?    : {es_exactamente_20}")      # True
print()


# ─────────────────────────────────────────────
# 4. OPERADORES LÓGICOS
# ─────────────────────────────────────────────
print("=" * 40)
print("  OPERADORES LÓGICOS")
print("=" * 40)

# Para ver una película necesito entrada Y ser mayor de edad
tiene_entrada = True
es_mayor = False

puede_entrar_cine = tiene_entrada and es_mayor
print(f"Tiene entrada: {tiene_entrada}, Es mayor: {es_mayor}")
print(f"¿Puede entrar al cine? (and): {puede_entrar_cine}")   # False

# Para entrar al parque me basta con tener invitación O ser socio
tiene_invitacion = False
es_socio = True

puede_entrar_parque = tiene_invitacion or es_socio
print(f"\nTiene invitación: {tiene_invitacion}, Es socio: {es_socio}")
print(f"¿Puede entrar al parque? (or): {puede_entrar_parque}")  # True

# not invierte el valor
esta_lloviendo = True
print(f"\n¿Está lloviendo? : {esta_lloviendo}")
print(f"¿No está lloviendo? (not): {not esta_lloviendo}")       # False
print()


# ─────────────────────────────────────────────
# 5. OPERADORES DE PERTENENCIA
# ─────────────────────────────────────────────
print("=" * 40)
print("  OPERADORES DE PERTENENCIA")
print("=" * 40)

ingredientes = ["harina", "huevo", "leche", "azucar"]
ingrediente_buscado = "huevo"
ingrediente_faltante = "mantequilla"

tiene_huevo = ingrediente_buscado in ingredientes
falta_mantequilla = ingrediente_faltante not in ingredientes

print(f"Lista: {ingredientes}")
print(f"¿Tiene '{ingrediente_buscado}'?        : {tiene_huevo}")        # True
print(f"¿Falta '{ingrediente_faltante}'? : {falta_mantequilla}")  # True
