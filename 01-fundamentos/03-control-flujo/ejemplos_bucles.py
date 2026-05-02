# ==========================================
# EJEMPLOS DE BUCLES: for y while
# ==========================================

print("--- EJEMPLO 1: Bucle while (Mientras) ---")
# Un contador regresivo usando while
contador = 5
while contador > 0:
    print(f"El contador va en: {contador}")
    # ¡Importante! Siempre debemos modificar la variable para no crear un bucle infinito
    contador -= 1  # Esto es igual a: contador = contador - 1
print("¡Despegue! 🚀\n")


print("--- EJEMPLO 2: Bucle for con rango de números ---")
# La función range(5) genera los números del 0 al 4.
for i in range(5):
    print(f"Vuelta número {i}")
print("Terminó el bucle for con range\n")


print("--- EJEMPLO 3: Bucle for con strings (texto) ---")
# El bucle for pasará letra por letra por la palabra
palabra = "Python"
for letra in palabra:
    print(f"Dame una: {letra}!")
print("¡Terminó el bucle for con string!\n")


print("--- EJEMPLO 4: Combinando bucles y condicionales (Extra) ---")
# Contando solo los números pares del 1 al 10
for numero in range(1, 11):  # Empieza en 1, termina en 10 (el 11 no se incluye)
    if numero % 2 == 0:      # Si el resto de dividir por 2 es 0, es par
        print(f"El número {numero} es par.")
