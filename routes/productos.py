from flask import Blueprint, render_template, request, redirect, flash
from models.producto import Producto

productos = Blueprint("productos", __name__)


@productos.route('/productos', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        products = Producto.query.all()
        print(products)
        return render_template("productos.html", products=products)
    elif request.method == "POST":
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        stock = request.form['stock']
        precio = request.form['precio']


        product = Producto(codigo=codigo, nombre=nombre, descripcion=descripcion, stock=stock, precio=precio)
        print(product)
        product.guardar_producto()
        return redirect("/productos")

@productos.route("/productos/update/<id>", methods=['GET', 'POST'])
def update_product(id):
    product = Producto.query.get(id)
    if request.method == 'GET':
        return render_template("update_product.html", product=product)

    elif request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        stock = request.form['stock']
        precio = request.form['precio']

        print(nombre,descripcion,stock)
        product.nombre = nombre
        product.descripcion = descripcion
        product.stock = stock
        product.precio = precio
        
        product.actualizar_producto()

        flash("producto actualizado exitosamente!")
        return redirect('/productos')

@productos.route("/productos/delete/<id>")
def delete_product(id):
    product = Producto.query.get(id)
    product.eliminar_producto()
    flash("Producto eliminado exitosamente!")
    return redirect("/productos")