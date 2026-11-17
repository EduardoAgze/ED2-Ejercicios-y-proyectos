# Ejercicio 1 — ADT Árbol Binario de Búsqueda

Implementación del Árbol Binario de Búsqueda (ABB) con sus operaciones básicas
y sus tres recorridos.

Los valores menores que un nodo van a su izquierda y los mayores o iguales a su
derecha. Por eso el recorrido inorden devuelve los valores ordenados.

## Archivos

| Archivo | Contenido |
|---|---|
| `nodo.py` | Clase `Nodo`: valor, hijo izquierdo e hijo derecho |
| `arbolbinario.py` | Clase `ArbolBinario` con las operaciones del ADT |
| `main.py` | Demostración de todas las operaciones |
| `__init__.py` | Permite reutilizar el ADT desde los otros ejercicios |

## Operaciones

| Operación | Qué hace |
|---|---|
| `es_vacio()` | Indica si el árbol no tiene raíz |
| `raiz` | Consulta o asigna el nodo raíz |
| `EsHoja()` | Indica si la raíz no tiene hijos |
| `insertar(valor)` | Agrega un valor manteniendo el orden del ABB |
| `buscar(valor)` | Indica si el valor existe |
| `eliminar(valor)` | Elimina un valor y devuelve `True` si existía |
| `altura()` | Cantidad de niveles del árbol |
| `PreOrden()` | Raíz, izquierdo, derecho |
| `InOrden()` | Izquierdo, raíz, derecho |
| `PostOrden()` | Izquierdo, derecho, raíz |
| `construir_desde_posfija(...)` | Construye un árbol desde notación posfija |

## Eliminación

Se resuelve según el nodo que se elimina:

1. **Hoja:** se desconecta de su padre.
2. **Un solo hijo:** el hijo ocupa su lugar.
3. **Dos hijos:** se reemplaza por el menor valor del subárbol derecho.

## Notas

- Los atributos son privados y se acceden mediante propiedades.
- En un árbol balanceado, insertar, buscar y eliminar cuestan O(log n); en el
  peor caso, O(n).
