# 🔒 Tuplas en Python: La Inmutabilidad al Poder

## 1. ¿Qué es una Tupla?
Una tupla es una colección de elementos **ordenada** e **inmutable**. A diferencia de las listas, una vez que creas una tupla, no puedes cambiar sus elementos, ni añadir nuevos, ni eliminarlos.

### Analogía del Mundo Real
Imagina que recibes un **Certificado de Nacimiento** o un **Título Universitario**. 
- Es una lista de datos (Nombre, Fecha, Institución).
- El orden importa.
- **No se puede modificar**. Si necesitas cambiar algo, tienes que emitir uno nuevo, no puedes simplemente borrar y escribir encima del original.

---

## 2. ¿Por qué usar Tuplas en lugar de Listas?

1. **Seguridad de Datos**: Si tienes datos que no deben cambiar durante la ejecución del programa (como los días de la semana o coordenadas geográficas), las tuplas evitan errores accidentales de modificación.
2. **Rendimiento**: Las tuplas son más ligeras y rápidas que las listas. Python reserva exactamente el espacio que necesitan en memoria.
3. **Uso como Claves**: A diferencia de las listas, las tuplas pueden ser usadas como **claves en un diccionario** (porque son "hashables").

---

## 3. Sintaxis y Operaciones Básicas

```python
# Creación
punto = (10, 20)
vacia = ()
un_solo_elemento = (5,) # OJO: La coma es obligatoria para un solo elemento

# Acceso (Igual que las listas)
print(punto[0]) # 10
```

---

## 4. El Superpoder: Unpacking (Desempaquetado)
Python permite asignar los elementos de una tupla a variables individuales de forma directa:

```python
persona = ("Johan", 25, "Colombia")
nombre, edad, pais = persona

print(nombre) # "Johan"
```

---

## 5. ¿Cuándo usar cada una?

| Estructura | ¿Se puede cambiar? | Caso de Uso |
|------------|-------------------|-------------|
| **Lista** | Sí (Mutable) | Colecciones de objetos similares que pueden crecer o cambiar. |
| **Tupla** | No (Inmutable) | Datos heterogéneos (Nombre, Edad) que representan una "unidad" o registro. |
