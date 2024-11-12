"""
Estructuras de control II

Como dije antes, las estructuras de control requieren de una palabra reservada para
definirlas, por tanto, ahora veremos los bucles "for".

Como vimos en los tipos de datos, hay escalares, vectores y matrices. En python
los vectores y las matrices se interpretan como iterables, ya que tienen varios
elementos.
El bucle for se aprovecha de esta característica tal que nos permite que podamos
recorrer cada uno de estos elementos ejecutando un dado código para cada uno de ellos.
Veamos un ejemplo:
"""

vec_i8: list[int] = [1, 2, 3, 4, 5]

for n in vec_i8:
    print(n)


"""
En la línea 15 definimos una variable llamada vec_i8:

(15) || vec_i8: list[int] = [1, 2, 3, 4, 5]

Y en la 17 referenciamos a esta variable:

(17) || for n in vec_i8:
        --- - -- ------
         A  B CC   DD

Vamos a romper esta expresión en pequeños trozos para entenderla mejor:

-> A = palabra reservada de nuestro bucle
-> B = declaración de variable de elemento en nuestro bucle
-> C = palabra reservada declarando el elemento iterable a recorrer
-> D = referencia al iterable

Y ahora vamos a dar una explicación más profunda.
A declara nuestro bucle, mientras que en B declaramos una variable, que
va a ser el elemento actual que estemos recorriendo durante el bucle, es
decir, si nosotros estamos recorriendo vec_i8 y lo hemos recorrido ya 3
veces, estamos en la cuarta iteración:

(15) || vec_i8: list[int] = [1, 2, 3, 4, 5]
                             -  -  -  -  -
                             A  B  C  D  E

A es la primera iteración, B la segunda, C la tercera... etc. Cuando
llegamos a 4 quiere decir que el código de la línea 18, es decir:

(18) ||     print(n)

se ha ejecutado ya 3 veces, y se va a ejecutar una cuarta. La pregunta es,
qué es n? en nuestro caso, n es el elemento número 4, ya que estamos en la
cuarta iteración del bucle. Si estuviésemos en la primera iteración, n = 1,
ya que el primer elemento de la lista es 1. En la segunda n = 2, porque es
el segundo elemento, etc.

En conclusión, un bucle for ejecuta un código tantas veces como longitud tenga
tu iterable, es decir, nuestro bucle for se ejecutará 5 veces, una por cada valor del iterable:
"""

vec_i8: list[int] = [1, 2, 3, 4, 5]

for n in vec_i8:
    print(n)

# * Primera vez: 'n = 1' ya que 'vec_i8[0] = 1'
# * Segunda: 'n = 2' ya que 'vec_i8[1] = 2'
# ? N es el elemento de la iteración actual, que quiere decir que si vamos
# ? a ejecutar el código 5 veces, la cuarta vez tomará el cuarto elemento
# ? de nuestro iterable.

"""
He mencionado como las matrices también son iterables, por tanto vamos a ver un ejemplo:
"""

m_1: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for vector in m_1:
    print("Vector:")
    for escalar in vector:
        print(escalar)

"""
En este snippet de código me he asegurado de en vez de nombrar las variables con
nombres poco descriptivos, las he nombrado de una manera legible para poder entender
bien lo que ocurre:

> La programación tiene dos partes muy difíciles:
> los punteros de memoria y nombrar las cosas.
> - Programador de C promedio

Vamos a descomponer lo que ocurre en el siguiente código, empezando por la línea 85 y 86:

(85) || for vector in m_1:
(86) ||     print("Vector:")

En estas líneas estamos recorriendo la matriz por los vectores que tiene dentro,
es decir, si una matriz es un vector de vectores, estamos aplicando un código a
cada uno de esos vectores. Digamos que acabamos de ejecutar el código, por tanto,
estamos iterando la matriz por primera vez y estamos en el primer vector:

(79) || m_1: list[list[int]] = [
(80) ||     [1, 2, 3],
(81) ||     [4, 5, 6],
(82) ||     [7, 8, 9],
(83) || ]

En la línea 80 podemos ver el primer vector, el cual contiene los elementos 1, 2, y 3.
En este caso, la variable "vector" se asigna a el vector de la línea 80, el cual
es el primer vector de los tres que tiene nuestra matriz. Esto quiere decir que
por cada vector que haya en nuestra matriz tendremos mandado a consola la cadena
"vector:", como dice en la línea 86:

(86) ||     print("Vector:")

Continuemos con las líneas 87 y 88:

(87) ||     for escalar in vector:
(88) ||         print(escalar)

Vamos a leer poco a poco la línea 87. Empezamos con otro bucle for, esta vez
anidado. Dice que por cada escalar que haya dentro del vector, se ejecute el
código de la línea 88. Vamos a poner un ejemplo como antes: estamos en la primera iteración del primer bucle for, el de la línea 85. Esto quiere decir que
la variable "vector" está asignada al primer vector de la la matriz. Entonces,
ahora recorreremos los escalares dentro de este vector.
Veamos que dice la línea 88:
En nuestro caso, esta línea nos manda a consola el escalar que estemos recorriendo
actualmente, que, como hemos explicado antes, es el primero del primero.
Por tanto, el código lo que hará sera enviar a stdout cada uno de los elementos
de la matriz, sin enviarlo en formato vector. La salida del programa será la siguiente:

```stdout
Vector:
1
2
3
Vector:
4
5
6
Vector:
7
8
9
```
Básicamente, recorremos la matriz y por cada vector de la matriz recorremos ese mismo
vector.
"""

# ? Este tema es complejo. Si no se entiende correctamente, ya sabes,
# ? WhatsApp a +34 660...