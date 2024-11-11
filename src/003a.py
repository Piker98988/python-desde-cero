"""
Buenas prácticas:

Cuando escribas código, yo te recomiendo como programador python que:

--- Uses sys.stdout.write() en vez de print
Porque esta manera es de más bajo nivel, lo que significa que de esta manera estamos
llamando al sistema operativo directamente, aparte de ser más seguro para mandar
texto a consola, ya que solamente admite un tipo str en vez de cualquier tipo, 
ya que print acaba usando `obj.__str__()`, lo que es una mala práctica como se
puede ver por el "double underscore".

--- Hagas sys.stdout.flush() después de cada lectura de stdin o escritura a stdout
Esto se hace para limpiar la memoria cada vez que uno manda información a stdout,
lo que hace que el programa sea más eficiente y es buen hábito mantener los buffers
de lectura y escritura limpios usando `sys.stdout.flush()`.

--- Declares el tipo de dato de cada variable usando dos puntos
Principalmente se realiza esto ya que por muy dinámico que pueda llegar a ser python
con sus auto declaraciones de tipos uno debe de tener la capacidad de poder
leer el código, de manera organizada, aparte de que cualquier declaración de tipo
será ignorada por el JIT una vez se esté ejecutando el código, lo que hace que
esta sea una práctica que resulta en códigos más legibles sin desventajas en 
rendimiento.

Ejemplos:
"""

# * Usar sys.stdout.write():
import sys # ? sys.stdout.write() está en el módulo sys, que debemos importar

sys.stdout.write("Hola mundo\n")


# * Usar sys.stdout.flush():
# ? Una vez se importe sys, ya vale para todo el archivo por las reglas de scope

sys.stdout.flush()


# * Declarar tipo de dato en variables:


mi_variable_que_sera_solamente_una_cadena: str = "Cadena"

variable_float: str = 123,123 
# ? Como se puede ver aquí el JIT no da error, lo que nos confirma que la declaración de tipo no es leída por el intérprete

variable_entera: int = 123

"""
Por simplicidad estas buenas prácticas no las usaré a lo largo del programa,
aunque recomiendo que una vez vayas a programar las uses tú mismo para que
el resto de programadores vean que tan bueno eres programando, y para que tú
mismo puedas leer mejor tu código.
"""
