"""
Python como lenguaje tiene varias cosas que guardar en nuestros
cajones, los cuales se llaman "tipos de datos". Estos tipos se te irán quedando
con el tiempo, ya que son extremadamente importantes para entender errores y como
Python trata los diferentes valores y objetos que guardemos en cajones. Los tipos de datos básicos en python son los siguientes:

- String
- Int
- Float
- List

Podemos especificar lo que queremos que haya en un cajón poniendo dos puntos
y el tipo que queramos a la hora de escribir, tal que así:
"""

cajón: str = "Calcetines"

"""
Ahora, podemos usar cajón dónde queramos, aunque le hemos dicho que es un
"str", que viene de string. Cada tipo significa una cosa diferente:

String: 
    String viene de cadena en inglés. En programación, no llamamos a las frases
    "frases", si no que las llamamos cadenas. Cualquier texto puede ser una cadena,
    ya que de ahí viene el nombre, cadena de cadena de caracteres.
    ? Llamado "str"

Int:
    Los Int toman su nombre del inglés integer, que traducido al español es
    entero. Un entero se refiere al número, es decir, al número entero, el
    cual puede ser negativo y positivo, pero nunca racional, es decir, con
    decimales.
    ? Este tipo de dato python lo llama "int"

Float:
    Float viene de la coma de los números racionales, ya que los float tienen
    una coma flotante, la cual podemos ir rotando a lo largo de 32 bits de espacio binario:
    
    0000000000000000000000000000,000
    
    Es una coma flotante porque la podemos mover a dónde sea en esa representación
    binaria, cualquiera de esos ceros puede ser la coma, lo que quiere decir
    que podemos tener más números a la izquierda para magnitudes grandes o más números
    a la derecha para precisión:
    
    00,00000000000000000000000000000
      ------------------------------
        Todos estos para precisión
    
    00000000000000000000000000000,00
    -----------------------------
       Para magnitudes grandes
"""

cajón_con_punto_flotante: float = 123,456

cajón_numerado: int = 123456


# Esos son los tipos de datos por ahora