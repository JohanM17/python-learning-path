"""
MÓDULO: Polimorfismo y Duck Typing
FASE 2: Programación Orientada a Objetos
---------------------------------------------------------
En este archivo exploramos las dos formas de polimorfismo en Python:
1. Polimorfismo por Herencia (Sobrescritura de métodos).
2. Duck Typing (Polimorfismo por comportamiento).
"""

# =======================================================
# SECCIÓN 1: POLIMORFISMO POR HERENCIA
# =======================================================
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_pago(self):
        """Método base que será sobrescrito"""
        pass

class Programador(Empleado):
    def calcular_pago(self):
        # El programador recibe un bono por líneas de código (ejemplo simple)
        bono = 500
        return self.salario_base + bono

class Gerente(Empleado):
    def calcular_pago(self):
        # El gerente recibe un bono del 20%
        return self.salario_base * 1.20

# Demostración
print("--- 1. Polimorfismo por Herencia ---")
empleados = [Programador("Juan", 2000), Gerente("Ana", 3000)]

for emp in empleados:
    # Tratamos a todos como 'Empleado', pero cada uno calcula su pago distinto
    print(f"Empleado: {emp.nombre} | Pago total: ${emp.calcular_pago():.2f}")


# =======================================================
# SECCIÓN 2: DUCK TYPING (EL "ESTILO PYTHON")
# =======================================================
class NotificadorEmail:
    def enviar(self, mensaje):
        print(f"📧 Enviando Email: {mensaje}")

class NotificadorSMS:
    def enviar(self, mensaje):
        print(f"📱 Enviando SMS: {mensaje}")

class NotificadorWhatsApp:
    def enviar(self, mensaje):
        print(f"🟢 Enviando WhatsApp: {mensaje}")

def difundir_alerta(notificador, mensaje):
    """
    Esta función no sabe qué tipo de notificador es. 
    Solo confía en que tiene el método .enviar()
    """
    notificador.enviar(mensaje)

print("\n--- 2. Duck Typing (Sin Herencia) ---")
# Creamos una lista de objetos que NO tienen un padre común
servicios = [NotificadorEmail(), NotificadorSMS(), NotificadorWhatsApp()]

for servicio in servicios:
    difundir_alerta(servicio, "¡La base de datos ha caído!")


# =======================================================
# SECCIÓN 3: POLIMORFISMO EN FUNCIONES INTEGRADAS
# =======================================================
# El método len() es polimórfico por naturaleza en Python
print("\n--- 3. Polimorfismo en len() ---")
print(f"Longitud de string: {len('Python')}")
print(f"Longitud de lista:  {len([1, 2, 3, 4])}")
print(f"Longitud de dict:   {len({'a': 1, 'b': 2})}")
