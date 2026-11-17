from flask import render_template, request, redirect, url_for, flash
from model.ejercicio_expresiones import infija_a_posfija
from model.ejercicio_expresiones import ArbolBinario_Expresiones
from model.ejercicio_expresiones import validar_expresion


def index():
    """Mostrar la página principal con el formulario de conversión."""
    return render_template("index.html")


def convertir():
    """Convertir una expresión infija y mostrar los resultados."""
    expresion = request.form.get("expresion")

    if not expresion:
        flash("Ingrese una expresión válida.")
        return redirect(url_for("index"))

    es_valida, mensaje = validar_expresion(expresion)
    if not es_valida:
        flash(mensaje)
        return redirect(url_for("index"))

    try:
        posfija = infija_a_posfija(expresion)
        arbol = ArbolBinario_Expresiones()
        arbol.construir_desde_posfija(posfija)
        preorden = arbol.PreOrden()
        inorden = arbol.InOrden()
        postorden = arbol.PostOrden()
        grafico_svg = arbol.grafo().pipe(format="svg").decode("utf-8")
    except (ValueError, IndexError) as e:
        flash(f"Error al procesar la expresión: {e}")
        return redirect(url_for("index"))

    flash("Expresión convertida")

    return render_template("index.html",
                           expresion=expresion,
                           posfija=posfija,
                           preorden=preorden,
                           inorden=inorden,
                           postorden=postorden,
                           grafico_svg=grafico_svg,
                           resultado=arbol.evaluar())