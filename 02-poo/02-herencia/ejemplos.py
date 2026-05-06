# ==========================================
# FASE 2: PROGRAMACIÓN ORIENTADA A OBJETOS
# TEMA: Herencia (Inheritance)
# ==========================================

"""
TEORÍA BREVE:
- Herencia: Permite crear una clase nueva basada en otra clase ya existente.
- Clase Padre (Base): Es la clase original (ej: Personaje).
- Clase Hijo (Derivada): Es la clase que "hereda" las características del padre pero puede añadir las suyas propias (ej: Mago).
- super(): Es una función especial que nos permite llamar a los métodos de la clase padre desde la clase hijo.
"""

# 1. Definimos la Clase Padre (Base)
class Personaje:
    def __init__(self, nombre: str, fuerza: int):
        self.nombre = nombre
        self.fuerza = fuerza
        self.vida = 100

    def presentarse(self):
        print(f"🛡️ Hola, soy {self.nombre} y mi fuerza es {self.fuerza}.")

# 2. Definimos la Clase Hijo (Derivada)
# Ponemos la clase padre entre paréntesis () para indicar la herencia
class Mago(Personaje):
    def __init__(self, nombre: str, fuerza: int, mana: int):
        # super().__init__ llama al constructor del Padre
        # Así no tenemos que repetir self.nombre = nombre, etc.
        super().__init__(nombre, fuerza)
        
        # Atributo único de la clase Mago
        self.mana = mana

    # Método único de la clase Mago
    def lanzar_hechizo(self):
        if self.mana >= 10:
            print(f"🔮 ¡{self.nombre} lanza una Bola de Fuego!")
            self.mana -= 10
        else:
            print("❌ No tienes maná suficiente.")

# --- PROBANDO LA HERENCIA ---
print("--- INICIANDO AVENTURA ---")

# Creamos un objeto de la clase Mago
gandalf = Mago("Gandalf el Gris", 10, 50)

# ¡Fíjate! Gandalf puede usar 'presentarse' aunque no esté definido dentro de Mago.
# Lo puede usar porque lo HEREDÓ de Personaje.
gandalf.presentarse()

# Y también puede usar sus habilidades de Mago
gandalf.lanzar_hechizo()
print(f"Maná restante de Gandalf: {gandalf.mana}")
