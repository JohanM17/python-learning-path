class Personaje:
    def __init__(self, nombre: str, fuerza: int, vida: int = 100):
        self.nombre = nombre
        self.fuerza = fuerza
        self.vida = vida

    def presentarse(self):
        print(f"Hola soy {self.nombre} y mi fuerza es {self.fuerza}")

    def recibir_daño(self, cantidad_daño: int):
        self.vida -= cantidad_daño
        if self.vida < 0:
            print("He sido derrotado")
        else:
            print(f"Me quedan {self.vida} puntos de vida")

personaje1 = Personaje("Superman", 90)
personaje2 = Personaje("Batman", 70)

personaje1.presentarse()
personaje2.presentarse()

personaje2.recibir_daño(50)
