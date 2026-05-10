"""
EJERCICIO: La Orquesta Polimórfica
---------------------------------------------------------
Consigna:
1. Crea las clases Guitarra, Piano y Bateria.
2. Implementa el método tocar() en cada una con un mensaje único.
3. Crea la función iniciar_concierto(lista_instrumentos).
4. (Opcional) Aplica Duck Typing con una clase Director.

Escribe tu código debajo de este comentario.
"""

# --- Tu código aquí ---

class Guitarra:
    def tocar(self):
        print("La guitarra suena trin")

class Piano:
    def tocar(self):
        print("El piano suena drun drun")

class Bateria:
    def tocar(self):
        print("La bateria suena bom bom")

def iniciar_concierto(lista_instrumentos):
    for i in lista_instrumentos:
        i.tocar()


mi_guitarra = Guitarra()
mi_piano = Piano()
mi_bateria = Bateria()

orquesta: list = [mi_guitarra, mi_piano, mi_bateria]

iniciar_concierto(orquesta)
