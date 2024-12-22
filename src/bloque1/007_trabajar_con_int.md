# Trabajar con Int

Para trabajar con este tipo de dato deberemos de saber que los Int tienen varias operaciones que nos facilita el idioma de programación, estas siendo lógicas y aritméticas.

## Operaciones aritméticas

Estas son las operaciones que trabajan con dos números y proveen un número.

> [!CAUTION]
> La división siempre devuelve un `float` en vez de un `int`, por tanto, cuando hagamos anotaciones, veremos que la declaración de tipo de nuestras divisiones es `float` en vez de `int`.

```python
suma: int = 1 + 1
resta: int = 1 - 1
multiplicación: int = 2 * 2
división: float = 4 / 3
módulo: int = 4 % 2
```

> [!IMPORTANT]
> El módulo de dos números es su resto al dividirlos, en caso de 4 y 2, es 0 ya que la división sale exacta: `4 / 2 = 2`. Si haces esta división a mano no hay resto, por tanto: `4 % 2 = 0`.

## Operaciones lógicas

Éstas son aquellas que al usar dos números, devuelven un *bool* o un *booleano*.

```python
op_or: int = 1 | 2
op_and: int = 1 and 2
op_not: int = not 2
```

> [!NOTE]
> El tipo `booleano` lo veremos en el siguiente archivo, si no lo entiendes todavía, no hay de qué preocuparse.

Estas operaciones nos facilitan el trabajo con estos números, y es tan simple **como usarlas y ya**.

> [!TIP]
> Recuerda que el nombre de una variable es simplemente **una flecha hacia el valor que nosotros definimos**. Si nuestra variable se llama "var", usando var dónde sea, var simplemente **actúa como una dirección de una calle**, donde **lo que se encuentra en esa calle es el valor que le asignamos a var**. ***Es simplemente darle un nombre a un dato***.
