"""
Autor:    Vargas Pantoja Luis Eduardo
Título:   Expresiones matemáticas de infija a posfija y su representación en un árbol binario (versión de consola).
Version:  1.1.0
Fecha:    31/08/2026
"""
from model.ejercicio_expresiones import (
    ArbolBinario_Expresiones,
    infija_a_posfija,
    validar_expresion,
)


def main():
    expresion = input(
        "Ingrese una expresión matemática (números, + - * / y paréntesis): "
    )

    es_valida, mensaje = validar_expresion(expresion)
    if not es_valida:
        print(f"Expresión inválida: {mensaje}")
        return

    try:
        # 1. Convertir de infija a posfija.
        posfija = infija_a_posfija(expresion)
        print(f"1. Notación posfija:              {posfija}")

        # 2. Crear el árbol binario y armar su estructura.
        arbol = ArbolBinario_Expresiones()
        arbol.construir_desde_posfija(posfija)

        # 3. Mostrar los recorridos y el resultado.
        print(f"2. Recorrido PreOrden del árbol:  {arbol.PreOrden()}")
        print(f"3. Recorrido InOrden del árbol:   {arbol.InOrden()}")
        print(f"4. Recorrido PostOrden del árbol: {arbol.PostOrden()}")
        print(f"5. Resultado de la expresión:     {arbol.evaluar()}")
    except (ValueError, IndexError) as error:
        print(f"Error al procesar la expresión: {error}")


if __name__ == "__main__":
    main()
