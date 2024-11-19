"""
El tipo bool: muy importante

El tipo bool viene de booleano, ya que hubo un gracioso que se apellidaba bool y este
gracioso decidió que todo se podía interpretar como 0 o 1, Falso o verdadero, negativo o positivo... etc.
Esto nos lleva a lo que es un bool en Python: un tipo bool puede tener dos valores: True o False
"""

True

verdadero: bool = True

falso: bool = False

"""
Esto quiere decir que podemos usar otros tipos de datos como booleanos, como mencioné
en el archivo 006.py, las operaciones lógicas devuelven siempre un booleano, por tanto,
nos sirven de ejemplo perfecto:
"""

operacion_or: bool = True or False 
# ? or = True

operacion_and: bool = True and False
# ? and = False

operación_not: bool = not True
# ? not = False

"""
Esto lo hemos dado en SOM. Debería de ser fácil:

OR -> True or False -> (Hay un True, por tanto la expresión "True or False" es verdadera) -> True
AND -> True and False -> (Los dos tienen que ser true, si no, es false) -> False
NOT -> not True -> (Literalmente no true, es decir, false) -> False
"""

booleano_cadena: bool = ""
booleano_verdadero: bool = "hola"

"""
Python es dinámico, por tanto, tiene la capacidad de traducir cualquier dato en un bool. En caso de Python, estas son las equivalencias para cada tipo de dato:

String
-> False = "" (cadenas vacías)
-> True  = "a" (cualquier cadena con algo dentro)

Int
-> False = 0 (valor 0)
-> True  = 256 (cualquier valor que no sea 0)
-> Se aplica lo mismo para floats

List
-> False = [] (una lista vacía)
-> True  = ["a", "b"] (lista con cualquier elemento de cualquier longitud)
"""