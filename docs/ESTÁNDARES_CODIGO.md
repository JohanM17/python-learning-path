# 📝 Estándares de Código - python-learning-path

Todos los códigos en este repositorio deben seguir estas reglas. No es opcional, es parte de aprender buenas prácticas profesionales desde el inicio.

---

## 1️⃣ NOMENCLATURA (Naming Conventions)

### Variables y Funciones: `snake_case`

```python
# ✅ CORRECTO
nombre_usuario = "Juan"
edad_promedio = 25
calcular_total()
obtener_lista_usuarios()

# ❌ INCORRECTO
nombreUsuario = "Juan"
edadPromedio = 25
CalcularTotal()
obtenerListaUsuarios()
```

### Clases: `PascalCase`

```python
# ✅ CORRECTO
class UsuarioPremium:
    pass

class GestorBaseDatos:
    pass

# ❌ INCORRECTO
class usuario_premium:
    pass

class gestor_base_datos:
    pass
```

### Constantes: `UPPER_SNAKE_CASE`

```python
# ✅ CORRECTO
EDAD_MINIMA = 18
RUTA_ARCHIVO = "/home/usuario/datos.txt"
TIMEOUT_CONEXION = 30

# ❌ INCORRECTO
edadMinima = 18
RutaArchivo = "/home/usuario/datos.txt"
timeout_conexion = 30
```

### Módulos/Archivos: `snake_case.py`

```
✅ CORRECTO:
- utils.py
- gestor_usuarios.py
- calculos_estadisticos.py

❌ INCORRECTO:
- Utils.py
- GestorUsuarios.py
- CalculosEstadisticos.py
```

---

## 2️⃣ FORMATO (PEP8)

### Indentación: 4 espacios (NUNCA tabs)

```python
# ✅ CORRECTO
def saludar():
    nombre = "Juan"
    if nombre:
        print(f"Hola {nombre}")

# ❌ INCORRECTO
def saludar():
  nombre = "Juan"  # 2 espacios
  if nombre:
    print(f"Hola {nombre}")  # tabs
```

### Longitud de línea: Máximo 79-88 caracteres

```python
# ✅ CORRECTO - Se rompe en líneas lógicas
resultado = calcular_algo(parametro1, parametro2,
                         parametro3, parametro4)

# ✅ CORRECTO - Se usa paréntesis
mensaje = (
    "Este es un mensaje muy largo que necesita "
    "múltiples líneas para mantener legibilidad"
)

# ❌ INCORRECTO - Línea muy larga
resultado = calcular_algo(parametro1, parametro2, parametro3, parametro4, parametro5, parametro6)
```

### Espacios en blanco

```python
# ✅ CORRECTO
edad = 25
# Dos espacios antes de comentario inline
lista = [1, 2, 3]  # lista de números

# Espacio después de comas
tupla = (1, 2, 3)

# Sin espacio dentro de paréntesis
funcion(arg1, arg2)

# Espacio alrededor de operadores
resultado = a + b - c * d

# ❌ INCORRECTO
edad=25
lista=[1,2,3]
funcion( arg1 , arg2 )
resultado=a+b-c*d
```

---

## 3️⃣ DOCSTRINGS (Documentación de Funciones)

Cada función DEBE tener un docstring. Usamos formato Google.

```python
# ✅ CORRECTO
def calcular_promedio(numeros: list[float]) -> float:
    """
    Calcula el promedio aritmético de una lista de números.
    
    Args:
        numeros: Lista de números flotantes a promediar
        
    Returns:
        El promedio de los números
        
    Raises:
        ValueError: Si la lista está vacía
        TypeError: Si hay elementos no numéricos
        
    Examples:
        >>> calcular_promedio([10, 20, 30])
        20.0
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    
    return sum(numeros) / len(numeros)


# ❌ INCORRECTO - Sin docstring
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)


# ❌ INCORRECTO - Docstring vacío o inútil
def calcular_promedio(numeros):
    """Calcula promedio"""
    return sum(numeros) / len(numeros)
```

### Para Clases

```python
# ✅ CORRECTO
class Usuario:
    """
    Representa un usuario del sistema.
    
    Attributes:
        nombre: Nombre completo del usuario
        email: Correo electrónico único
        edad: Edad en años (≥18)
    """
    
    def __init__(self, nombre: str, email: str, edad: int):
        """Inicializa un nuevo usuario."""
        self.nombre = nombre
        self.email = email
        self.edad = edad
```

---

## 4️⃣ COMENTARIOS

Comentarios SOLO para lógica compleja. No comentes lo obvio.

```python
# ✅ CORRECTO - Comenta decisiones no obvias
def calcular_costo_envio(peso: float, zona: str) -> float:
    """Calcula el costo de envío según peso y zona."""
    
    # Aplicamos un factor de 1.5 para zonas remotas debido a costos operacionales
    factor_zona = 1.5 if zona == "remota" else 1.0
    
    # El costo base es 0.5 por kg, con descuento por volumen después de 10kg
    costo_base = peso * 0.5
    descuento = 0.1 if peso > 10 else 0
    
    return (costo_base * factor_zona) * (1 - descuento)


# ❌ INCORRECTO - Comentarios obvios
def calcular_costo_envio(peso, zona):
    # Definir factor
    factor_zona = 1.5 if zona == "remota" else 1.0  # Si es remota, 1.5
    
    # Calcular costo
    costo = peso * 0.5  # Multiplicar peso por 0.5
    
    # Retornar
    return costo * factor_zona
```

---

## 5️⃣ TYPE HINTS (A partir de Fase 2)

Desde la Fase 2 en adelante, TODOS los parámetros y retornos deben tener type hints.

```python
# ✅ CORRECTO
def buscar_usuarios(nombre: str, edad_minima: int = 18) -> list[dict]:
    """Busca usuarios por nombre y edad mínima."""
    usuarios = []
    # ... lógica
    return usuarios


def procesar_lista(items: list[str]) -> dict[str, int]:
    """Procesa una lista y retorna un diccionario."""
    resultado = {}
    # ... lógica
    return resultado


# ✅ CORRECTO - Tipos complejos
from typing import Optional, Union, Tuple

def obtener_usuario(id: int) -> Optional[dict]:
    """Obtiene un usuario por ID o None si no existe."""
    # ... lógica
    return usuario or None


def convertir_a_numero(valor: Union[str, int, float]) -> float:
    """Convierte un valor a número flotante."""
    return float(valor)


# ❌ INCORRECTO - Sin type hints (después de Fase 1)
def buscar_usuarios(nombre, edad_minima=18):
    usuarios = []
    return usuarios
```

---

## 6️⃣ MANEJO DE ERRORES

Siempre maneja excepciones explícitamente. No uses `except:` sin especificar.

```python
# ✅ CORRECTO
def leer_archivo(ruta: str) -> str:
    """Lee contenido de un archivo."""
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"El archivo {ruta} no existe")
        raise
    except IOError:
        print("Error de lectura del archivo")
        raise
    except Exception as e:
        print(f"Error inesperado: {e}")
        raise


# ❌ INCORRECTO
def leer_archivo(ruta):
    try:
        return open(ruta).read()
    except:  # ¡NUNCA hagas esto!
        pass
```

---

## 7️⃣ ESTRUCTURA DE ARCHIVOS

```python
"""
Módulo: utils.py
Descripción: Utilidades generales para el proyecto
"""

# 1. Imports estándar
import os
import sys
from pathlib import Path

# 2. Imports de terceros
import requests

# 3. Imports locales
from . import config

# 4. Constantes
TIMEOUT_DEFECTO = 30
REINTENTOS_MAXIMOS = 3

# 5. Funciones de utilidad
def conectar_api(url: str) -> dict:
    """Conecta a una API y retorna JSON."""
    # ...
    pass

# 6. Clases
class GestorDatos:
    """Gestiona operaciones de datos."""
    pass

# 7. Main (si aplica)
if __name__ == "__main__":
    # Código de prueba
    pass
```

---

## 8️⃣ EJEMPLO COMPLETO

Aquí está todo junto:

```python
"""
Módulo: gestor_usuarios.py
Propósito: Gestionar usuarios del sistema
Autor: Tu nombre
Fecha: 2025-04-25
"""

from typing import Optional, List
from datetime import datetime


# Constantes
EDAD_MINIMA_VALIDA = 18
LARGO_MINIMO_PASSWORD = 8


class UsuarioInvalidoError(Exception):
    """Excepción para usuarios inválidos."""
    pass


class Usuario:
    """
    Representa un usuario del sistema.
    
    Attributes:
        nombre: Nombre completo (requerido)
        email: Email único (requerido)
        edad: Edad en años (≥18)
        activo: Si la cuenta está activa
    """
    
    def __init__(
        self,
        nombre: str,
        email: str,
        edad: int,
        activo: bool = True
    ):
        """Inicializa un nuevo usuario."""
        if edad < EDAD_MINIMA_VALIDA:
            raise UsuarioInvalidoError(
                f"Usuario debe ser mayor de {EDAD_MINIMA_VALIDA} años"
            )
        
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.activo = activo
        self.fecha_registro = datetime.now()
    
    def validar_email(self) -> bool:
        """
        Valida que el email tenga formato correcto.
        
        Returns:
            True si el email es válido, False en caso contrario
        """
        return "@" in self.email and "." in self.email.split("@")[1]
    
    def __str__(self) -> str:
        """Representación legible del usuario."""
        estado = "Activo" if self.activo else "Inactivo"
        return f"{self.nombre} ({self.email}) - {estado}"


def crear_usuario(
    nombre: str,
    email: str,
    edad: int
) -> Usuario:
    """
    Crea un nuevo usuario con validación.
    
    Args:
        nombre: Nombre completo
        email: Email del usuario
        edad: Edad en años
        
    Returns:
        Objeto Usuario creado
        
    Raises:
        UsuarioInvalidoError: Si los datos no son válidos
    """
    usuario = Usuario(nombre, email, edad)
    
    if not usuario.validar_email():
        raise UsuarioInvalidoError(f"Email inválido: {email}")
    
    return usuario


def filtrar_usuarios_activos(usuarios: List[Usuario]) -> List[Usuario]:
    """
    Filtra solo usuarios activos de una lista.
    
    Args:
        usuarios: Lista de objetos Usuario
        
    Returns:
        Lista de usuarios con activo=True
    """
    return [usuario for usuario in usuarios if usuario.activo]


if __name__ == "__main__":
    # Pruebas
    try:
        user1 = crear_usuario("Juan Pérez", "juan@example.com", 25)
        print(user1)
    except UsuarioInvalidoError as e:
        print(f"Error: {e}")
```

---

## ✅ CHECKLIST ANTES DE HACER COMMIT

Antes de hacer commit de tu código, verifica:

- [ ] El código sigue PEP8 (nombres, espacios, etc)
- [ ] Cada función tiene docstring completo
- [ ] No hay líneas de más de 88 caracteres
- [ ] Las excepciones son específicas (no `except:`)
- [ ] Los type hints están presentes (Fase 2+)
- [ ] No hay código comentado/muerto
- [ ] No hay `print()` de debug (usa logging)
- [ ] El código es ejecutable sin errores
- [ ] Nombres de variables son descriptivos

**Herramientas útiles:**

```bash
# Formatea automáticamente
black .

# Verifica PEP8
flake8 .

# Analiza código
pylint archivo.py
```

---

## 📖 Referencias

- [PEP8 - Style Guide](https://pep8.org/)
- [PEP257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Type Hints PEP 484](https://www.python.org/dev/peps/pep-0484/)

---

*Última actualización: Abril 2025*

Recuerda: **El código se escribe una vez, pero se lee cien veces. Hazlo legible.**
