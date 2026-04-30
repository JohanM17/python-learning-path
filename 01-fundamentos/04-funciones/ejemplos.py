# ==========================================
# EJEMPLOS: FUNCIONES EN PYTHON
# ==========================================

# 1. FUNCIÓN BÁSICA (Sin parámetros, sin retorno)
def saludar():
    """Función simple que no recibe parámetros y no retorna nada."""
    print("¡Hola! Bienvenido al tema de funciones.")

# 2. FUNCIÓN CON PARÁMETROS (Input)
def saludar_por_nombre(nombre):
    """Función que recibe un parámetro y lo usa dentro."""
    print(f"¡Hola, {nombre}! Qué bueno verte.")

# 3. FUNCIÓN CON RETORNO (Output)
def sumar(a, b):
    """Función que recibe dos parámetros y RETORNA un valor."""
    resultado = a + b
    return resultado

# 4. FUNCIÓN CON PARÁMETROS POR DEFECTO (Opcionales)
def preparar_cafe(tipo="negro"):
    """Si no le pasamos el parámetro 'tipo', usará 'negro' por defecto."""
    print(f"Preparando un delicioso café {tipo} ☕")

# 5. FUNCIÓN QUE RETORNA MÚLTIPLES VALORES
def obtener_datos_usuario():
    """Retorna varios valores al mismo tiempo."""
    nombre = "Ana"
    edad = 25
    return nombre, edad


# ==========================================
# CÓMO LLAMAR (EJECUTAR) ESTAS FUNCIONES
# ==========================================

print("--- 1 y 2. FUNCIONES BÁSICAS ---")
saludar()
saludar_por_nombre("Johan")

print("\n--- 3. FUNCIÓN CON RETORNO ---")
total = sumar(5, 3)
print(f"El resultado de la suma es: {total}")

print("\n--- 4. PARÁMETROS POR DEFECTO ---")
# Si no le paso nada, usa "negro"
preparar_cafe()          
# Si le paso algo, ignora "negro" y usa lo que le paso
preparar_cafe("capuchino") 

print("\n--- 5. RETORNANDO MÚLTIPLES VALORES ---")
# Python permite guardar cada valor retornado en una variable diferente (se llama desempaquetado)
nombre_usuario, edad_usuario = obtener_datos_usuario()
print(f"Usuario: {nombre_usuario}, Edad: {edad_usuario}")

print("\n--- 6. ARGUMENTOS NOMBRADOS (Keyword arguments) ---")
# Puedes enviar los datos en desorden siempre y cuando le digas a Python qué parámetro es cuál
total_suma = sumar(b=10, a=20) 
print(f"Suma con argumentos nombrados (a=20, b=10): {total_suma}")
