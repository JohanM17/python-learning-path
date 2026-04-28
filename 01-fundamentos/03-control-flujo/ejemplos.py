edad = 17

if edad >= 18:
    print("Eres mayor de edad, puedes pasar.")
    # Todo lo que tenga este espacio a la izquierda está DENTRO del if
elif edad == 17:
    print("Casi puedes entrar, vuelve en un año.")
else:
    print("Eres menor, no puedes pasar.")

# Este print ya no tiene espacios, por lo tanto se ejecuta SIEMPRE
print("Fin de la validación.")
