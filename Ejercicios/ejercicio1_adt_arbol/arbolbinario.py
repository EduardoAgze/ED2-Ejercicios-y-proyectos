"""
Autor:    Vargas Pantoja Luis Eduardo
Título:   Clase ArbolBinario para representar un árbol binario de búsqueda (ABB)
          incluyendo inserción, búsqueda, eliminación y recorridos.
Version:  1.1.0
Fecha:    31/08/2026
"""
from .nodo import Nodo


class ArbolBinario:
    """Representa un árbol binario de búsqueda (ABB).

    Attributes:
        raiz: Referencia al nodo raíz del árbol, o None si está vacío.
    """

    def __init__(self):
        """Inicializa un árbol binario de búsqueda vacío."""
        self._raiz = None


    def es_vacio(self):
        """Comprueba si el árbol está vacío.

        Returns:
            bool: True si el árbol no tiene raíz, False en caso contrario.
        """
        return self.raiz is None

    def EsHoja(self):
        """Comprueba si la raíz del árbol es una hoja.

        Returns:
            bool: True si la raíz no tiene hijos, False en caso contrario.
        """
        if self.raiz is not None:
            return self.raiz.izquierdo is None and self.raiz.derecho is None
        return False

    def insertar(self, valor):
        """Inserta un valor en el árbol binario de búsqueda.

        Args:
            valor: Valor que se insertará en el árbol.
        """
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo):
        """Inserta un valor de forma recursiva manteniendo el orden del ABB.

        Args:
            valor: Valor que se insertará.
            nodo: Nodo actual durante el recorrido del árbol.
        """
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo.izquierdo)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo.derecho)

    def buscar(self, valor):
        """Busca un valor en el árbol binario de búsqueda.

        Args:
            valor: Valor que se buscará en el árbol.

        Returns:
            bool: True si el valor existe en el árbol, False en caso contrario.
        """
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo):
        """Busca un valor de forma recursiva.
        """
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(valor, nodo.izquierdo)
        else:
            return self._buscar_recursivo(valor, nodo.derecho)

    def eliminar(self, valor):
        """Elimina un valor del árbol binario de búsqueda.

        Cubre los tres casos clásicos: nodo hoja, nodo con un solo hijo y
        nodo con dos hijos (se reemplaza por el menor de su subárbol derecho).

        Args:
            valor: Valor que se eliminará del árbol.

        Returns:
            bool: True si el valor existía y fue eliminado, False si no se encontró.
        """
        self.raiz, eliminado = self._eliminar_recursivo(self.raiz, valor)
        return eliminado

    def _eliminar_recursivo(self, nodo, valor):
        """Elimina un valor de forma recursiva manteniendo el orden del ABB.

        Args:
            nodo: Nodo actual durante la búsqueda del valor.
            valor: Valor que se eliminará.

        Returns:
            tuple: (nueva_raíz_del_subárbol, se_eliminó)
        """
        if nodo is None:
            return None, False

        if valor < nodo.valor:
            nodo.izquierdo, eliminado = self._eliminar_recursivo(nodo.izquierdo, valor)
            return nodo, eliminado

        if valor > nodo.valor:
            nodo.derecho, eliminado = self._eliminar_recursivo(nodo.derecho, valor)
            return nodo, eliminado

        # Caso 1 y 2: nodo hoja o con un solo hijo.
        if nodo.izquierdo is None:
            return nodo.derecho, True
        if nodo.derecho is None:
            return nodo.izquierdo, True

        # Caso 3: dos hijos -> sustituir por el menor del subárbol derecho.
        sucesor = self._minimo(nodo.derecho)
        nodo.valor = sucesor.valor
        nodo.derecho, _ = self._eliminar_recursivo(nodo.derecho, sucesor.valor)
        return nodo, True

    def _minimo(self, nodo):
        """Devuelve el nodo con el menor valor del subárbol indicado."""
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def altura(self):
        """Calcula la altura del árbol (número de niveles).

        Returns:
            int: 0 si el árbol está vacío, 1 si solo tiene la raíz, etc.
        """
        return self._altura_recursivo(self.raiz)

    def _altura_recursivo(self, nodo):
        """Calcula la altura de un subárbol de forma recursiva."""
        if nodo is None:
            return 0
        return 1 + max(
            self._altura_recursivo(nodo.izquierdo),
            self._altura_recursivo(nodo.derecho),
        )

    def construir_desde_posfija(self, posfija):
        """Construye un árbol binario a partir de una expresión en notación posfija.

        Args:
            posfija (list | str): Expresión en notación posfija. Si es una cadena
                se asume que no tiene espacios y cada carácter es un token.
                Los operandos pueden ser números o variables y los operadores
                son: +, -, *, /.

        Raises:
            ValueError: Si la expresión está vacía o mal formada.
        """
        if not posfija:
            self.raiz = None
            return

        pila_nodos = []

        for token in posfija:
            nodo = Nodo(token)

            # Si es un operando, se apila.
            if token not in "+-*/":
                pila_nodos.append(nodo)
            else:
                # Si es un operador, toma los dos últimos nodos como sus hijos.
                if len(pila_nodos) < 2:
                    raise ValueError(
                        f"Expresión inválida: operador '{token}' sin suficientes operandos."
                    )
                nodo.derecho = pila_nodos.pop()
                nodo.izquierdo = pila_nodos.pop()
                pila_nodos.append(nodo)

        if len(pila_nodos) != 1:
            raise ValueError("Expresión inválida: sobran operandos sin operador.")

        # El último nodo en la pila es la raíz principal.
        self.raiz = pila_nodos.pop()




# RECORRIDOS DEL ÁRBOL




    def InOrden(self):
        """Recorre el árbol en orden simétrico (inorden).

        Returns:
            str: Cadena con los valores del árbol separados por espacios.
        """
        elementos = []
        self._inorden_recursivo(self.raiz, elementos)
        return " ".join(elementos)

    def _inorden_recursivo(self, nodo, elementos):
        """Recorre el subárbol en inorden y almacena sus valores.

        Args:
            nodo: Nodo raíz del subárbol a recorrer.
            elementos: Lista donde se almacenan los valores.
        """
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, elementos)
            elementos.append(str(nodo.valor))
            self._inorden_recursivo(nodo.derecho, elementos)



    def PostOrden(self):
        """Recorre el árbol en postorden.

        Returns:
            str: Cadena con los valores del árbol separados por espacios.
        """
        elementos = []
        self._post_orden_recursivo(self.raiz, elementos)
        return " ".join(elementos)

    def _post_orden_recursivo(self, nodo_actual, elementos):
        """Recorre el subárbol en postorden y almacena sus valores.

        Args:
            nodo_actual: Nodo raíz del subárbol a recorrer.
            elementos: Lista donde se almacenan los valores.
        """
        if nodo_actual is not None:
            # 1. Recorrer subárbol izquierdo
            self._post_orden_recursivo(nodo_actual.izquierdo, elementos)
            # 2. Recorrer subárbol derecho
            self._post_orden_recursivo(nodo_actual.derecho, elementos)
            # 3. Visitar raíz
            elementos.append(str(nodo_actual.valor))



    def PreOrden(self):
        """Recorre el árbol en preorden.

        Returns:
            str: Cadena con los valores del árbol separados por espacios.
        """
        elementos = []
        self._preorden_recursivo(self.raiz, elementos)
        return " ".join(elementos)

    def _preorden_recursivo(self, nodo, elementos):
        """Recorre el subárbol en preorden y almacena sus valores.

        Args:
            nodo: Nodo raíz del subárbol a recorrer.
            elementos: Lista donde se almacenan los valores.
        """
        if nodo is not None:
            elementos.append(str(nodo.valor))
            self._preorden_recursivo(nodo.izquierdo, elementos)
            self._preorden_recursivo(nodo.derecho, elementos)











    @property
    def raiz(self):
        """GETTER:
        Obtiene la referencia al nodo raíz del árbol."""
        return self._raiz

    @raiz.setter
    def raiz(self, raiz):
        """SETTER:
        Establece la referencia al nodo raíz del árbol."""
        self._raiz = raiz
