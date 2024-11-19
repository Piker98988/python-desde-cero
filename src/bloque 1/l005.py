"""
Tipos de datos avanzados

En matemáticas conocemos las magnitudes como escalares, conjuntos de magnitudes
como vectores y conjuntos de vectores como matrices. Esto se puede interpretar como
una lista. Las listas son vectores, y sus valores son escalares. Por tanto, una
lista de la cual sus valores son otras listas, se puede interpretar como una matriz, tal que:

[
    [a1, a2, a3]
    [b1, b2, b3]
    [c1, c2, c3]
]

Esto se interpreta como una matriz.
"""

mi_lista: list = [1, 2, 3]

"""
A partir de ahora los llamaremos vectores por conveniencia. Los vectores pueden
tener cuantos valores sean, mientras estos estén definidos. Las matrices se representan así:
"""

mi_matriz: list[list] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

"""
Podemos usar cualquier elemento de una lista usando el corchete para los índices.
En programación SIEMPRE se empieza a contar desde el 0. Por tanto, el primer
elemento de nuestro vector es x sub 0, ya que está en la posición 0.
"""

primer_elemento_vector: int = mi_lista[0] 
# ? Es 1, ya que x sub 0 en la lista es 1

"""
Expandiendo en esto, podemos definir lo que es la anidación. La anidación supone
lo siguiente: este concepto significa que hay algo sobre algo, igual que los nidos
de pájaro en los árboles. Podemos anidar una expresión de corchetes sobre otra,
tal que la primera indique la posición y de nuestro elemento y la segunda expresión
sobre x, tal que aplicado al concepto de que se empieza a contar desde cero,
sale lo siguiente:

m[y - 1][x - 1]

Lo cual aplicado significa que si queremos obtener el elemento 8, busquemos sus
propiedades:

8 está en la segunda columna y tercera fila, que se traduce a x = 2 e y = 3.
Aplicando la fórmula resulta: m[2][1], y ahora simplemente hace falta sustituir
m por una matriz adecuada:
"""

m = mi_matriz

ocho: int = m[2][1] # ? El resultado es 8