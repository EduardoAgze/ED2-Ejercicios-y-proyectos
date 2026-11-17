# Ejercicio 1 — ADT Árbol Binario de Búsqueda

Implementación del **Tipo de Dato Abstracto Árbol Binario de Búsqueda (ABB)**
con sus operaciones básicas y sus tres recorridos.

## Archivos

| Archivo | Contenido |
|---|---|
| `nodo.py` | Clase `Nodo`: valor y referencias a los hijos izquierdo y derecho, con propiedades (getters/setters) |
| `arbolbinario.py` | Clase `ArbolBinario`: operaciones del ADT y recorridos |
| `main.py` | Demostración en consola de todas las operaciones |
| `__init__.py` | Expone `Nodo` y `ArbolBinario` como paquete reutilizable |

## Operaciones del ADT

| Operación | Descripción | Complejidad promedio |
|---|---|---|
| `es_vacio()` | Indica si el árbol no tiene raíz | O(1) |
| `raiz` | Propiedad que consulta (y asigna) el nodo raíz | O(1) |
| `EsHoja()` | Indica si la raíz no tiene hijos | O(1) |
| `insertar(valor)` | Inserta respetando el orden del ABB (menores a la izquierda, mayores o iguales a la derecha) | O(log n) |
| `buscar(valor)` | Indica si el valor existe en el árbol | O(log n) |
| `eliminar(valor)` | Elimina un valor y devuelve `True` si existía | O(log n) |
| `altura()` | Número de niveles del árbol (0 si está vacío) | O(n) |
| `PreOrden()` | Raíz → izquierdo → derecho | O(n) |
| `InOrden()` | Izquierdo → raíz → derecho (en un ABB devuelve los valores ordenados) | O(n) |
| `PostOrden()` | Izquierdo → derecho → raíz | O(n) |
| `construir_desde_posfija(...)` | Construye un árbol a partir de una expresión en notación posfija | O(n) |

> Las complejidades son las de un árbol balanceado. En el peor caso (árbol
> degenerado) las operaciones de búsqueda, inserción y eliminación son O(n).

### Casos de eliminación

`eliminar` cubre los tres casos clásicos:

1. **Nodo hoja:** se desconecta del padre.
2. **Nodo con un hijo:** el hijo ocupa el lugar del nodo eliminado.
3. **Nodo con dos hijos:** se reemplaza por el menor valor de su subárbol
   derecho (sucesor inorden) y luego se elimina ese sucesor.

## Cómo ejecutar

```bash
python3 Ejercicios/adt_arbol/main.py
```

## Salida esperada (resumen)

```text
=== ADT Árbol Binario de Búsqueda ===

--- Árbol recién creado ---
¿Está vacío?      : True
Raíz              : None
Altura            : 0

--- Después de insertar 50, 30, 70, 20, 40, 60, 80 ---
¿Está vacío?      : False
Raíz              : 50
Altura            : 3
Preorden          : 50 30 20 40 70 60 80
Inorden           : 20 30 40 50 60 70 80
Postorden         : 20 40 30 60 80 70 50
```

## Notas de diseño

- Los atributos se guardan como `_valor`, `_izquierdo` y `_derecho`, y se
  acceden mediante propiedades para mantener el encapsulamiento.
- La inserción y la búsqueda son recursivas; la eliminación devuelve la nueva
  raíz de cada subárbol para reconectar el árbol en una sola pasada.
