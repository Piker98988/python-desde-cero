"""
Estructuras de control III

En ete caso, vamos a ver el bucle while. Como vimos en 008.py, hay varias
palabras reservadas, y las que vamos a usar esta vez serán "while" y "break".
Veamos un ejemplo de un bucle while:
"""

while True:
    user_tiene_hermanos = input("Tienes hermanos? ")
    if user_tiene_hermanos:
        print("cuida de tus hermanos")
    else:
        break

"""
Este ejemplo es un poco más complejo, por tanto, necesitaremos un poco más
de chicha para explicarlo. Empecemos por lo que es la línea 9:

(09) || while True:

esta línea abre nuestra estructura de control, la cual es un bucle while. En nuestro
caso, podemos ver que la condición del bucle es True, la cual es una afirmación
lógica verdadera, por tanto, mientras el programa esté corriendo, este bucle
se ejecutará de manera indefinida, ya que la condición se cumplirá siempre.
Recuerdas la estructura de control "if"? En esta estructura si la condición se
cumplía, se ejecutaría el código una vez solamente, en cambio, en los bucles
while, si la condición se cumple, el código dentro de el bucle se ejecutará hasta
que la condición se deje de cumplir. Nuestra condición es "True",
aunque podría ser una expresión booleana como "es_mayor_de_edad and tiene_hermanos".
"""

while True: # Se ejecutará indefinidamente
    user_tiene_hermanos = input("Tienes hermanos? ")
    if user_tiene_hermanos:
        print("cuida de tus hermanos")
    else:
        break
    

"""
Ahora, pasemos a la línea 34:

(34) || user_tiene_hermanos = input("Tienes hermanos? ")

Esta línea define la entrada del usuario y la guarda en nuestra variable "user_tiene_hermanos".
Como podemos ver, la función input hace una llamada a print con lo que tenga dentro y
tras ello toma la entrada del usuario y te la devuelve en forma de string.
Esta línea toma la respuesta del usuario a la pregunta "Tienes hermanos? " y la
guarda en una variable. Pasemos al resto de líneas del bucle:

(35) || if user_tiene_hermanos:
(36) ||     print("Cuida de tus hermanos")
(37) || else:
(38) ||     break

Aquí podemos ver que evaluamos la condición "user_tiene_hermanos". Si recuerdas de
007.py, aquí mencionamos que las strings se pueden interpretar como booleanos, es
decir, si la string está vacía (el usuario no responde), se interpretará como
False y si el usuario ha respondido algo, se interpretará como True y la condición será válida.
Entonces, si el usuario responde a la pregunta, se ejecutará la línea 36, la cual
manda a stdout el texto "Cuida de tus hermanos". Después de eso, como seguimos en
un bucle while, se evaluará de nuevo la condición de la línea 33, la cual sigue
siendo verdadera.
Si la afirmación es falsa, se ejecutará el código dentro del "else", el cual es el de la línea 38:

(38) ||     break

Como dijimos en 008.py, "break" es una palabra reservada, la cual
literalmente, como el propio nombre indica, rompe. Pero qué rompe?
En nuestro caso, rompe el bucle while de la línea 33. Esta sería la 
manera de salir del bucle, ya que la afirmación True siempre será
verdadera, por tanto, el bucle se ejecutará siempre.
Vamos a recorrer el código de nuevo con comentarios:
"""

while True: # ? Se va a ejecutar todo el tiempo
    user_tiene_hermanos = input("Tienes hermanos? ") # * Entrada del user
    if user_tiene_hermanos: # ? si el usuario responde:
        print("cuida de tus hermanos") # * manda a stdout y ejecuta de nuevo desde la línea 78
    else: # ? si el usuario no responde
        break # * rompe el bucle y ejecuta el código después del bucle