contraseña:str = "python123"

entrada:str = str(input("Ingresa la contraseña secreta:"))

while entrada != contraseña:
    print("Contraseña incorrecta.")
    entrada:str = str(input("Ingresa la contraseña secreta:"))

print("Acceso concedido.")
