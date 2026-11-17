# Ejercicio 3 — Reordenamiento de un árbol

Convierte un **Árbol Binario de Búsqueda desbalanceado** en un árbol
**balanceado** con exactamente los mismos valores.

## ¿Por qué reordenar?

Un ABB se degenera cuando los valores se insertan en orden:

```text
Insertar 10, 20, 30, 40, 50, 60, 70

10
 └── 20
      └── 30
           └── 40
                └── 50
                     └── 60
                          └── 70
```

El árbol se comporta como una lista enlazada: su altura es **7** y buscar el
último valor requiere recorrer todos los nodos, es decir, O(n).

## Algoritmo

1. **Recorrido inorden:** en un ABB devuelve los valores ordenados de menor a
   mayor → `[10, 20, 30, 40, 50, 60, 70]`.
2. **Elegir el valor central** del arreglo como raíz → `40`.
3. **Dividir y repetir:** el segmento izquierdo `[10, 20, 30]` forma el
   subárbol izquierdo y el derecho `[50, 60, 70]` el subárbol derecho,
   aplicando el mismo criterio de forma recursiva.

```text
              40
           /      \
         20        60
        /  \      /  \
      10   30    50   70
```

Resultado: la altura baja de **7 a 3** y las búsquedas pasan a O(log n).

## Archivo

| Archivo | Contenido |
|---|---|
| `reordenamiento.py` | `valores_inorden`, `construir_balanceado`, `reordenar`, `esta_balanceado` y la demostración |

## Funciones

| Función | Descripción |
|---|---|
| `valores_inorden(arbol)` | Obtiene los valores ordenados del ABB |
| `construir_balanceado(valores, inicio, fin)` | Construye recursivamente un ABB balanceado a partir de una lista ordenada |
| `reordenar(arbol)` | Devuelve un nuevo `ArbolBinario` balanceado con los mismos valores |
| `esta_balanceado(arbol)` | Verifica que cada nodo tenga subárboles con diferencia de altura ≤ 1 |
| `mostrar_arbol(arbol, titulo)` | Imprime altura, balanceo, recorridos y estructura indentada |

## Cómo ejecutar

```bash
python3 Ejercicios/reordenamiento_arbol/reordenamiento.py
```

## Salida esperada (resumen)

```text
=== Árbol original (desbalanceado) ===
Altura           : 7
¿Balanceado?     : False
Inorden          : 10 20 30 40 50 60 70

=== Árbol reordenado (balanceado) ===
Altura           : 3
¿Balanceado?     : True
Preorden         : 40 20 10 30 60 50 70
Inorden          : 10 20 30 40 50 60 70
Estructura:
- 40
    - 20
        - 10
        - 30
    - 60
        - 50
        - 70
```

El recorrido inorden no cambia: el árbol conserva los mismos valores y el
orden del ABB. Solo cambia su forma.

## Complejidad

- Recorrido inorden: **O(n)**.
- Construcción del nuevo árbol: **O(n)** (una visita por nodo, sin búsquedas).
- Total: **O(n)** en tiempo y **O(n)** en memoria adicional.

> `reordenar` construye un árbol nuevo en lugar de modificar el original. Si
> se desea reutilizar el mismo objeto, basta con asignar
> `arbol.raiz = nuevo.raiz`.
