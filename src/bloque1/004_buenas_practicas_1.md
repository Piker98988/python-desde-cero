# Buenas prácticas I

Cuando escribas código, yo te recomiendo como programador Python varias cosas, las cuales te van a ayudar a esto:

- Parecer mejor programador aunque no tengas ni idea
- Entender mejor tu propio código
- Ayudar a otros a entender tu código

## Usar `sys.stdout.write()` en vez de `print()`

Esta manera es de **más bajo nivel**, lo que significa que de esta manera estamos **llamando al sistema operativo directamente**, aparte de ser **más seguro para mandar texto a consola**, ya que **solamente admite un tipo `str`** en vez de cualquier tipo.

### Pequeño paréntesis

Más adelante veremos los objetos y cómo crear nuestras propias clases, pero para introducir, voy a decir que todos los literales, es decir, todo lo que puedas llamar "literal", es un objeto instanciado en memoria, el cual tiene sus propios atributos accesibles a través de métodos.

Uno de esos atributos es `.__str__()`, que cuando lo llamas te devuelve una representación que el programador de ese objeto ha dicho que debe de ser así, es decir, si tu tienes una clase que se llama *"perro"* con varios atributos como "edad", "nombre", etcétera, y has instanciado en memoria un objeto con el nombre *`mi_perrito`*, el programador puede decir que cuando tú hagas `mi_perrito.__str__()`, salga en consola con un formato lo que sea, es decir, puedes decir que salga cualquier cosa, y cuando digo cualquier cosa es cualquiera.

Un buen programador dirá que en este método, tomando el ejemplo de antes, se te devuelva los atributos del objeto instanciado para proporcionar información sobre ese mismo objeto, por ejemplo, cuando tu llames `mi_perrito.__str__()` se te va a devolver algo como `"Perro con nombre "(nombre del perro)" y edad (edad del perro)"`.

### Razones

Una vez explicado eso, voy a continuar diciendo que `print()` usa `obj.__str__()` para **cualquier** cosa que le des, **como por ejemplo un `int`**. Cuando usas `sys.stdout.write()`, si le pasas un `int` **te da error**, ya que esto **no es un `str`**.

Desde mi punto de vista, `sys.stdout.write()` es una manera **mucho mejor** de paliar la necesidad de **mandar información a consola** por **seguridad** y esas cosas; aparte, `print()` **pone un salto de línea al final**, y `sys.stdout.write()` **no**, lo que ya **es una ventaja** de por sí, ya que **te da más control sobre cómo quieres que python haga las cosas**.

Si quieres usar la funcionalidad del `print()` dentro de `sys.stdout.write()` lo que debes de hacer el simplemente llamar el método `.__str__()` de lo que sea que quieras mandar.

### Ejemplos

#### Uso común

```python
import sys 
# sys.stdout.write() está en el módulo sys, que debemos importar

sys.stdout.write("Hola mundo\n")
```

#### Usar `sys.stdout.write()` como `print()`

```python
import sys

mi_variable: int = 2

sys.stdout.write(mi_variable) # esta línea debería de dar error
sys.stdout.write(mi_variable.__str__()) # esta ya no, mandaría a consola "2"
```

## Hacer un flush

Después de cada [lectura de stdin](006_buenas_practicas_2.md) o escritura a stdout existe un "buffer" de memoria que guarda lo que has mandado, es decir, cuando haces una llamada a `sys.stdout.write("hola")`, se llena el buffer de escritura con el texto "hola", lo cual afecta luego a cómo el ordenador procesará la entrada de datos. Esto se hace para limpiar la memoria cada vez que uno manda información a stdout, lo que hace que el programa sea más eficiente y es buen hábito mantener los buffers de lectura y escritura limpios usando `sys.stdout.flush()`.

De momento no es extremadamente útil más allá de querer parecer un super técnico en programación, pero cuando lleguemos a [stdin](006_buenas_practicas_2.md) nos servirá enormemente para poder leer lo que ocurre bien.

### Ejemplos

#### Flush después de escritura

```python
import sys

sys.stdout.write("hola")

sys.stdout.flush()
```

#### [Flush entre escritura y lectura](006_buenas_practicas_2.md)

## Declarar el tipo de dato de cada variable

Principalmente se realiza esto ya que **por muy dinámico que pueda llegar a ser Python con sus auto-declaraciones de tipos uno debe de tener la capacidad de poder leer el código**, a lo cual ayuda que este mismo esté escrito de **una manera organizada**, aparte de que cualquier declaración de tipo **será ignorada por el compilador JIT** una vez se esté ejecutando el código, lo que hace que esta sea una práctica que resulta en **códigos más legibles sin desventajas en rendimiento**.

Para python (el compilador JIT), estas declaraciones **no existen**, así que si las escribimos mal el compilador JIT **no va a dar error**.

### Ejemplos

#### Cadenas

```python
mi_variable_que_sera_solamente_una_cadena: str = "Cadena"
```

#### Números

```python
variable_entera: int = 123

variable_float: float = 123.123
```

#### Al compilador le da igual

```python
variable_entera: str = 123
# Si ejecutas este código en el REPR de python, verás que el compilador no te dará error.
```

## Nombres descriptivos

Cuando escribes código, como he mencionado antes, es vital que tu yo del futuro pueda entender este código para que cuando surjan errores puedas depurarlo de manera cómoda. Esto se hace con nombres descriptivos.

Con nombres descriptivos no me refiero a "variable_cadena", si no que me refiero a un nombre que describa **exactamente** lo que vas a hacer con esa variable, es decir, un nombre que nada más leerlo yo pueda saber para qué es la variable.

### Anexo

Las variable escritas en mayúsculas se interpretan como constantes. Al compilador le da igual, y le da el mismo trato dinámico que al resto, es decir, que aunque yo te diga que las variables en mayúsculas son constantes, tú puedes modificar su valor igual.

Python no cuenta con una funcionalidad como las constantes. En otros idiomas de programación, antes de definir tu variable, puedes pasarle parámetros, como "público", "global" y "constante". En python eso no existe, por tanto, las constantes como tal no existen.

Cuando leas código y veas una variable toda en mayúsculas, quiere decir que el desarrollador de esa aplicación nunca cambiará el valor de esa variable.

### Ejemplos

#### Abreviaciones

```python
import sys

# Código malo
p: str = "persona"
n: int = 33

sys.stdout.write(p + n.__str__())
```

```python
import sys

# Código bueno
nombre_persona: str = "persona"
edad_persona: int = 33

sys.stdout.write(nombre_persona + edad_persona.__str__())
```

#### Malos nombres

```python
# nombre malo
mi_variable_que_siempre_va_a_ser_una_cadena_y_no_va_a_cambiar: str = "cadena"

# nombre mid
cadena_1: str = "cadena"

# nombre bueno
STR_CADENA_1: str = "cadena"
```

## Dejar comentarios

Los comentarios están en **todos** los idiomas de programación, aunque pienses que **son inútiles**. Si están, es por algo, y esta razón se debe a que uno normalmente no desarrolla un programa completo **por si solo**, si no que lo desarrolla **en grupo**. Estos fieles compañeros que estén en tu grupo **son humanos como tú**, y con esto te quiero decir que pueden no entender partes de tu código. Por ello, te recomiendo **dejar comentarios** y ***docstrings***.

### Ejemplos

#### Explicaciones

```python
print("hola")
# (he usado print porque) necesitaba hacerlo rápido
```

#### TO DO

Aclaración: los TODO en comentarios los resaltan automáticamente en TODOS los editores por estándar. TODO del inglés "To Do", que significa "por hacer". En la mayoría de editores existe una pestaña específica para los TODOs pendientes, la cual te da una vista global de tus TODOs.

```python
print() # TODO no me acuerdo de qué tenía que hacer
```

#### [Puntos suspensivos](#)

#### Docstrings

Las docstrings se colocan debajo de expresiones, como *variables*, *funciones*, *métodos* y hasta inicios de archivos. La mayoría de editores te permiten colocar tu cursor encima de un nombre, para que te aparezca documentación sobre ello. De ahí el nombre "docstring", de "doc", que es una abreviatura de la palabra "documentation", es decir, "documentación" en inglés y también de "string", "cadena" en español.

##### Inicios de archivo

```python
"""
Este archivo define muchas variables importantes para el resto del programa
"""

...
# Resto del archivo
```

##### Variables

Si colocas tu mouse encima del nombre de la variable, te aparecerá la docstring que hayas escrito. Te animo a que copies el código de aquí, lo pegues en tu IDE de elección y coloques tu cursor del ratón encima del nombre de la variable.

```python
mi_variable: str = "valor"
"""Esta variable guarda un valor cualquiera"""

print(mi_variable)
```

##### [Funciones](#)

## [Pasamos a I/O II](005_in_out_2.md)