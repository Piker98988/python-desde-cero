# Interactuar con el usuario II

Ahora que hemos visto las funciones, **vamos a ver otra**: `input()`. `input()` es una función builtin que llama a stdin para **tomar la entrada del usuario**. Recuerdas [las funciones](003_in_out_1.md)? Pues esta sí que **nos devuelve algo**: una **cadena**. Esta cadena será **la entrada del usuario**, incluso con el *caracter de final de línea*.

```python
input("Cómo te llamas? ")
```

## Funcionalidad

Por **sí sola** la función no vale mucho, pero cuando usamos **una variable** para **guardar** lo que **nos escribe el usuario**, empieza a resultar muy **útil**:

```python
nombre: str = input("Cómo te llamas? ")
```

Lo que estamos haciendo es preguntar al usuario por su nombre, es decir, la pregunta que le va a salir a nuestro usuario final va a ser el texto que le pasemos a nuestra función `input()`.

Cuando el usuario ponga su nombre y **le de enter**, la parte del código que dice `input()` se **transformará en lo que sea que haya escrito nuestro usuario por consola**.

Esto quiere decir que lo que sea que el usuario nos **responda** lo guardaremos para usarlo **como queramos** en la variable `nombre`.

En esencia, `input()` es una función que nos permite **pedirle una entrada** al usuario, para **interactuar con él**.

## Reto

Aunque no hayamos visto [operadores aritméticos](006_int.md), intenta escribir un programa de calculadora, el cual le pida la entrada al usuario dos veces y luego te dé ese mismo número sumado. **Continúa cuando hayas resuelto el ejercicio.** Tienes una solución con los conocimientos que hemos ganado en el [siguiente archivo](005_solucion.py).
