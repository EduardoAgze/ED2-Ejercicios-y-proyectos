# Ejercicio 3 — Reordenamiento de un árbol

Convierte un árbol binario de búsqueda **desbalanceado** en uno **balanceado**
con los mismos valores.

Un ABB se desbalancea cuando los valores se insertan en orden: el árbol queda
como una lista y su altura crece hasta ser igual al número de nodos.

```text
Árbol desbalanceado          Árbol balanceado
10                                  40
 └── 20                          /      \
      └── 30                  20          60
           └── 40           /   \       /   \
                └── 50     10    30    50    70
                     └── 60
                          └── 70
```

## Algoritmo

1. Recorrer el árbol en inorden para obtener los valores ordenados.
2. Elegir el valor central del arreglo como raíz.
3. Repetir el proceso con la mitad izquierda y la mitad derecha.

Así, cada subárbol recibe una cantidad de valores lo más parecida posible y la
altura se reduce al mínimo.

## Funciones

| Función | Qué hace |
|---|---|
| `valores_inorden(arbol)` | Obtiene los valores ordenados |
| `construir_balanceado(valores, inicio, fin)` | Construye el árbol balanceado |
| `reordenar(arbol)` | Devuelve un árbol nuevo, balanceado |
| `esta_balanceado(arbol)` | Comprueba que la diferencia de alturas sea ≤ 1 |
| `mostrar_arbol(arbol, titulo)` | Muestra altura, recorridos y estructura |

## Notas

- Los valores y el recorrido inorden no cambian; solo cambia la forma del árbol.
- En la demostración, la altura pasa de 7 a 3.
- El algoritmo es O(n) en tiempo y usa O(n) de memoria adicional.
