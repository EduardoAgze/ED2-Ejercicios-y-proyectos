# Proyecto 2 — Tres en raya con Machine Learning

Juego de tres en raya desarrollado con Flask. Permite jugar entre dos personas
o contra una inteligencia artificial que puede funcionar de dos formas:
**Minimax** o **Machine Learning**. La interfaz muestra cuántos nodos exploró
la IA y cuánto tardó en decidir.

## Modos de juego

| Modo | Descripción |
|---|---|
| Humano vs Humano | Dos personas juegan en el mismo tablero |
| Humano vs Minimax | La IA busca en el árbol de jugadas con dificultad ajustable |
| Humano vs ML | La IA usa un árbol de decisión entrenado con partidas de Minimax |

El humano juega con `X` y la IA con `O`.

## Cómo funciona la IA

### Minimax

Imagina la partida como un árbol de jugadas. Asigna +10 si gana la IA, -10 si
gana el humano y 0 si hay empate. Explora, retrocede y prueba otra jugada
(*backtracking*). La dificultad limita la profundidad de búsqueda: fácil 1
jugada, medio 2 y difícil hasta el final.

### Machine Learning

1. Se generan partidas de Minimax contra un jugador aleatorio.
2. Cada tablero y su jugada óptima se guardan en `data/dataset.csv`.
3. Un árbol de decisión se entrena con esos datos.
4. Al jugar, el modelo predice la casilla; si la predicción no es válida, se usa
   Minimax como respaldo.

El dataset incluido tiene 1072 estados generados a partir de 300 partidas.

## Métricas

- **Nodos:** estados que revisó la IA.
- **Tiempo IA:** milisegundos que tardó en elegir.
- **ML directo / fallback:** indica si jugó el modelo o si usó Minimax.

## Estructura

```text
Proyecto_2_Tres_En_Raya_ML/
├── app.py                        # Rutas de Flask
├── controller/
│   └── game_controller.py        # Coordina modelo, sesión y vista
├── model/
│   ├── game_model.py             # Reglas del juego
│   ├── evaluation.py             # Evaluación de estados
│   ├── minimax_agent.py          # IA Minimax
│   ├── ai_service.py             # Elige entre Minimax y ML
│   ├── session.py                # Estado de la partida
│   ├── ml_agent.py               # Generación del dataset
│   ├── train_model.py            # Entrenamiento del modelo
│   └── tictactoe_dt.joblib       # Modelo entrenado
├── data/dataset.csv              # Estados y jugadas óptimas
├── templates/index.html          # Interfaz
├── static/styles.css             # Estilos
├── requirements.txt
└── README.md
```

## Tecnologías

Python, Flask, scikit-learn, pandas y joblib.

## Notas

- El modo ML aprende de un dataset pequeño, por lo que no es perfecto.
- El respaldo con Minimax evita que la IA haga jugadas inválidas.
