# Fase 1, Tema 2: Operadores

## 1. ¿Qué es un operador?

Un **operador** es un símbolo que le dice a Python que realice una operación entre uno o más valores.
Piénsalo como los botones de una calculadora: el `+` suma, el `-` resta, pero en Python tenemos
muchos más tipos de "botones" con poderes distintos.

En este tema cubrimos **5 tipos** de operadores.

---

## 2. Operadores Aritméticos

Los más conocidos. Hacen matemáticas.

| Operador | Nombre            | Ejemplo      | Resultado |
|----------|-------------------|--------------|-----------|
| `+`      | Suma              | `10 + 3`     | `13`      |
| `-`      | Resta             | `10 - 3`     | `7`       |
| `*`      | Multiplicación    | `10 * 3`     | `30`      |
| `/`      | División real     | `10 / 3`     | `3.333...`|
| `//`     | División entera   | `10 // 3`    | `3`       |
| `%`      | Módulo (residuo)  | `10 % 3`     | `1`       |
| `**`     | Potencia          | `2 ** 8`     | `256`     |

> 💡 **Analogía**: Tienes 10 panes y los repartes entre 3 personas.
> - Con `/` cada una recibe `3.333...` panes (no muy real).
> - Con `//` cada una recibe `3` panes enteros.
> - Con `%` te quedan `1` pan sobrando.

---

## 3. Operadores de Asignación

Ya conociste el `=` para crear variables. Existen versiones "compuestas" que
**modifican una variable y la reasignan** al mismo tiempo, ahorrando escritura.

| Operador | Equivale a         |
|----------|--------------------|
| `x += 5` | `x = x + 5`       |
| `x -= 5` | `x = x - 5`       |
| `x *= 5` | `x = x * 5`       |
| `x /= 5` | `x = x / 5`       |
| `x //= 5`| `x = x // 5`      |
| `x **= 2`| `x = x ** 2`      |

> 💡 **Analogía**: Tienes $100 en la billetera. `billetera += 50` es decir
> "agrega 50 a lo que ya tenía", en vez de escribir `billetera = billetera + 50`.

---

## 4. Operadores de Comparación

Comparan dos valores y **siempre devuelven un booleano** (`True` o `False`).
Son la base de toda toma de decisiones en programación.

| Operador | Significado        | Ejemplo      | Resultado |
|----------|--------------------|--------------|-----------|
| `==`     | ¿Son iguales?      | `5 == 5`     | `True`    |
| `!=`     | ¿Son diferentes?   | `5 != 3`     | `True`    |
| `>`      | ¿Mayor que?        | `10 > 3`     | `True`    |
| `<`      | ¿Menor que?        | `10 < 3`     | `False`   |
| `>=`     | ¿Mayor o igual?    | `18 >= 18`   | `True`    |
| `<=`     | ¿Menor o igual?    | `5 <= 4`     | `False`   |

> ⚠️ **Error clásico**: No confundas `=` (asignar) con `==` (comparar).
> `edad = 18` → guarda el número 18 en `edad`.
> `edad == 18` → pregunta si `edad` vale 18 (responde True o False).

---

## 5. Operadores Lógicos

Combinan condiciones booleanas. Son como conectores del lenguaje natural:
"Y", "O", "NO".

| Operador | Significado                                    | Ejemplo                      | Resultado |
|----------|------------------------------------------------|------------------------------|-----------|
| `and`    | Ambas condiciones deben ser `True`             | `True and False`             | `False`   |
| `or`     | Al menos una condición debe ser `True`         | `True or False`              | `True`    |
| `not`    | Invierte el booleano                           | `not True`                   | `False`   |

> 💡 **Analogía para `and`**: Para entrar a una película necesitas
> *tener entrada* **Y** *ser mayor de edad*. Ambas al mismo tiempo.
>
> 💡 **Analogía para `or`**: Para abrir la puerta puedes usar la *llave*
> **O** la *tarjeta magnética*. Con una sola basta.

---

## 6. Operadores de Pertenencia

Comprueban si un elemento **existe dentro** de una colección (lista, texto, etc).
Los veremos más en el Tema de listas, pero es importante conocerlos ya.

| Operador  | Significado                     | Ejemplo                          | Resultado |
|-----------|---------------------------------|----------------------------------|-----------|
| `in`      | ¿Está dentro?                   | `"a" in "hola"`                  | `True`    |
| `not in`  | ¿No está dentro?                | `"z" not in "hola"`              | `True`    |

---

## 7. Precedencia de Operadores (Orden de operaciones)

Python sigue las mismas reglas que las matemáticas: hay un orden en que evalúa los operadores.

```
1. **         (potencia)
2. *, /, //, %  (multiplicación, divisiones)
3. +, -         (suma y resta)
4. ==, !=, >, <, >=, <=  (comparaciones)
5. not          (negación lógica)
6. and          (Y lógico)
7. or           (O lógico)
```

> 💡 **Regla de oro**: Ante la duda, usa **paréntesis**. Son gratis y
> hacen tu código mucho más legible.
> `resultado = (precio * cantidad) + (envio * 1.1)` → clarísimo.
