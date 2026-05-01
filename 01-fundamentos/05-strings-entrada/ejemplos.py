# ==========================================
# EJEMPLOS: STRINGS Y ENTRADAS DE USUARIO
# ==========================================

print("--- 1. ENTRADA DE DATOS (input) ---")
# input() SIEMPRE captura lo que el usuario escribe como Texto (String)
nombre = input("Por favor, ingresa tu nombre: ")

# Si queremos pedir un número para hacer matemáticas, debemos convertirlo (Casteo)
edad_texto = input("¿Cuántos años tienes? ")
edad = int(edad_texto)  # Convertimos el texto "25" al número 25

print("\n--- 2. FORMATO DE STRINGS (f-strings) ---")
# Las f-strings (format strings) permiten inyectar variables directamente en el texto
# Solo necesitas poner una 'f' antes de las comillas
mensaje = f"Hola {nombre}, el próximo año tendrás {edad + 1} años."
print(mensaje)

print("\n--- 3. MÉTODOS ÚTILES PARA MANIPULAR TEXTO ---")
# Los strings tienen "poderes" (métodos) integrados
texto_ejemplo = "   python es INCREÍBLE   "
print(f"Original: '{texto_ejemplo}'")

# .strip() -> Quita los espacios vacíos al inicio y al final (muy útil para inputs)
texto_limpio = texto_ejemplo.strip()
print(f"Con .strip(): '{texto_limpio}'")

# .upper(), .lower(), .title() -> Cambian mayúsculas y minúsculas
print(f"Con .upper(): {texto_limpio.upper()}")
print(f"Con .title(): {texto_limpio.title()}")

# .replace() -> Cambia una palabra por otra
texto_nuevo = texto_limpio.replace("INCREÍBLE", "genial")
print(f"Con .replace(): {texto_nuevo}")

print("\n--- 4. FORMATO AVANZADO CON NÚMEROS ---")
precio = 19.99999
# Podemos redondear números dentro del mismo f-string usando :.2f (2 decimales)
print(f"El precio es: ${precio:.2f}")
