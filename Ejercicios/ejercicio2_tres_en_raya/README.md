# Ejercicio 2 — Tres en raya con árboles binarios

El tablero de tres en raya se representa con **tres árboles binarios**, uno por
fila. Cada árbol tiene exactamente tres nodos.

## Representación

```text
            raíz        hijo izq.   hijo der.
Fila 0:    (0,0)    ←     (0,1)   →   (0,2)
Fila 1:    (1,0)    ←     (1,1)   →   (1,2)
Fila 2:    (2,0)    ←     (2,1)   →   (2,2)
```

La columna 0 es la raíz, la columna 1 es el hijo izquierdo y la columna 2 es el
hijo derecho. Cada nodo guarda el símbolo de la casilla: `' '`, `'X'` u `'O'`.

## Métodos

| Método | Qué hace |
|---|---|
| `obtener_nodo(fila, columna)` | Devuelve el nodo de una casilla |
| `obtener_valor(fila, columna)` | Devuelve el símbolo de una casilla |
| `establecer_valor(fila, columna, valor)` | Coloca un símbolo en una casilla |
| `hay_ganador()` | Revisa filas, columnas y diagonales; devuelve el ganador o `None` |
| `mostrar()` | Imprime el tablero en consola |

## Notas

- Los tres árboles son independientes; no hay un árbol que contenga a los demás.
- La partida de ejemplo coloca los símbolos directamente, sin interacción: el
  ejercicio se centra en la estructura de datos.
- Reutiliza `Nodo` y `ArbolBinario` del [ejercicio 1](../ejercicio1_adt_arbol/).
