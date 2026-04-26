# 🚀 python-learning-path

**Ruta completa de aprendizaje en Python: desde fundamentos hasta FastAPI + Bases de Datos**

Una jornada de aprendizaje estructurada, práctica e intensiva para dominar Python y desarrollo backend moderno.

---

## 📋 Tabla de Contenidos

- [Visión General](#visión-general)
- [Timeline Estimado](#timeline-estimado)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Cómo Usar Este Repositorio](#cómo-usar-este-repositorio)
- [Metodología](#metodología)
- [Tecnologías a Aprender](#tecnologías-a-aprender)
- [Progreso](#progreso)

---

## 🎯 Visión General

Este repositorio documenta mi ruta de aprendizaje en Python, desde lo más básico hasta desarrollo backend profesional con FastAPI. Cada fase incluye:

- **Teoría** explicada de forma clara y progresiva
- **Ejemplos de código** anotados y funcionales
- **Ejercicios prácticos** con soluciones
- **Proyectos integradores** que combinan múltiples conceptos
- **Estándares de código** profesionales (PEP8, docstrings, etc)

**Objetivo final**: Dominar Python y ser capaz de crear APIs REST completas con FastAPI, manejo de bases de datos y deployment.

---

## ⏱️ Timeline Estimado

| Fase | Tema | Duración | Inicio | Fin |
|------|------|----------|--------|-----|
| 1 | Fundamentos Python | 3 semanas | - | - |
| 2 | Programación Orientada a Objetos | 3 semanas | - | - |
| 3 | Estructuras de Datos Avanzadas | 2 semanas | - | - |
| 4 | Módulos y Librerías | 1 semana | - | - |
| 5 | Datos y Archivos | 1 semana | - | - |
| 6 | Bases de Datos y SQL | 2 semanas | - | - |
| 7 | APIs REST y Requests | 1 semana | - | - |
| 8 | FastAPI Avanzado | 3 semanas | - | - |
| **TOTAL** | | **16 semanas** | - | - |

**Nota**: Ajustable según ritmo de aprendizaje. Flexibilidad es la clave.

---

## 📁 Estructura del Repositorio

```
python-learning-path/
│
├── README.md (este archivo)
├── PROFESOR_PROMPT.md (el prompt para la IA)
├── .gitignore
├── requirements.txt
│
├── 01-fundamentos/                          [Semanas 1-3]
│   ├── 01-variables-tipos/
│   │   ├── teoria.md
│   │   ├── ejemplos.py
│   │   └── ejercicios/
│   │       ├── 01_basico.py
│   │       ├── 02_intermedio.py
│   │       └── soluciones/
│   ├── 02-operadores/
│   ├── 03-control-flujo/
│   ├── 04-funciones/
│   ├── 05-strings-entrada/
│   └── PROYECTO_01_INTEGRADOR/
│
├── 02-poo/                                   [Semanas 4-6]
│   ├── 01-clases-objetos/
│   ├── 02-herencia/
│   ├── 03-polimorfismo/
│   ├── 04-metodos-especiales/
│   └── PROYECTO_02_INTEGRADOR/
│
├── 03-estructuras-datos/                     [Semanas 7-8]
│   ├── 01-listas-avanzado/
│   ├── 02-diccionarios-sets/
│   ├── 03-tuplas/
│   ├── 04-iteradores-generadores/
│   └── PROYECTO_03_INTEGRADOR/
│
├── 04-modulos-librerias/                     [Semana 9]
│   ├── 01-crear-modulos/
│   ├── 02-stdlib/
│   ├── 03-pip-virtualenv/
│   └── PROYECTO_04_INTEGRADOR/
│
├── 05-datos-archivos/                        [Semana 10]
│   ├── 01-archivos-texto/
│   ├── 02-json-csv/
│   ├── 03-excepciones/
│   ├── 04-logging/
│   └── PROYECTO_05_INTEGRADOR/
│
├── 06-bases-datos/                           [Semanas 11-12]
│   ├── 01-sql-basico/
│   ├── 02-sqlite-intro/
│   ├── 03-sqlalchemy-orm/
│   ├── 04-relaciones/
│   └── PROYECTO_06_INTEGRADOR/
│
├── 07-apis-rest/                             [Semana 13]
│   ├── 01-http-conceptos/
│   ├── 02-libreria-requests/
│   ├── 03-consumir-apis/
│   └── PROYECTO_07_INTEGRADOR/
│
├── 08-fastapi/                               [Semanas 14-16]
│   ├── 01-setup-basico/
│   ├── 02-endpoints-basicos/
│   ├── 03-parametros-validacion/
│   ├── 04-db-integration/
│   ├── 05-autenticacion/
│   ├── 06-deployment/
│   └── PROYECTO_08_FINAL/
│
└── docs/
    ├── METODOLOGIA.md
    ├── ESTÁNDARES_CODIGO.md
    └── RECURSOS_ADICIONALES.md
```

---

## 🎓 Cómo Usar Este Repositorio

### Opción 1: Aprendizaje Guiado (RECOMENDADO)

```bash
# 1. Clona el repositorio
git clone https://github.com/tuusuario/python-learning-path.git
cd python-learning-path

# 2. Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Abre tu IDE (Visual Studio Code, PyCharm, etc)
# Navega a 01-fundamentos/01-variables-tipos/

# 5. Lee teoria.md primero
# 6. Estudia ejemplos.py
# 7. Resuelve ejercicios/ por tu cuenta
# 8. Compara con soluciones/
# 9. Commit en Git: "feat: fundamentos - variables y tipos completado"
```

### Opción 2: Con IA Profesor

```bash
# Usa el prompt en profesor-ia.md
# Cópialo a tu IDE con IA integrada (Antigravity, Cursor, etc)
# La IA te guiará a través de cada tema
# Sigue el método: Teoría → Ejemplos → Ejercicio → Code Review
```

---

## 🧠 Metodología

### Estructura de Cada Lección

Cada tema sigue este patrón:

```
📄 teoria.md
└─ Explicación conceptual
   ├─ Qué es
   ├─ Por qué lo necesitamos
   ├─ Analogías del mundo real
   └─ Casos de uso

💻 ejemplos.py
└─ 3-5 ejemplos de código
   ├─ Creciente en complejidad
   ├─ Completamente anotados
   └─ Ejecutables (copy-paste)

📝 ejercicios/
└─ Problemas prácticos
   ├─ 01_basico.py (fácil)
   ├─ 02_intermedio.py (medio)
   └─ soluciones/ (con explicaciones)
```

### El Ciclo de Aprendizaje

```
1. LEER teoría.md
   ↓
2. EJECUTAR ejemplos.py (sin cambios)
   ↓
3. MODIFICAR ejemplos.py (experimentos)
   ↓
4. RESOLVER ejercicios/ (sin ver soluciones)
   ↓
5. COMPARAR con soluciones/ (aprender variaciones)
   ↓
6. HACER code review (aplicar estándares)
   ↓
7. COMMIT en Git
```

### Estándares de Código Obligatorios

Todos los códigos seguirán:

- **PEP8**: snake_case, 4 espacios, líneas ≤79 caracteres
- **Docstrings**: Cada función y clase debe tener docstring
- **Comentarios**: Solo para lógica compleja
- **Type hints**: A partir de Fase 2 (opcional pero recomendado)
- **Sin código muerto**: Nada comentado que no se use

**Ejemplo de estándar**:
```python
def calcular_promedio(numeros: list[float]) -> float:
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numeros: Lista de números flotantes
        
    Returns:
        El promedio de los números
        
    Raises:
        ValueError: Si la lista está vacía
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    
    return sum(numeros) / len(numeros)
```

---

## 🛠️ Tecnologías a Aprender

### Fase 1-5: Python Puro

- Core Python (tipos, control de flujo, funciones)
- POO (clases, herencia, polimorfismo)
- Estructuras de datos (listas, dicts, sets, tuplas)
- Módulos estándar (os, sys, json, datetime, pathlib)
- Manejo de archivos (txt, json, csv)
- Excepciones y logging

### Fase 6: Bases de Datos

- **SQLite**: Base de datos local
- **SQL básico**: SELECT, INSERT, UPDATE, DELETE, JOINs
- **SQLAlchemy**: ORM (Object-Relational Mapping)
- **Relaciones**: 1:1, 1:N, N:N

### Fase 7: APIs REST

- **HTTP**: Métodos, status codes, headers
- **requests**: Librería de cliente HTTP
- **JSON**: Parseo y serialización
- **APIs públicas**: Consumir datos externos

### Fase 8: FastAPI

- **FastAPI**: Framework web asincrónico
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI
- **Autenticación**: JWT básico
- **CORS**: Cross-Origin Resource Sharing
- **Documentación automática**: Swagger UI
- **Deployment**: Heroku, Railway, Render, etc

---

## 📊 Progreso

### ✅ Completado

- [ ] Fase 1: Fundamentos Python
- [ ] Fase 2: Programación Orientada a Objetos
- [ ] Fase 3: Estructuras de Datos
- [ ] Fase 4: Módulos y Librerías
- [ ] Fase 5: Datos y Archivos
- [ ] Fase 6: Bases de Datos
- [ ] Fase 7: APIs REST
- [ ] Fase 8: FastAPI Completo

### 📈 En Progreso

- [ ] Tema actual: _________________

### 🎯 Próximo

- [ ] Próximo tema: _________________

---

## 📚 Recursos Adicionales

### Documentación Oficial

- [Python Docs](https://docs.python.org/3/)
- [PEP8 Style Guide](https://pep8.org/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)

### Libros Recomendados

- "Fluent Python" - Luciano Ramalho
- "Clean Code" - Robert C. Martin
- "Design Patterns" - Gang of Four

### Comunidades

- r/learnprogramming
- Stack Overflow
- Python Discord

---

## 🤝 Cómo Contribuir (A Futuro)

Este es un repo personal de aprendizaje, pero si quieres mejorarlo:

1. Fork el repo
2. Crea una rama: `git checkout -b mejora/tema-x`
3. Commit: `git commit -m "docs: mejora en teoria de tema x"`
4. Push: `git push origin mejora/tema-x`
5. Pull Request

---

## 📝 Notas Personales

**Razón de este repositorio**: Documentar mi camino desde aprender Python básico hasta ser capaz de crear backends profesionales con FastAPI. Este repo será mi:

- 📚 Biblioteca de referencia
- 🎯 Portfolio de proyectos
- 📊 Tracker de progreso
- 🧑‍🏫 Recurso para enseñar a otros

**Compromiso**: Commit al menos 2-3 veces por semana, documentación clara, y código que sea orgulloso de mostrar.

---

## 📞 Preguntas Frecuentes

**¿Por dónde empiezo?**
→ `01-fundamentos/01-variables-tipos/teoria.md`

**¿Qué pasa si me atraso?**
→ Continúa con tu ritmo. La consistencia es más importante que la velocidad.

**¿Necesito experiencia previa?**
→ No. Este camino asume CERO experiencia previa en programación.

**¿Cuándo puedo hacer proyectos reales?**
→ Después de la Fase 4. Antes están los proyectos integradores.

---

## ⭐ Reconocimientos

Metodología basada en:
- Estructura de cursos profesionales (Stanford CS, MIT OCW)
- Mejores prácticas de la industria
- Feedback de mentores en ingeniería de software
- Experiencia propia aprendiendo

---

**Última actualización**: Abril 2025

**Estado**: 🟢 Activo en desarrollo

---

*Hecho con ❤️ como parte de mi viaje en ingeniería de software*
