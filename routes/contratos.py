from flask import Blueprint, render_template, request, redirect, flash
from models.contrato import Contrato

contratos = Blueprint("contratos", __name__)


@contratos.route('/contratos', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        contratos = Contrato.query.all()
        return render_template("contratos.html", contratos=contratos)

    elif request.method == "POST":
        descripcion = request.form['descripcion']

        contrato = Contrato(descripcion=descripcion)
        contrato.guardar_contrato()
        flash("Contrato registrada correctamente!")
        return redirect("/contratos")
