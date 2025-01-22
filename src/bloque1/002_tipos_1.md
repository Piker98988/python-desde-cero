# Tipos de datos I

Python como lenguaje tiene varias cosas que podemos guardar en nuestros cajones, los cuales se llaman *"tipos de datos"*. Estos tipos **se te irán quedando con el tiempo**, ya que son **extremadamente importantes** para entender errores y como Python **trata los diferentes valores y objetos que guardemos en variables**. Los tipos de datos básicos en Python son los siguientes:

## Tipos básicos

- String
- [Int](./007_trabajar_con_int.md)
- Float
- [List](listas_1.md)
- [Boolean](./008_tipo_bool.md)

### String

String viene de **cadena en inglés**. En programación, no llamamos a las frases *"frases"*, si no que las llamamos **cadenas**. **Cualquier texto puede ser una cadena**, ya que de ahí viene el nombre, *cadena de caracteres*. Python lo llama ***"str"***, y para crearlo tenemos que rodear **cualquier** texto con comillas dobles o simples:

```python
"cadena"
'cadena también'
```

> [!NOTE]
> Cualquier texto rodeado entre comillas se le llamará cadena o string a partir de ahora, ya que el estándar de hoy en día se basa en instancias de objetos, cuando tengamos una cadena, la llamaremos *instancia del tipo string*. En programación orientada a objetos entenderemos por qué lo llamamos así.

### Int

Los Int toman su nombre del inglés **integer**, que **traducido al español es *entero***. Un *entero* se refiere al número, es decir, al **número entero**, el cual puede ser **negativo y positivo**, pero **nunca racional**, es decir, **siempre sin decimales**. Este tipo de dato Python lo llama *"int"*, y **se determina con un simple número**, sin ningún añadido:

```python
1
12345
7890293741234986192387
-4569
```

> [!NOTE]
> En caso de los ints, se aplica lo mismo, cualquier número en python (que no forme parte de una cadena) es una *instancia* del tipo **int**.

### Float

Float viene de **la coma de los números racionales**, ya que esta es una *coma flotante*, la cual podemos ir rotando a lo largo de **32 bits de espacio binario**:

```python
0000000000000000000000000000.000
```

Es una coma flotante porque la podemos mover a dónde sea en esa representación binaria, **cualquiera de esos ceros puede ser la coma**, lo que quiere decir que podemos tener más números a la izquierda **para magnitudes grandes** o más números a la derecha **para precisión**:

```python
00.00000000000000000000000000000
   -----------------------------
    Todos estos para precisión

00000000000000000000000000000.00
-----------------------------
    Para magnitudes grandes
```

### Booleano

Los tipos booleanos aparecen por el álgebra de bool, pronunciado "buul" o "buleano". Estos tipos representan *Sí* o *No*, **"Verdadero"** o **"Falso"**. Las palabras reservadas `True` y `False` representan estos valores. En python se los llama **`bool`**.

```python
verdadero = True
falso = False
```

## Sintaxis

Podemos especificar lo que queremos que haya en una variable poniendo **dos puntos y el tipo que queramos** antes de darle un valor a nuestra variable, es decir, **entre el operador y el nombre**, tal que así:

```python
cajón: str = "Calcetines"
```

Ahora, podemos usar `cajón` **donde queramos**, aunque le hemos dicho que **es un `str`**, que viene de `string`. Cada tipo **significa una cosa diferente**:

```python
cajón_con_punto_flotante: float = 123.456

cajón_numerado: int = 123456

cajón_de_mentira: bool = False
```

Esos son los tipos de datos **por ahora**. Ahora veremos [cómo interactuar con el usuario de forma básica](003_in_out_1.md).
