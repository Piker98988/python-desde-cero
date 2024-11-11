"""
Estructuras de control: lo que nos permite tomar decisiones

Las estructuras de control son delatadas porque todas se definen usando una 
"palabra reservada". Estas palabras están reservadas para el intérprete o JIT
y no las puedes usar de variables. Aparte, estas mismas keywords son estándares en la
mayoría de lenguajes, lo que justifica aún más la afirmación de que el primer lenguaje
de programación que aprendes es el más difícil.

Python tiene muchas palabras reservadas, más de 25, aunque se pueden sacar por 
intuición. Llamarías a una variable "import"? Lo dudo mucho. Igualmente, de todas
estas palabras solo hay pocas que nos interesan, que son las que definen nuestras
estructuras de control. Empecemos con una lista de keywords:

- while
- if
- else
- elif
- break
- for
- in

Vamos a ver el uso de estas palabras reservadas en un simple ejemplo con "if", "elif" y "else":
"""
es_hombre = True
es_mujer = False


if es_hombre and es_mujer:
    print("Eres hombre y eres mujer")
elif es_hombre:
    print("Eres hombre")
elif es_mujer:
    print("Eres mujer")
else:
    print("No eres nada")

"""
Vamos a romper esta expresión en diferentes partes, empecemos con la línea 29 y 30:
en la línea 29 declaramos nuestra condición a cumplir, es decir, si se cumple x
condición, que se ejecute el código de la línea dentro de ese "if". 
Cómo sabemos que está dentro del "if"? En caso de la mayoría de lenguajes de
programación se usan lo que en inglés se denomina "curly braces" o "brackets":

if condición {
    código
}

En caso de python, usa una sintaxis mucho más legible para nuevos programadores.
Lo que denota cada alcance o scope es la indentación. una doble indentación quiere
decir que tenemos un código anidado sobre otro:

if condición:
    código
        más_código

Ahora, veamos que se debe de cumplir para que se ejecute la línea 30:

if es_hombre and es_mujer:

Esta línea hace uso de un operador lógico que explicamos en 007.py.
En caso de nuestro usuario, es_hombre es verdadero y es_mujer es falso,
lo que supone que la afirmación "es_hombre and es_mujer" resulta falsa.
Esto hace que se salte el código de la línea 30 y se ejecute el resto del programa.
Para que la línea 30 se ejecute, es_hombre y es_mujer deben de ser verdaderos
al mismo tiempo. Si se ejecuta la línea 30 de código la evaluación de condiciones
para, lo que explicaremos un poco más adelante.
"""

if es_hombre and es_mujer: # Condición falsa
    print("Eres hombre y eres mujer") # Código muerto
elif es_hombre:
    print("Eres hombre")
elif es_mujer:
    print("Eres mujer")
else:
    print("No eres nada")
    
"""
elif es una palabra reservada que actúa como una fusión de "else" e "if". Esto se
traduce a "si no, si pasa esto, ejecuta lo siguiente". Esto resulta útil para
recursivamente evaluar diferentes valores, como hacemos aquí. Para decodificar
esta línea de código vamos a interpretarla como si fuese un simple "if":

(72) || elif es_hombre:
(73) ||     print("Eres hombre")

Esto nos quiere decir que si la condición "es_hombre" es verdadera, se ejecutará
el código de la línea 73 y se terminará de evaluar la expresión, lo que hará que no
se compruebe la siguiente afirmación:

(74) || elif es_mujer:
(75) ||     print("Eres mujer")

Este código no se ejecutará de ninguna manera, ya que ya se ha salido de la evaluación de expresiones en la línea 73. 
Esto significa que el intérprete ni siquiera comprobará la veracidad de la afirmación
en la línea 74.
"""

# ! El código muerto será indicado con una exclamación al principio del comentario
if es_hombre and es_mujer:              # Condición falsa
    print("Eres hombre y eres mujer")   
    # ! Código muerto
elif es_hombre:                         # Verdadero
    print("Eres hombre")                
    # Se ejecutará esta línea de código
elif es_mujer:                          # ! No se evaluará la siguiente condición
    print("Eres mujer")                 
    # ! Código muerto
else:
    print("No eres nada")


"""
Finalmente, else es una condición de descarte. Si no se cumple ninguna de las anteriores,
ejecuta lo siguiente. Es una "wild card". Un as en la manga. En caso de que
no se ejecute ninguna de las condiciones anteriores ejecuta esto. Ya que es una
condición de descarte, no necesitamos proveer a la palabra reservada con una
expresión que evaluar.
"""