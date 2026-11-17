"""
Autor:    Vargas Pantoja Luis Eduardo
Título:   Demostración del ADT Árbol Binario de Búsqueda.
Version:  1.0.0
Fecha:    17/11/2026

Muestra el uso de las operaciones básicas del ADT: crear el árbol, verificar
si está vacío, consultar la raíz, insertar, buscar, eliminar y recorrerlo en
preorden, inorden y postorden.
"""
import os
import sys

# Permite ejecutar el archivo directamente: python Ejercicios/ejercicio1_adt_arbol/main.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ejercicio1_adt_arbol import ArbolBinario  # noqa: E402


def mostrar_estado(arbol, titulo):
    """Imprime el estado actual del árbol con sus recorridos."""
    print(f"\n--- {titulo} ---")
    print(f"¿Está vacío?      : {arbol.es_vacio()}")
    print(f"Raíz              : {arbol.raiz.valor if arbol.raiz else None}")
    print(f"Altura            : {arbol.altura()}")
    print(f"Preorden          : {arbol.PreOrden()}")
    print(f"Inorden           : {arbol.InOrden()}")
    print(f"Postorden         : {arbol.PostOrden()}")


def main():
    arbol = ArbolBinario()

    print("=== ADT Árbol Binario de Búsqueda ===")
    mostrar_estado(arbol, "Árbol recién creado")

    # Insertar valores: el árbol se ordena automáticamente.
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arbol.insertar(valor)

    mostrar_estado(arbol, "Después de insertar 50, 30, 70, 20, 40, 60, 80")

    # Búsqueda.
    print("\n--- Búsqueda ---")
    for valor in (40, 55):
        encontrado = arbol.buscar(valor)
        print(f"¿Existe {valor}?    : {encontrado}")

    # Eliminación de los tres casos posibles.
    print("\n--- Eliminación ---")
    print(f"Eliminar 20 (hoja)                : {arbol.eliminar(20)}")
    print(f"Eliminar 30 (un hijo)             : {arbol.eliminar(30)}")
    print(f"Eliminar 50 (raíz con dos hijos)  : {arbol.eliminar(50)}")
    print(f"Eliminar 99 (no existe)           : {arbol.eliminar(99)}")

    mostrar_estado(arbol, "Árbol después de las eliminaciones")


if __name__ == "__main__":
    main()
