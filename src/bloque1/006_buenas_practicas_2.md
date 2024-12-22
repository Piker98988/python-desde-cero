# Buenas prácticas II

## Usar `sys.stdin.readline()` en vez de `input()`

### Comportamiento

Esta función no se comporta igual que `input()`, lo cual debemos de tener en cuenta siempre que la usemos. Cuando usas `sys.stdin.readline()` tienes que tener en cuenta que estás capturando la línea entera, que significa que también estás leyendo la pregunta que le hiciste al usuario. Por ello, debemos de hacer un `sys.stdout.flush()` entre lecturas y escrituras como [mencionamos antes](004_buenas_practicas_1.md).

### Ejemplos

#### Uso común

```python
import sys

sys.stdout.write("Cómo te llamas? ")
sys.stdout.flush()

nombre: str = sys.stdin.readline()
```

> [!NOTE]
> En este código, preguntamos al usuario cómo se llama usando `stdout`, hacemos un `flush()`, y finalmente guardamos su entrada en la variable `nombre`.
