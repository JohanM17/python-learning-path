"""
🚀 PROYECTO INTEGRADOR - FASE 2: POO
Sistema de Gestión de Flota Logística
---------------------------------------------------------

CONSIGNA:
1. Clase Base 'Vehiculo':
   - __init__(self, patente, marca, modelo)
   - __str__ -> Debe retornar: "Marca Modelo (Patente)"
   - __eq__  -> Dos vehículos son iguales si tienen la misma patente.
   - calcular_autonomia() -> Retorna 0.

2. Herencia:
   - 'Camion': Agrega atributo 'capacidad_carga'. autonomia = 500.
   - 'AutoElectrico': Agrega atributo 'nivel_bateria'. autonomia = bateria * 5.
   - 'Motocicleta': Agrega atributo 'cilindrada'. autonomia = 200.

3. Clase 'GestionFlota':
   - Atributo: lista de vehículos.
   - agregar_vehiculo(v) -> añade a la lista.
   - __len__ -> retorna cantidad de vehículos.
   - reporte_autonomias() -> (POLIMORFISMO) recorre la lista e imprime
     la autonomía de cada vehículo usando el método calcular_autonomia().

4. Pruebas:
   - Crea un objeto de cada tipo.
   - Agrégalos a la flota.
   - Imprime el len() de la flota.
   - Ejecuta el reporte.
"""

class Vehiculo:
    def __init__(self, patente:int, marca:str, modelo:int):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca}{self.modelo}{self.patente}"

    def __eq__(self, otro):
        return self.patente == otro.patente

    def calcular_autonomia(self):
        return 0

class Camion(Vehiculo):
    def __init__(self, patente, marca, modelo, capacidad_carga:int):
        super().__init__(patente, marca, modelo)
        self.capacidad_carga = capacidad_carga
    
    def calcular_autonomia(self):
        return 500

class AutoElectrico(Vehiculo):
    def __init__(self, patente, marca, modelo, nivel_bateria:int):
        super().__init__(patente, marca, modelo)
        self.nivel_bateria = nivel_bateria

    def calcular_autonomia(self):
        return self.nivel_bateria*5

class Motocicleta(Vehiculo):
    def __init__(self, patente, marca, modelo, cilindrada:int):
        super().__init__(patente, marca, modelo)
        self.cilindrada = cilindrada

    def calcular_autonomia(self):
        return 200


class GestionFlota:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, Vehiculo):
        self.vehiculos.append(Vehiculo)

    def __len__(self):
        return len(self.vehiculos)

    def reporte(self):
        for v in self.vehiculos:
            distancia = v.calcular_autonomia()

            print(f"Vehiculo: {v}, autonomia: {distancia} km")
    

# --- SECCIÓN DE PRUEBAS ---
flota = GestionFlota()

# 1. Creamos los vehículos
c = Camion("ABC-123", "Volvo", 2023, 15)
a = AutoElectrico("ELE-555", "Tesla", 2024, 80)
m = Motocicleta("MOT-999", "Yamaha", 2022, 600)

# 2. Los agregamos
flota.agregar_vehiculo(c)
flota.agregar_vehiculo(a)
flota.agregar_vehiculo(m)

# 3. Verificamos
print(f"Total vehículos en flota: {len(flota)}")
flota.reporte()
