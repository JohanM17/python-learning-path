contraseña: str = "python123"

entrada: str = input("Ingresa la contraseña secreta: ")

while entrada != contraseña:
    print("Contraseña incorrecta.")
    entrada = input("Ingresa la contraseña secreta: ")

# El print de éxito debe ir fuera del bucle (sin indentación)
# Así solo se ejecutará cuando el bucle while haya terminado (es decir, cuando la contraseña sea correcta).
print("Acceso concedido.")
