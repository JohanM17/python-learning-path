"""
EJERCICIO: La Biblioteca Personal
---------------------------------------------------------
Consigna:
Vas a crear un sistema para gestionar tu colección de libros.

1. Crea una clase 'Libro' con __init__ que reciba:
   - titulo (str)
   - autor (str)
   - paginas (int)

2. Implementa __str__ para que al hacer print(libro) muestre:
   📖 "El Principito" por Antoine de Saint-Exupéry (96 páginas)

3. Implementa __eq__ para que dos libros sean iguales
   si tienen el mismo título Y el mismo autor.

4. Crea una clase 'Biblioteca' con __init__ que tenga
   una lista vacía llamada 'libros'.
   - Agrega un método 'agregar(libro)' que añada libros a la lista.
   - Implementa __len__ para que len(biblioteca) retorne cuántos libros tiene.
   - Implementa __str__ para que muestre: "Biblioteca con X libros."

5. Prueba así:
   - Crea al menos 3 libros distintos.
   - Agrega todos a la biblioteca.
   - Imprime cada libro con print().
   - Imprime la biblioteca con print().
   - Verifica len() de la biblioteca.
   - Compara dos libros con ==.

Entrada esperada:
   libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
   print(libro1)

Salida esperada:
   📖 "El Principito" por Antoine de Saint-Exupéry (96 páginas)
"""

class Libro:
   def __init__(self, titulo:str, autor:str, paginas:int):
      self.titulo = titulo
      self.autor = autor
      self.paginas = paginas

   def __str__(self):
      return f"{self.titulo} por {self.autor} ({self.paginas} páginas)"

   def __eq__(self, otro):
      return self.titulo == otro.titulo and self.autor == otro.autor


class Biblioteca:
   def __init__(self):
      self.libros = []

   def agregar(self, libro):
      self.libros.append(libro)

   def __len__(self):
      return len(self.libros)

   def __str__(self):
      return f"La biblioteca tiene {len(self)} libros"


libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
libro2 = Libro("Harry Potter y la Piedra filosofal", "Rowling", 100)
libro3 = Libro("El Hobbit", "Desconocido", 126)

mi_biblioteca = Biblioteca()
mi_biblioteca.agregar(libro1)
mi_biblioteca.agregar(libro2)
mi_biblioteca.agregar(libro3)

print(f"""Libros que hay
         {libro1}
         {libro2}
         {libro3}
         """)

print(mi_biblioteca)
print(f"Libros: {len(mi_biblioteca)}")
print(libro1 == libro2)
