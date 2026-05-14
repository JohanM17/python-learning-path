# 📖 Diccionarios y Sets en Python

## 1. Diccionarios (`dict`)
Los diccionarios son colecciones de pares **clave-valor**. Son mutables, desordenados (en versiones antiguas, aunque mantienen el orden de inserción desde Python 3.7+) y no permiten claves duplicadas.

### ¿Por qué usarlos?
Imagina que quieres guardar la edad de 100 personas. 
- En una **lista**, tendrías que recordar que el índice 0 es Juan, el 1 es Maria... ¡Un caos!
- En un **diccionario**, usas el nombre como clave: `edades["Juan"]`. Es directo y eficiente.

### Sintaxis Básica
```python
mi_dict = {
    "clave": "valor",
    "otra_clave": 123
}
```

---

## 2. Sets (Conjuntos)
Los conjuntos son colecciones de elementos únicos y desordenados. Se definen con llaves `{}` pero sin el formato `clave: valor`.

### Características:
- No permiten duplicados.
- Son ideales para operaciones matemáticas de conjuntos (unión, intersección, diferencia).
- Son extremadamente rápidos para verificar si un elemento existe (`x in mi_set`).

---

## 3. Comparativa de Eficiencia (Big O)

| Operación | Listas (O) | Diccionarios/Sets (O) |
|-----------|-----------|-----------------------|
| Buscar un elemento | O(n) | O(1) - Instantáneo |
| Insertar | O(1) o O(n) | O(1) |
| Eliminar | O(n) | O(1) |

---

## 4. Métodos Clave

### Diccionarios:
- `.get(key, default)`: Acceso seguro.
- `.keys()`: Lista de todas las claves.
- `.values()`: Lista de todos los valores.
- `.items()`: Tuplas de (clave, valor).
- `.pop(key)`: Elimina y devuelve el valor.

### Sets:
- `.add(elem)`: Añade un elemento.
- `.remove(elem)`: Elimina (da error si no existe).
- `.discard(elem)`: Elimina (no da error).
- `.union(otro_set)`: Combina ambos.
- `.intersection(otro_set)`: Solo los comunes.
