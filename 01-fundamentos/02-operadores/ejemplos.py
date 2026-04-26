# --- Operadores Aritméticos ---
panes = 10
personas = 3

reparto = panes / personas    # 3.3333...
reparto_entero = panes // personas # 3 (solo la parte entera)
sobra = panes % personas      # 1 (el residuo que queda)


# --- Operadores de Comparación ---
mi_edad = 20
edad_minima = 18

puedo_entrar = mi_edad >= edad_minima # True
es_igual = (10 == 10)                 # True
es_diferente = (10 != 5)              # True


# --- Operadores Lógicos ---
sol_brilla = True
hay_playa = False

# Solo salgo si el sol brilla Y hay playa
salida_playa = sol_brilla and hay_playa # False

# Salgo si hay playa O el sol brilla (es más flexible)
salida_ciudad = hay_playa or sol_brilla # True

# Si no hay sol, mejor me quedo adentro
si_no_sol = not sol_brilla           # False


# --- Operadores de Asignación ---
cafe = 5
# Me lo tomo
cafecito = cafe - 3      # 2

# Una forma más rápida de escribir: cafe - 3
cafecito -= 3             # 2
cafecito += 1             # 3
cafecito *= 2             # 6
cafecito /= 3             # 2.0


# --- Operadores de Pertenencia (Membership) ---
frutas = ["manzana", "banana", "cereza"]

# ¿Está "banana" en la lista?
esta_en_lista = "banana" in frutas  # True

# ¿Está "uva" en la lista?
no_esta = "uva" not in frutas       # True


# --- Operadores de Identidad ---
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# ¿Son la misma lista en memoria?
identico_ab = a is b  # False (son dos listas diferentes)
identico_ac = a is c  # True (c es una copia de la referencia de a)
