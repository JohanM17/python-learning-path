# Así se declaran variables en Python
nombre = "Johan"          # Esto es un String (str)
edad = 20                # Esto es un Integer (int)
estatura = 1.75          # Esto es un Float (float)
es_estudiante = True     # Esto es un Boolean (bool)

# Podemos imprimir los valores y sus tipos
print(f"Hola, mi nombre es {nombre}")
print(f"Tipo de dato de 'edad': {type(edad)}")

# Las variables pueden cambiar de valor (por eso se llaman variables)
puntos = 10
puntos = puntos + 5      # Ahora puntos vale 15


# Adicional, python permite escribir variables con tipado estricto o dinamico
# La manera dinamica es la que acabamos de ver
# La manera estricta es la siguiente:

numero: int = 10
numero = numero + 5      # Ahora numero vale 15
numero = "texto"         # Esto daria error en tipado estricto, sin embargo en python no es obligatorio el tipado estricto

# No obstante, a pesar de que python sea un lenguaje de tipado dinamico, es buena practica usar tipado estricto para evitar errores