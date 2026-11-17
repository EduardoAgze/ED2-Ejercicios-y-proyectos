# Proyectos

Proyectos integradores de la materia. Cada uno es una aplicación independiente
con su propio `README.md`, `requirements.txt` y entorno virtual.

| # | Proyecto | Carpeta | Tecnologías |
|---|---|---|---|
| 1 | **Árbol de expresiones** | [`Proyecto_1_Arbol_Expresiones/`](Proyecto_1_Arbol_Expresiones/) | Python · Flask · Graphviz · MVC |
| 2 | **3 en raya con Machine Learning** | [`Proyecto_2_Tres_En_Raya_ML/`](Proyecto_2_Tres_En_Raya_ML/) | Python · Flask · scikit-learn · pandas |

## Proyecto #1 — Árbol de expresiones

Convierte una expresión matemática escrita en notación infija a notación
posfija, construye el árbol binario de la expresión, muestra sus recorridos y
evalúa el resultado. Incluye una interfaz web y una versión de consola.

## Proyecto #2 — 3 en raya ML

Tres en raya jugable contra una IA **Minimax** (con dificultad ajustable) o
contra una IA entrenada con **Machine Learning** (árbol de decisión). La
interfaz muestra los nodos explorados y el tiempo de decisión de la IA.

## Ejecución

Cada proyecto se instala y ejecuta por separado:

```bash
cd Proyecto_1_Arbol_Expresiones
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python app.py
```

```bash
cd Proyecto_2_Tres_En_Raya_ML
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python app.py
```
