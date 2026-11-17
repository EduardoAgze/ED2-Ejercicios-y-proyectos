# Proyecto 1 — Árbol de expresiones

Aplicación web que convierte una expresión matemática de notación infija a
posfija, construye su árbol binario, muestra los recorridos, calcula el
resultado y dibuja el árbol. Está desarrollada con Flask y arquitectura MVC.

## Qué hace

- Valida la expresión y muestra el error cuando está mal escrita.
- Convierte de infija a posfija respetando prioridades y paréntesis.
- Construye el árbol binario de la expresión.
- Muestra los recorridos preorden, inorden y postorden.
- Evalúa la expresión.
- Genera una imagen SVG del árbol con Graphviz.
- Incluye una versión de consola con la misma lógica.

## Ejemplo

Para `(3+5)*2`:

| Resultado | Valor |
|---|---|
| Posfija | `3 5 + 2 *` |
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

## Estructura

```text
Proyecto_1_Arbol_Expresiones/
├── app.py                        # Rutas de Flask
├── demo_consola.py               # Versión de consola
├── controller/
│   └── expresiones_controller.py # Valida y coordina el modelo
├── model/
│   ├── nodo.py                   # Nodo del árbol
│   ├── arbolbinario.py           # ADT Árbol Binario
│   └── ejercicio_expresiones.py  # Conversión, árbol y evaluación
├── templates/index.html          # Vista
├── static/css/styles.css         # Estilos
├── requirements.txt
└── README.md
```

## Cómo funciona

1. **Validación:** separa la expresión en tokens y comprueba que operandos,
   operadores y paréntesis estén en orden.
2. **Infija a posfija:** usa una pila de operadores y la prioridad de cada uno.
3. **Árbol:** recorre la posfija; cada operando se apila y cada operador toma
   los dos últimos nodos como hijos.
4. **Evaluación:** recorre el árbol en postorden y aplica cada operador.

## Alcance

- Operadores: `+`, `-`, `*`, `/`.
- Números enteros y decimales positivos.
- No admite el signo menos unario.
- El inorden se muestra sin paréntesis.
