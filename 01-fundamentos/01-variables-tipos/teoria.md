# Fase 1, Tema 1: Variables y Tipos de Datos

## 1. ¿Qué es una variable?
Imagina que te estás mudando de casa y tienes muchas cajas. Para no perderte, a una caja le pones una etiqueta que dice "Libros", a otra "Ropa" y a otra "Platos".
En programación, la computadora tiene una memoria inmensa. Una **variable** es como una de esas cajas: un espacio en la memoria al que le ponemos una "etiqueta" (un nombre) para guardar información y poder encontrarla más tarde.

En Python, crear una caja y guardar algo dentro es tan sencillo como:
`nombre_variable = valor`

## 2. Tipos de Datos Principales
Las cajas no solo guardan cualquier cosa; a veces es útil saber de qué tipo es lo que guardamos, porque no es lo mismo sumar dos números que "sumar" dos textos.

En Python, tenemos 4 tipos fundamentales:
1. **Enteros (`int`)**: Números sin decimales (ej. 10, -5, 0). Como contar manzanas.
2. **Flotantes (`float`)**: Números con decimales (ej. 3.14, -0.5). Como medir el peso o la estatura.
3. **Cadenas de texto (`str`)**: Palabras o frases. Siempre van entre comillas simples (`'`) o dobles (`"`). Como el título de un libro.
4. **Booleanos (`bool`)**: Solo pueden ser Verdadero (`True`) o Falso (`False`). Como un interruptor de luz (encendido/apagado).

## 3. Reglas de oro al nombrar variables (PEP8)
- Usa letras minúsculas.
- Separa las palabras con guiones bajos (`_`), por ejemplo: `edad_usuario` (esto se llama *snake_case*).
- ¡El nombre debe tener sentido! Es mejor `precio_total` que una simple `p`.
- No pueden empezar con números ni usar símbolos extraños.

## 4. Tipado Dinámico
Una cosa mágica de Python es que no tienes que decirle de qué tipo es la variable. Python es lo suficientemente inteligente para averiguarlo solo viendo qué guardas. Además, una variable puede guardar un número hoy, y mañana un texto (aunque es mejor evitarlo por orden).
