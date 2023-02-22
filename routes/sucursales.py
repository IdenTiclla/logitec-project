from flask import Blueprint, render_template, request, redirect, flash
from models.sucursal import Sucursal
sucursales = Blueprint("sucursales", __name__)


@sucursales.route('/sucursales', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        sucursales = Sucursal.query.all()
        return render_template("sucursales.html", sucursales=sucursales)

    elif request.method == "POST":
        nombre = request.form['nombre']
        direccion = request.form['direccion']

        sucursal = Sucursal(nombre=nombre, direccion=direccion)
        sucursal.guardar_sucursal()
        flash("Sucursal registrada correctamente!")
        return redirect("/sucursales")
