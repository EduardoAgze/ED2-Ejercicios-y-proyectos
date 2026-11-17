# Ejercicios

Ejercicios de clase sobre árboles binarios. Todos usan únicamente la
biblioteca estándar de Python y se ejecutan desde la raíz del repositorio o
desde su propia carpeta.

| # | Ejercicio | Carpeta | Qué se practica |
|---|---|---|---|
| 1 | **ADT Árbol** | [`adt_arbol/`](adt_arbol/) | Crear el árbol, verificar si está vacío, consultar la raíz, insertar, buscar, eliminar y recorridos pre/in/postorden |
| 2 | **3 en raya en un árbol** | [`tres_en_raya/`](tres_en_raya/) | Representar un tablero de 3×3 con tres árboles binarios (uno por fila) |
| 3 | **Reordenamiento de un árbol** | [`reordenamiento_arbol/`](reordenamiento_arbol/) | Convertir un ABB desbalanceado en un árbol balanceado sin perder valores |

## Ejecución

```bash
python3 Ejercicios/adt_arbol/main.py
python3 Ejercicios/tres_en_raya/ejercicio_3en_raya.py
python3 Ejercicios/reordenamiento_arbol/reordenamiento.py
```

## Relación entre ejercicios

El paquete `adt_arbol` contiene la implementación base del **Árbol Binario de
Búsqueda** (clases `Nodo` y `ArbolBinario`). Los ejercicios de *3 en raya* y
*reordenamiento* lo reutilizan, de modo que existe una sola implementación del
ADT en todo el repositorio.

```text
adt_arbol/  ──►  tres_en_raya/
     │
     └────────►  reordenamiento_arbol/
```
