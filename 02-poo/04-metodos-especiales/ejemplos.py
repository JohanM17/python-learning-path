"""
MÓDULO: Métodos Especiales (Dunder Methods)
FASE 2: Programación Orientada a Objetos
---------------------------------------------------------
Los Dunder Methods (Double UNDERscore) son métodos que Python
llama AUTOMÁTICAMENTE en situaciones específicas.
Tú los defines, Python los invoca cuando los necesita.
"""

# =======================================================
# SECCIÓN 1: __init__ — El Constructor
# =======================================================
# POR QUÉ EXISTE: Sin él, los objetos nacen vacíos, sin datos.
# PARA QUÉ: Recibir los datos iniciales del objeto al crearlo.
# CUÁNDO LO LLAMA PYTHON: Al hacer MiClase() con paréntesis.

class CuentaBancaria:
    def __init__(self, titular, saldo):
        """
        Python llama esto automáticamente cuando escribes:
        mi_cuenta = CuentaBancaria("Juan", 50000)
        """
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

mi_cuenta = CuentaBancaria("Juan", 50000)

print("--- 1. __init__ (Constructor) ---")
print(f"Titular: {mi_cuenta.titular}")
print(f"Saldo: ${mi_cuenta.saldo}")
mi_cuenta.depositar(10000)
print(f"Saldo tras depósito: ${mi_cuenta.saldo}")


# =======================================================
# SECCIÓN 2: __str__ — La Tarjeta de Presentación
# =======================================================
# POR QUÉ EXISTE: Sin él, print(objeto) muestra la fea dirección de memoria.
# PARA QUÉ: Definir cómo se ve tu objeto cuando alguien lo imprime.
# CUÁNDO LO LLAMA PYTHON: Al hacer print(objeto) o str(objeto).

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        """
        Python llama esto automáticamente cuando escribes:
        print(mi_estudiante)
        Tú decides qué texto muestra.
        """
        estado = "Aprobado ✅" if self.nota >= 3.0 else "Reprobado ❌"
        return f"Estudiante: {self.nombre} | Nota: {self.nota} | Estado: {estado}"

print("\n--- 2. __str__ (Tarjeta de Presentación) ---")
est1 = Estudiante("María", 4.5)
est2 = Estudiante("Pedro", 2.8)

print(est1)  # Python llama __str__ automáticamente
print(est2)


# =======================================================
# SECCIÓN 3: __eq__ — El Comparador
# =======================================================
# POR QUÉ EXISTE: Sin él, == compara direcciones de memoria (siempre False).
# PARA QUÉ: Tú defines QUÉ hace que dos objetos sean "iguales".
# CUÁNDO LO LLAMA PYTHON: Al usar el operador ==.

class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo  # Código único del producto

    def __eq__(self, otro):
        """
        Python llama esto automáticamente cuando escribes:
        producto1 == producto2
        Aquí decidimos: dos productos son iguales si tienen el mismo código.
        """
        return self.codigo == otro.codigo

print("\n--- 3. __eq__ (Comparador) ---")
prod1 = Producto("Coca-Cola 500ml", "COC-001")
prod2 = Producto("Coca-Cola 1L", "COC-001")   # Mismo código, diferente nombre
prod3 = Producto("Pepsi 500ml", "PEP-002")    # Código diferente

print(f"¿prod1 == prod2? {prod1 == prod2}")   # True: mismo código
print(f"¿prod1 == prod3? {prod1 == prod3}")   # False: código diferente


# =======================================================
# SECCIÓN 4: __len__ — El Tamaño
# =======================================================
# POR QUÉ EXISTE: Para que len() funcione con tus objetos personalizados.
# PARA QUÉ: Definir qué significa el "tamaño" de tu objeto.
# CUÁNDO LO LLAMA PYTHON: Al hacer len(objeto).

class Carrito:
    def __init__(self):
        self.items = []  # Lista vacía de productos

    def agregar(self, producto):
        self.items.append(producto)

    def __len__(self):
        """
        Python llama esto automáticamente cuando escribes:
        len(mi_carrito)
        Retornamos cuántos ítems tiene el carrito.
        """
        return len(self.items)

    def __str__(self):
        return f"Carrito con {len(self)} productos"

print("\n--- 4. __len__ (Tamaño) ---")
carrito = Carrito()
carrito.agregar("Leche")
carrito.agregar("Pan")
carrito.agregar("Huevos")

print(carrito)              # Usa __str__
print(f"Items: {len(carrito)}")  # Usa __len__
