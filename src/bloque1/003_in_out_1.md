# Interactuar con el usuario I

Para interactuar con el usuario, por ejemplo, **decirle cosas**, usaremos **la fabulosa función `print()`**. Esta función es un *builtin*, que quiere decir que es *built-in*. Esto significa que **lo uses donde lo uses va a funcionar**, porque está ***embebida* en el propio lenguaje**. Todo lo que tenga **paréntesis al final**, es una ***función***: `print()`. Todo lo que **empiece por un punto** y luego **tenga un paréntesis**, es un ***método***: `.upper()`.

```python
print("Función print")
"método capitalize".capitalize()
# Se puede ver que tienen colores diferentes resaltados por tu editor
```

## ¿Qué es una función?

En este código podemos ver cómo usamos **la función print**. Las funciones se pueden comparar con *máquinas*; **máquinas en las que introducimos algo y hace algo con ese mismo algo**. Es decir, si tu tienes una función f(x), esta misma función **te devolverá resultados diferentes dependiendo de x**, lo que básicamente se puede **comparar con una máquina**. Digamos que:

$$
f(x) = x + 1
$$

Entonces, esto querría decir que si nosotros **ponemos 1** en la máquina $f(x)$, **saldrá 2**, para representar esto, decimos $f(1)$:

$$
f(1) = 1 + 1 = 2
$$

## Funciones aplicadas a print

En caso de `print()`, nosotros **introducimos una cadena**, la cual será manipulada y
**se mandará a `stdout`**, es decir, **la salida de texto del programa**:

$$
print(x) = mandar - a - consola - x
$$

La función `print()` ***no* nos devuelve nada**, solamente ***usa* ese valor** que nosotros le proporcionamos para **mandarlo a `stdout`**. A medida que avancemos iremos encontrando **otras funciones** que, en vez de eso, nos *devuelven* un valor **aparte de manipularlo**, o simplemente **nos devuelven uno sin que nosotros le tengamos que proporcionar nada**.

## Referenciación

```python
cajón: str = "mi variable cajón"

print(cajón)
```

Aquí podemos ver cómo ***referenciamos*** la variable `cajón`, es decir, le pasamos como *parámetro* a **la función `print()`** la variable `cajón`. Se podría decir que las variables son como **flechas a valores** que nosotros elegimos cuando las estamos **definiendo** usando el **operador de asignación** *"$=$"*.

Recuerda que si algo no se entiende correctamente, **eres libre de abrir un issue en la página de GitHub**.

**Ahora pasamos a [buenas prácticas](buenas_practicas_1.md).**