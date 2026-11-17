# Ejercicio 2 — Tres en raya con árboles binarios

Representación del tablero de **tres en raya (3×3)** usando **tres árboles
binarios**, uno por cada fila. El objetivo es practicar la relación entre una
estructura bidimensional y los nodos de un árbol.

## Representación

Cada fila es un árbol binario con exactamente tres nodos:

```text
        raíz            hijo izquierdo      hijo derecho
Fila 0:   (0,0)     ←       (0,1)      →      (0,2)
Fila 1:   (1,0)     ←       (1,1)      →      (1,2)
Fila 2:   (2,0)     ←       (2,1)      →      (2,2)
```

Por lo tanto, la columna 0 del tablero es la raíz del árbol de esa fila, la
columna 1 es el hijo izquierdo y la columna 2 es el hijo derecho.

## Archivo

| Archivo | Contenido |
|---|---|
| `ejercicio_3en_raya.py` | Clase `Tablero3EnRaya` y una partida de ejemplo |

## Métodos

| Método | Descripción |
|---|---|
| `obtener_nodo(fila, columna)` | Devuelve el nodo que representa esa casilla |
| `obtener_valor(fila, columna)` | Devuelve el símbolo guardado (`' '`, `'X'` u `'O'`) |
| `establecer_valor(fila, columna, valor)` | Coloca un símbolo en una casilla |
| `hay_ganador()` | Revisa las 3 filas, 3 columnas y 2 diagonales; devuelve el símbolo ganador o `None` |
| `mostrar()` | Imprime el tablero en consola |

## Cómo ejecutar

```bash
python3 Ejercicios/tres_en_raya/ejercicio_3en_raya.py
```

## Salida esperada

```text
Tablero final:
O | X |
X | O |
X |   | O

Gana el jugador: O
```

La partida de ejemplo coloca los símbolos directamente con
`establecer_valor`, sin interacción del usuario: el ejercicio se centra en la
**estructura de datos**, no en el bucle de juego.

## Notas

- El tablero se crea con tres árboles independientes; no hay un árbol general
  que contenga a los tres.
- `hay_ganador()` aprovecha la traducción `(fila, columna) → (árbol, nodo)` para
  leer cualquier casilla de forma uniforme.
- La clase reutiliza el ADT `ArbolBinario` y la clase `Nodo` del paquete
  [`adt_arbol`](../adt_arbol/), por lo que no duplica la implementación.
