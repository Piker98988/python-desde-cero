# El tipo bool: muy importante

El tipo bool viene de booleano, ya que hubo un gracioso que se apellidaba bool y este gracioso decidió que todo se podía interpretar como 0 o 1, Falso o verdadero, negativo o positivo... etc.

Esto nos lleva a lo que es un bool en Python: un tipo bool puede tener dos valores: `True` o `False`.

```python
verdadero: bool = True

falso: bool = False
```

Esto quiere decir que podemos usar otros tipos de datos como booleanos, como mencioné
en [la lección anterior](./007_trabajar_con_int.md), las operaciones lógicas devuelven siempre un booleano, por tanto, nos sirven de ejemplo perfecto:

```python
operacion_or: bool = True or False 

operacion_and: bool = True and False

operación_not: bool = not True
```

> [!TIP]
> Para interpretar estas operaciones, es simplemente lógica. `A or B` quiere decirte que si `A` o `B` son o equivalen a `True`, la sentencia `A or B` es igual a `True`.

## OR

`True or False` ->
Hay un True, por tanto la expresión "True or False" es verdadera ->
`True`

## AND

`True and False` ->
Los dos tienen que ser true, si no, es false ->
`False`

## NOT

`not True` ->
Literalmente no true, es decir, false ->
`False`

## Dinamismo

> [!TIP]
> Python tiene la capacidad de traducir cualquier tipo de dato, es decir, cadenas, int, etc. en un bool.

```python
booleano_cadena: bool = ""
booleano_verdadero: bool = "hola"
```

### Equivalencias String

- False = "" (cadenas vacías)
- True  = "a" (cualquier cadena con algo dentro)

Por tanto, una `str` es `True` si contine  algún texto dentro, si está vacía, es `False`.

### Equivalencias Int

- False = 0 (valor 0)
- True  = 256 (cualquier valor que no sea 0)

> [!IMPORTANT]
> Estas equivalencias se aplican al tipo `float` también.

Un `int` es `True` si es diferente a 0, si es exactamente 0, es `False`.

### Tipo List

- False = [] (una lista vacía)
- True  = ["a", "b"] (lista con cualquier elemento de cualquier longitud)

> [!NOTE]
> Aunque todavía no hemos visto listas, éstas se crean usando corchetes (`[]`) con elementos dentro; estos elementos separados por comas: `[a, b]`

Entonces, una lista vacía o sin elementos es equivalente a `False`, mientras que una lista poblada, es decir, con elementos, es igual a `True`.
