# Proyecto #1 — Árbol de expresiones

Aplicación web que toma una expresión matemática en **notación infija**,
la convierte a **notación posfija**, construye su **árbol binario de
expresión**, muestra los tres recorridos, evalúa el resultado y dibuja el
árbol con Graphviz.

Desarrollada con **Flask** siguiendo el patrón **MVC** (modelo, controlador y
vistas).

---

## ✨ Funcionalidades

- Validación de la expresión con mensajes de error específicos (caracteres no
  permitidos, operadores mal ubicados, paréntesis desbalanceados, números
  inválidos, etc.).
- Conversión **infija → posfija** con el algoritmo *Shunting Yard*, respetando
  prioridad de operadores y paréntesis.
- Construcción del **árbol binario de expresión** a partir de la notación
  posfija.
- Recorridos **preorden**, **inorden** y **postorden**.
- **Evaluación** del árbol (soporta números enteros y decimales).
- **Gráfico SVG** del árbol generado con Graphviz.
- Versión de **consola** (`demo_consola.py`) con la misma lógica.

## 🧪 Ejemplo

Para la expresión `(3+5)*2`:

| Resultado | Valor |
|---|---|
| Notación posfija | `3 5 + 2 *` |
| Preorden | `* + 3 5 2` |
| Inorden | `3 + 5 * 2` |
| Postorden | `3 5 + 2 *` |
| Resultado | `16.0` |

```text
        *
      /   \
     +     2
   /   \
  3     5
```

---

## 📁 Estructura (MVC)

```text
Proyecto_1_Arbol_Expresiones/
├── app.py                        # Punto de entrada y rutas de Flask
├── demo_consola.py               # Versión de consola del proyecto
├── controller/
│   └── expresiones_controller.py # Recibe la petición y coordina el modelo
├── model/
│   ├── nodo.py                   # Nodo del árbol
│   ├── arbolbinario.py           # ADT Árbol Binario base
│   └── ejercicio_expresiones.py  # Conversión, árbol de expresión y evaluación
├── templates/
│   └── index.html                # Vista (formulario y resultados)
├── static/
│   └── css/styles.css            # Estilos
├── requirements.txt
└── README.md
```

| Capa | Responsabilidad |
|---|---|
| **Modelo** | Estructuras de datos, conversión de notaciones y evaluación |
| **Controlador** | Valida la entrada y decide qué datos enviar a la vista |
| **Vista** | Formulario y presentación de resultados (HTML + CSS) |

---

## 🚀 Cómo ejecutarlo

```bash
cd Proyectos/Proyecto_1_Arbol_Expresiones

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abrir **http://127.0.0.1:5000** en el navegador.

> El gráfico del árbol usa la biblioteca de Python `graphviz` y el programa
> `dot`. En Debian/Ubuntu se instala con `sudo apt install graphviz`.

### Versión de consola

```bash
python demo_consola.py
```

```text
Ingrese una expresión matemática (números, + - * / y paréntesis): (3+5)*2
1. Notación posfija:              ['3', '5', '+', '2', '*']
2. Recorrido PreOrden del árbol:  * + 3 5 2
3. Recorrido InOrden del árbol:   3 + 5 * 2
4. Recorrido PostOrden del árbol: 3 5 + 2 *
5. Resultado de la expresión:     16.0
```

---

## 🧠 Cómo funciona

1. **Validación:** se separa la expresión en *tokens* y se comprueba que
   operandos, operadores y paréntesis estén en el orden correcto.
2. **Infija → posfija:** se recorre la lista de tokens con una pila de
   operadores. Un operador se desapila cuando tiene prioridad mayor o igual
   que el operador actual; los paréntesis delimitan bloques.
3. **Construcción del árbol:** se recorre la notación posfija; cada operando se
   apila como nodo y cada operador desapila dos nodos (derecho e izquierdo) y
   se apila a sí mismo como raíz de ese subárbol.
4. **Evaluación:** recorrido postorden recursivo; las hojas se convierten a
   número y los nodos internos aplican su operador.
5. **Gráfico:** se recorre el árbol y se generan nodos y aristas de Graphviz,
   que se renderizan como SVG dentro de la página.

---

## 📌 Alcance y limitaciones

- Operadores soportados: `+`, `-`, `*`, `/`.
- Números enteros y decimales positivos (`3`, `4.5`).
- El signo menos **unario** no está soportado (`-3+5` se rechaza); para restar
  se debe usar una operación binaria.
- El recorrido inorden se muestra sin paréntesis, por lo que no siempre
  reconstruye la expresión original de forma inequívoca.
- La división por cero se informa como error sin romper la aplicación.

---

## 🛠️ Tecnologías

- Python 3
- Flask
- Graphviz
