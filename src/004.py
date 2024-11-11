"""
Interactuar con el usuario 2

Ahora que hemos visto las funciones, vamos a ver otra: `input()`.
input() es una función builtin que llama a stdin para tomar la entrada de un usuario.
Recuerdas las funciones de 003.py? Pues aquí esta máquina sí que nos devuelve algo: una cadena.
Esta cadena será la entrada del usuario, incluso con el caractér de final de línea.
"""

input()

"""
Por sí sola la función no vale mucho, pero cuando usamos una variable para asignar la entrada del usuario:
"""

entrada: str = input()

"""
Ahora lo que estamos haciendo es tomar la entrada del usuario, que es input() y
la estamos guardando en un cajón llamado "entrada". Esto nos aporta dinamismo y
nos permite interactuar con el usuario, con lo que podemos hacer muchas cosas.
Te propongo un reto: Aunque no hayamos visto operadores aritméticos, (ahora en cuanto vayamos con int_type)
intenta escribir un programa de calculadora, el cual le pida la entrada al usuario dos veces y luego te dé ese mismo número sumado. Solución en 004s.py.
Continúa cuando hayas resuelto el ejercicio.
"""


"""
En esencia, input() es una función que nos permite pedirle una entrada al usuario, para interactuar con él y poder pedirle y remitirle información.
"""