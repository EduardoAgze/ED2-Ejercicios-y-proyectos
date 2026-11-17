"""
Autor:    Vargas Pantoja Luis Eduardo
Título:   Reordenamiento de un árbol binario de búsqueda (ABB).
Version:  1.0.0
Fecha:    17/11/2026

Un ABB puede quedar desbalanceado si los valores se insertan en orden. Este
ejercicio toma ese árbol, obtiene sus valores ordenados con un recorrido
inorden y los vuelve a insertar eligiendo siempre el valor central como raíz,
de modo que la nueva altura sea mínima (árbol balanceado).
"""
import os
import sys

# Permite ejecutar el archivo directamente:
# python Ejercicios/ejercicio3_reordenamiento_arbol/reordenamiento.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ejercicio1_adt_arbol import ArbolBinario, Nodo  # noqa: E402


def valores_inorden(arbol):
    """Devuelve los valores del árbol ordenados de menor a mayor.

    Aprovecha que el recorrido inorden de un ABB visita sus nodos en orden.

    Args:
        arbol (ArbolBinario): Árbol del que se obtienen los valores.

    Returns:
        list: Valores ordenados.
    """
    return [int(valor) for valor in arbol.InOrden().split()]


def construir_balanceado(valores, inicio=0, fin=None):
    """Construye un ABB balanceado a partir de una lista ordenada.

    El valor central de cada segmento se convierte en la raíz, y los segmentos
    izquierdo y derecho se procesan de forma recursiva.

    Args:
        valores (list): Valores ordenados de menor a mayor.
        inicio (int): Índice inicial del segmento (inclusive).
        fin (int): Índice final del segmento (inclusive).

    Returns:
        Nodo: Raíz del subárbol construido, o None si el segmento está vacío.
    """
    if fin is None:
        fin = len(valores) - 1
    if inicio > fin:
        return None

    medio = (inicio + fin) // 2
    nodo = Nodo(valores[medio])
    nodo.izquierdo = construir_balanceado(valores, inicio, medio - 1)
    nodo.derecho = construir_balanceado(valores, medio + 1, fin)
    return nodo


def reordenar(arbol):
    """Reordena un ABB para que quede balanceado.

    Args:
        arbol (ArbolBinario): Árbol original (puede estar desbalanceado).

    Returns:
        ArbolBinario: Nuevo árbol con los mismos valores y altura mínima.
    """
    valores = valores_inorden(arbol)

    nuevo = ArbolBinario()
    nuevo.raiz = construir_balanceado(valores)
    return nuevo


def esta_balanceado(arbol):
    """Comprueba si el árbol cumple la condición de árbol balanceado.

    Un árbol está balanceado si, en cada nodo, la diferencia de altura entre
    sus subárboles izquierdo y derecho no supera 1.

    Args:
        arbol (ArbolBinario): Árbol que se desea comprobar.

    Returns:
        bool: True si está balanceado en todos sus nodos.
    """
    return _esta_balanceado_recursivo(arbol.raiz)


def _esta_balanceado_recursivo(nodo):
    """Versión recursiva de la comprobación de balanceo."""
    if nodo is None:
        return True

    altura_izquierda = _altura(nodo.izquierdo)
    altura_derecha = _altura(nodo.derecho)
    if abs(altura_izquierda - altura_derecha) > 1:
        return False

    return _esta_balanceado_recursivo(nodo.izquierdo) and _esta_balanceado_recursivo(nodo.derecho)


def _altura(nodo):
    """Devuelve la altura de un subárbol (0 si está vacío)."""
    if nodo is None:
        return 0
    return 1 + max(_altura(nodo.izquierdo), _altura(nodo.derecho))


def mostrar_arbol(arbol, titulo):
    """Imprime el árbol de forma indentada junto con sus recorridos."""
    print(f"\n=== {titulo} ===")
    print(f"Altura           : {arbol.altura()}")
    print(f"¿Balanceado?     : {esta_balanceado(arbol)}")
    print(f"Preorden         : {arbol.PreOrden()}")
    print(f"Inorden          : {arbol.InOrden()}")
    print(f"Postorden        : {arbol.PostOrden()}")
    print("Estructura:")
    _imprimir_nodos(arbol.raiz)


def _imprimir_nodos(nodo, nivel=0):
    """Recorre el árbol en preorden mostrando la profundidad de cada nodo."""
    if nodo is None:
        return
    print(f"{'    ' * nivel}- {nodo.valor}")
    _imprimir_nodos(nodo.izquierdo, nivel + 1)
    _imprimir_nodos(nodo.derecho, nivel + 1)


if __name__ == "__main__":
    # Insertar valores en orden creciente genera un árbol degenerado (una lista).
    desbalanceado = ArbolBinario()
    for valor in range(10, 80, 10):
        desbalanceado.insertar(valor)

    mostrar_arbol(desbalanceado, "Árbol original (desbalanceado)")

    balanceado = reordenar(desbalanceado)
    mostrar_arbol(balanceado, "Árbol reordenado (balanceado)")

    print(
        "\nResultado: la altura pasó de "
        f"{desbalanceado.altura()} a {balanceado.altura()} "
        "sin cambiar los valores del árbol."
    )
