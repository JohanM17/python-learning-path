"""
EJERCICIO 01 - BÁSICO: Tu Tarjeta de Presentación
==================================================
OBJETIVO: Practicar la creación de variables con los 4 tipos de datos.

INSTRUCCIONES:
Imagina que eres un nuevo empleado en una empresa y debes llenar 
una "tarjeta de presentación digital". Tu tarea es guardar tu 
información en variables y luego mostrarla en pantalla.

DATOS QUE DEBES GUARDAR (usa tus propios datos o inventados):
  - Tu nombre completo          -> tipo: str
  - Tu edad                     -> tipo: int
  - Tu altura en metros         -> tipo: float
  - ¿Tienes experiencia laboral?-> tipo: bool
  - El nombre de tu departamento-> tipo: str
  - Años de experiencia         -> tipo: int

SALIDA ESPERADA (con datos de ejemplo):
  =============================
   TARJETA DE PRESENTACIÓN
  =============================
  Nombre    : María López
  Edad      : 24 años
  Altura    : 1.65 m
  Experiencia: True
  Departamento: Desarrollo
  Años de exp.: 2 años
  =============================

RESTRICCIONES:
  1. Usa nombres de variable en snake_case (ej: nombre_completo)
  2. No uses números mágicos: guarda TODO en variables primero.
  3. ¡Escríbelo tú mismo, no copies los ejemplos!

Cuando termines, comparte tu código aquí para revisarlo juntos.
"""

# TU CÓDIGO AQUÍ 👇

nombre_completo: str = "Johan Felipe Molina Aguirre"
edad: int = 19
altura_metros: float = 1.77
experiencia_laboral: bool = True
departamento: str = "Desarrollo"
años_experiencia: int = 2

print(f"""
  TARJETA DE PRESENTACIÓN
  Nombre    : {nombre_completo}
  Edad      : {edad} años
  Altura    : {altura_metros} m
  Experiencia: {experiencia_laboral}
  Departamento: {departamento}
  Años de exp.: {años_experiencia} años
  """)