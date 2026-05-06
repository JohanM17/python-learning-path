# Clase padre
class Animal:
    def __init__(self, nombre: str, especie: str):
        self.nombre = nombre
        self.especie = especie

    def hacer_sonido(self):
        print("Este animal hace un sonido genérico.")

# Clase hija
class Perro(Animal):
    def __init__(self, nombre: str, raza: str):
        # Pasamos el nombre y definimos la especie como "Canino"
        super().__init__(nombre, especie="Canino")
        self.raza = raza

    def hacer_sonido(self):
        print("¡Guau guau!")

# Clase hija
class Gato(Animal):
    def __init__(self, nombre: str, color: str):
        # ERROR CORREGIDO: Ahora pasamos nombre Y especie
        super().__init__(nombre, especie="Felino")
        self.color = color
    
    def hacer_sonido(self):
        print("¡Miau!")

# Pruebas
if __name__ == "__main__":
    pertulfio = Gato("Pertulfio", "Blanco")
    max_dog = Perro("Max", "Pastor Aleman")

    print(f"{pertulfio.nombre} es un {pertulfio.especie}:")
    pertulfio.hacer_sonido()

    print(f"{max_dog.nombre} es un {max_dog.especie}:")
    max_dog.hacer_sonido()
