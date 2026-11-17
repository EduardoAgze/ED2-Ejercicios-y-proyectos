# ADT Árbol Binario — Ejercicios y Proyectos

Repositorio de la materia **Estructura de Datos II**. Reúne los ejercicios de
clase sobre árboles binarios y los proyectos desarrollados durante el curso,
organizados en dos secciones: `Ejercicios/` y `Proyectos/`.

**Alumno:** Luis Eduardo Vargas Pantoja
**# de Registro:** 225044765
**Materia:** Estructura de Datos II

---

## 📂 Contenido

| Sección | Tema | Documentación |
|---|---|---|
| **Ejercicios** | Prácticas de árboles binarios | [`Ejercicios/README.md`](Ejercicios/README.md) |
| ↳ ADT Árbol | Crear, verificar vacío, consultar raíz, eliminar y recorridos | [`Ejercicios/adt_arbol/README.md`](Ejercicios/adt_arbol/README.md) |
| ↳ 3 en raya | El tablero representado con tres árboles binarios | [`Ejercicios/tres_en_raya/README.md`](Ejercicios/tres_en_raya/README.md) |
| ↳ Reordenamiento | Convertir un ABB desbalanceado en uno balanceado | [`Ejercicios/reordenamiento_arbol/README.md`](Ejercicios/reordenamiento_arbol/README.md) |
| **Proyectos** | Aplicaciones completas | [`Proyectos/README.md`](Proyectos/README.md) |
| ↳ Proyecto #1 | Árbol de expresiones con interfaz web (MVC + Flask) | [`Proyectos/Proyecto_1_Arbol_Expresiones/README.md`](Proyectos/Proyecto_1_Arbol_Expresiones/README.md) |
| ↳ Proyecto #2 | 3 en raya con IA (Minimax + Machine Learning) | [`Proyectos/Proyecto_2_Tres_En_Raya_ML/README.md`](Proyectos/Proyecto_2_Tres_En_Raya_ML/README.md) |

---

## 🗂️ Estructura del repositorio

```text
ADT-ArbolBinario/
├── Ejercicios/
│   ├── README.md
│   ├── adt_arbol/                  # ADT ArbolBinario + demo de operaciones
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── nodo.py
│   │   ├── arbolbinario.py
│   │   └── main.py
│   ├── tres_en_raya/
│   │   ├── README.md
│   │   └── ejercicio_3en_raya.py
│   └── reordenamiento_arbol/
│       ├── README.md
│       └── reordenamiento.py
├── Proyectos/
│   ├── README.md
│   ├── Proyecto_1_Arbol_Expresiones/
│   │   ├── README.md
│   │   ├── app.py
│   │   ├── demo_consola.py
│   │   ├── controller/
│   │   ├── model/
│   │   ├── templates/
│   │   ├── static/
│   │   └── requirements.txt
│   └── Proyecto_2_Tres_En_Raya_ML/
│       ├── README.md
│       ├── app.py
│       ├── controller/
│       ├── model/
│       ├── data/
│       ├── templates/
│       ├── static/
│       └── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Cómo ejecutar

Los ejercicios solo usan la biblioteca estándar de Python, por lo que se
ejecutan directamente:

```bash
python3 Ejercicios/adt_arbol/main.py
python3 Ejercicios/tres_en_raya/ejercicio_3en_raya.py
python3 Ejercicios/reordenamiento_arbol/reordenamiento.py
```

Los proyectos son aplicaciones Flask y cada uno tiene su propio
`requirements.txt` y su propio entorno virtual:

```bash
cd Proyectos/Proyecto_1_Arbol_Expresiones
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python app.py          # http://127.0.0.1:5000
```

```bash
cd Proyectos/Proyecto_2_Tres_En_Raya_ML
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python app.py          # http://127.0.0.1:5000
```

> En Windows el intérprete del entorno virtual está en `.venv\Scripts\python`.

---

## 🧠 Temas cubiertos

- Tipos de datos abstractos (TDA/ADT) y encapsulamiento con propiedades.
- Árboles binarios de búsqueda: inserción, búsqueda, eliminación y altura.
- Recorridos: preorden, inorden y postorden.
- Construcción de árboles a partir de notación posfija.
- Evaluación de expresiones aritméticas almacenadas en un árbol.
- Balanceo de árboles mediante recorrido inorden y división recursiva.
- Búsqueda adversarial con Minimax y poda por profundidad.
- Generación de datasets y entrenamiento de un árbol de decisión.
- Arquitectura MVC y desarrollo web con Flask.
