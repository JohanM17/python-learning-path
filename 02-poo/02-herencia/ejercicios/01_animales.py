#Clase padre
class Animal:
    def __init__(self,nombre:str,especie:str):
        self.nombre = nombre
        self.especie = especie

    def hacer_sonido(self):
        print("Este animal hace un sonido genérico.")

#Clase hija
class Perro(Animal):
    def __init__(self,nombre:str, raza:str):
        super().__init__(nombre, especie="canino")
        self.raza = raza

    def hacer_sonido(self):
        print("Guau guau")

#Clase hija
class Gato(Animal):
    def __init__(self, nombre:str, color:str):
        super().__init__(nombre, especie="felino") #Correccion de pasarle especie de la clase padre
        self.color = color
    
    def hacer_sonido(self):
        print("Miau")

pertulfio = Gato("Pertulfio", "Blanco")
max = Perro("Max", "Pastor Aleman")

pertulfio.hacer_sonido()
max.hacer_sonido()
