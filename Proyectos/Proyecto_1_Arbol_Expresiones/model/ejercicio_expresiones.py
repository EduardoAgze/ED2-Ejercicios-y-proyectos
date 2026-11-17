"""
Autor:    Vargas Pantoja Luis Eduardo
Título:   Expresiones matematicas de infija a posfija y su representación en un árbol binario.
Version:  1.0.0
Fecha:    31/08/2026
"""

from model.arbolbinario import ArbolBinario
from model.nodo import Nodo

class ArbolBinario_Expresiones(ArbolBinario):
    """Representa un árbol binario de expresiones matemáticas.

    Attributes:
        raiz: Referencia al nodo raíz del árbol, o None si está vacío.
    """

    def __init__(self):
        super().__init__()

    def grafo(self):
        """Devuelve un objeto Digraph de Graphviz con la estructura del árbol.

        Returns:
            Digraph: Grafo dirigido con los nodos y las aristas del árbol binario.
        """
        # Se importa aquí para que el módulo funcione en consola aunque
        # Graphviz no esté instalado (solo se necesita para generar la imagen).
        from graphviz import Digraph

        dot = Digraph()

        def visitar(nodo, padre_id=None):
            if nodo is None:
                return
            id_actual = str(id(nodo))
            dot.node(id_actual, str(nodo.valor))
            if padre_id:
                dot.edge(padre_id, id_actual)
            visitar(nodo.izquierdo, id_actual)
            visitar(nodo.derecho, id_actual)

        visitar(self.raiz)
        return dot

    def construir_desde_posfija(self, posfija):
        if not posfija:
            self.raiz = None
            return

        pila_nodos = []

        for caracter in posfija:
            nodo = Nodo(caracter)

            if caracter not in "+-*/":
                pila_nodos.append(nodo)
            else:
                if len(pila_nodos) < 2:
                    raise ValueError(
                        f"Expresión inválida: operador '{caracter}' sin suficientes operandos."
                    )
                nodo._derecho = pila_nodos.pop()
                nodo._izquierdo = pila_nodos.pop()
                pila_nodos.append(nodo)

        if len(pila_nodos) != 1:
            raise ValueError("Expresión inválida: sobran operandos sin operador.")

        self.raiz = pila_nodos.pop()

    def evaluar(self):
        """Evalúa la expresión representada por el árbol binario.

        Returns:
            float: Resultado de la evaluación de la expresión.
        """
        return self._evaluar_recursivo(self.raiz)

    def _evaluar_recursivo(self, nodo):
        """Evalúa la expresión de forma recursiva.

        Args:
            nodo: Nodo actual durante el recorrido del árbol.

        Returns:
            float: Resultado parcial de la evaluación.
        """
        if nodo is None:
            return 0

        # Si es una hoja (número), devolver su valor
        if nodo.izquierdo is None and nodo.derecho is None:
            return float(nodo.valor)

        # Evaluar los subárboles izquierdo y derecho
        izquierda = self._evaluar_recursivo(nodo.izquierdo)
        derecha = self._evaluar_recursivo(nodo.derecho)

        # Aplicar el operador del nodo actual a los resultados de los subárboles
        if nodo.valor == '+':
            return izquierda + derecha
        elif nodo.valor == '-':
            return izquierda - derecha
        elif nodo.valor == '*':
            return izquierda * derecha
        elif nodo.valor == '/':
            if derecha == 0:
                raise ValueError("División por cero no permitida.")
            return izquierda / derecha
        else:
            raise ValueError(f"Operador desconocido: {nodo.valor}")


def prioridad(op):
    """Devuelve la jerarquía del operador matemático.

    Args:
        op (str): Operador matemático ('+', '-', '*', '/').

    Returns:
        int: Nivel de prioridad (1 para '+' y '-', 2 para '*' y '/').
    """
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def tokenizar(expresion):
    """Separa una expresión infija en números, operadores y paréntesis.

    Args:
        expresion (str): Expresión infija, por ejemplo ``3*(4.5+2)``.

    Returns:
        list: Tokens de la expresión. Los números se devuelven como cadenas
        para conservar su escritura original.

    Raises:
        ValueError: Si aparece un carácter no permitido.
    """
    tokens = []
    numero_actual = ""

    for posicion, caracter in enumerate(expresion, start=1):
        if caracter.isdigit() or caracter == '.':
            numero_actual += caracter
        elif caracter in "+-*/()":
            if numero_actual != "":
                tokens.append(numero_actual)
                numero_actual = ""
            tokens.append(caracter)
        elif caracter.isspace():
            continue
        else:
            raise ValueError(f"Carácter no permitido: '{caracter}' (posición {posicion})")

    if numero_actual != "":
        tokens.append(numero_actual)

    return tokens


def infija_a_posfija(expresion):
    """Convierte una expresión matemática de notación infija a posfija.

    Usa el algoritmo de Shunting Yard, que respeta la prioridad de los
    operadores y los paréntesis.

    Args:
        expresion (str): Expresión matemática en notación infija.

    Returns:
        list: Tokens de la expresión en notación posfija.

    Raises:
        ValueError: Si la expresión no está bien formada.
    """
    salida = []
    pila_operadores = []

    for token in tokenizar(expresion):
        if token not in "+-*/()":
            # Es un operando.
            salida.append(token)
        elif token == '(':
            pila_operadores.append(token)
        elif token == ')':
            # Desapilar hasta encontrar el paréntesis de apertura.
            while pila_operadores and pila_operadores[-1] != '(':
                salida.append(pila_operadores.pop())
            if not pila_operadores:
                raise ValueError("Paréntesis desbalanceados: sobra un ')'.")
            pila_operadores.pop()
        else:
            # Desapilar operadores con prioridad >= al operador actual.
            while (
                pila_operadores
                and pila_operadores[-1] != '('
                and prioridad(pila_operadores[-1]) >= prioridad(token)
            ):
                salida.append(pila_operadores.pop())
            pila_operadores.append(token)

    while pila_operadores:
        operador = pila_operadores.pop()
        if operador == '(':
            raise ValueError("Paréntesis desbalanceados: falta un ')'.")
        salida.append(operador)

    return salida


def validar_expresion(expresion):
    """Valida que una expresión infija esté bien formada antes de convertirla.

    Reglas comprobadas:
      - Solo se permiten dígitos, punto decimal, ``+ - * /``, paréntesis y espacios.
      - Los números deben ser válidos (por ejemplo, ``1.5``).
      - Operandos y operadores deben alternarse correctamente.
      - Los paréntesis deben estar balanceados y no vacíos.

    Args:
        expresion (str): Expresión matemática en notación infija.

    Returns:
        tuple: ``(es_valida, mensaje)``.
    """
    texto = (expresion or "").strip()
    if not texto:
        return False, "La expresión está vacía."

    try:
        tokens = tokenizar(texto)
    except ValueError as error:
        return False, str(error)

    if not tokens:
        return False, "La expresión está vacía."

    espera_operando = True
    profundidad = 0

    for token in tokens:
        if token == '(':
            if not espera_operando:
                return False, "Falta un operador antes de '('."
            profundidad += 1
            espera_operando = True

        elif token == ')':
            if espera_operando:
                return False, "Falta un operando antes de ')'."
            profundidad -= 1
            if profundidad < 0:
                return False, "Paréntesis desbalanceados: sobra un ')'."
            espera_operando = False

        elif token in "+-*/":
            if espera_operando:
                return False, f"Operador '{token}' en una posición inesperada."
            espera_operando = True

        else:
            if not espera_operando:
                return False, f"Falta un operador antes de '{token}'."
            try:
                float(token)
            except ValueError:
                return False, f"Número inválido: '{token}'."
            espera_operando = False

    if profundidad != 0:
        return False, "Paréntesis desbalanceados: falta un ')'."
    if espera_operando:
        return False, "La expresión no puede terminar con un operador o '('."

    return True, ""

