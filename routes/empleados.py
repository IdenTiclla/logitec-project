from flask import Blueprint, render_template, request, redirect, flash
from models.empleado import Empleado
from models.sucursal import Sucursal
from models.contrato import Contrato
empleados = Blueprint("empleados", __name__)


@empleados.route('/empleados', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        empleados = Empleado.query.all()
        sucursales = Sucursal.query.all()
        contratos = Contrato.query.all()
        return render_template("empleados.html", empleados=empleados, sucursales=sucursales, contratos=contratos)

    elif request.method == "POST":
        nombre = request.form['nombre']
        sueldo = request.form['sueldo']
        #sucursalId
        sucursal_id = request.form['sucursalId']
        contrato_id = request.form['contratoId']

        empleado = Empleado(nombre=nombre, sueldo=sueldo, sucursal_id=sucursal_id, contrato_id=contrato_id)
        empleado.guardar_empleado()
        flash("Empleado registrado correctamente!")
        return redirect("/empleados")


@empleados.route("/empleados/update/<id>", methods=['GET', 'POST'])
def update_empleado(id):
    empleado = Empleado.query.get(id)
    if request.method == 'GET':
        return render_template("update_empleado.html", empleado=empleado)

    elif request.method == 'POST':
        nombre = request.form['nombre']
        sueldo = request.form['sueldo']

        print(nombre, sueldo)
        empleado.nombre = nombre
        empleado.sueldo = sueldo

        
        empleado.actualizar_empleado()

        flash("Empleado actualizado correctamente!")
        return redirect('/empleados')


@empleados.route("/empleados/delete/<id>")
def delete_empleado(id):
    empleado = Empleado.query.get(id)
    empleado.eliminar_empleado()
    flash("Empleado eliminado exitosamente!")
    return redirect("/empleados")