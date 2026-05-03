# ==========================================
# FASE 2: PROGRAMACIÓN ORIENTADA A OBJETOS
# TEMA: Clases y Objetos
# ==========================================

"""
TEORÍA BREVE:
- Clase: Es el molde o plano (ej: plano de una casa).
- Objeto: Es la instancia real creada (ej: la casa construida).
- self: Es una variable que representa al objeto mismo. Es obligatorio como primer parámetro.
- __init__: Es el método "Constructor". Se ejecuta automáticamente al crear el objeto.
"""

# Definición de la Clase
class Celular:
    def __init__(self, marca: str, modelo: str, bateria: int):
        # Atributos (Características)
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.esta_encendido = False

    # Métodos (Acciones que el objeto puede realizar)
    def encender(self):
        self.esta_encendido = True
        print(f"✅ El {self.marca} {self.modelo} se está encendiendo...")

    def tomar_foto(self):
        if self.esta_encendido:
            print(f"📸 ¡Click! Foto tomada con el {self.modelo}!")
        else:
            print(f"❌ Error: El {self.modelo} está apagado. Enciéndelo primero.")

# --- Creación de Objetos (Instancias) ---
print("--- INICIANDO SIMULACIÓN DE CELULARES ---")

# Creamos dos objetos distintos a partir de la misma clase
mi_cel = Celular("Samsung", "S23 Ultra", 95)
tu_cel = Celular("Apple", "iPhone 15 Pro", 80)

# Cada objeto es independiente
print(f"Mi celular es un {mi_cel.marca}")
mi_cel.encender()
mi_cel.tomar_foto()

print("-" * 30)

print(f"Tu celular es un {tu_cel.marca}")
tu_cel.tomar_foto() # Esto mostrará el error porque no lo hemos encendido
