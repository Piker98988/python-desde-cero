"""
Concisidad de Python: Anexo

En Python tenemos expresiones muy concisas y muy rápidas de escribir, lo cual
nos ayuda a entender el código y por tanto a poder depurarlo de una manera más simple.
En este caso, vamos a ver cómo podemos reducir una estructura "if" a una línea de código:
"""

print("Te gustan las patatas? (s/n)")
input_del_user: str = input(">> ")

input_del_user_parseada: bool = True if input_del_user == "s" else False

"""
La línea 9 y 10 preguntan y toman la entrada del usuario, que ya debería de estar
interiorizado, así que no voy a explicarlo más. Vamos a ver nuestra expresión
condensada de la línea 12:

(12) || input_del_user_parseada: bool = True if input_del_user == "s" else False

Vamos a dividirlo en partes:

(12) || input_del_user_parseada: bool = True if input_del_user == "s" else False
xxxxxxx -----------------------  ----   ---- -- --------------------- ----------
                   A               B     C    D         E                  F

Y ahora expliquemoslo:
-> A: nombre de la variable. La variable tiene al final "parseada" que viene de "parse"
en inglés. La palabra "parse" quiere llegar a significar que vamos a sacar algo
de otra cosa, es decir, el verbo "to parse" es el verbo de "procesar información y devolver algo diferente".
-> B: Como vimos en las buenas prácticas de 003a.py, esta parte nos ayuda a entender
que esta variable va a ser un booleano, lo cual no hubiésemos sabido a primera
vista como en este código. Sigo recomendando poner los tipos en Python, aunque no
sea necesario en lo absoluto.
-> C: A primera vista puede parecer que el valor de la variable es True, pero eso
nos lleva a D:
-> D: La palabra reservada if, la cual en este caso actúa de manera diferente a
como vimos en las estructuras de control. En este caso, el valor a devolver está
a la izquierda, el cual es "C". Luego, vemos que la condición para que este 
valor "C" se devuelva y por tanto se asigne a nuestra variable se encuentra a la
derecha, así que la sintaxis es la siguiente:

(xx) || variable_a_asignar: clase = valor_a if condición

-> E: esta es nuestra condición. Aún no hemos visto operadores de comparación, 
lo cual constituirá la siguiente lección. De manera rápida, un igual (a = b) es
un operador de asignación, que quiere decir que "a es b", en cambio, un doble 
igual es un operador de comparación, que traducido a cristiano es básicamente que
"¿es a lo mismo que b?", lo cual devolverá un booleano. Esta expresión es la que
se evaluará cuando se deba de decidir en nuestro if si queremos que se devuelva
True o no, que se ejecute la parte F.
-> F: Aquí está nuestro renombrado else. Else es una cláusula de "todo vale", como
hemos mencionado ya varias veces. Esta cláusula devolverá False
solamente si no se cumple la condición establecida en el if, por tanto:
"""

input_del_user_parseada: bool = True if input_del_user == "s" else False
# Será True si el usuario introduce s, si introduce otra cosa será False.

# Anexo un poco largo, pero vale la pena entender estas expresiones y saber que
# existen, porque son muy útiles cuando estamos tratando de programar.
