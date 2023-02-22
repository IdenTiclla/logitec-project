from flask import Blueprint, render_template, request, redirect, flash, session, send_file
from models.venta import Venta
from models.producto import Producto
from models.empleado import Empleado
from datetime import datetime


from fpdf import FPDF


from utils.db import db

ventas = Blueprint("ventas", __name__)

@ventas.route("/ventas")
def index():
    productos = []
    all_products = Producto.query.all()
    for product in all_products:
        if product.stock > 0:
            productos.append(product)

    cart = session.get('cart')
    if not cart:
        cart = []
    
    print(cart)


    precio_total = 0
    for item in cart:
        precio_total += item['precio'] * item['cantidad']

    empleados = Empleado.query.all()
    return render_template("ventas.html", productos=productos, cart=cart, precio_total=precio_total, empleados=empleados)

@ventas.route("/ventas/addToCart/<id>")
def add_to_cart(id):
    # product = Producto.query.get(id)
    # cart = session.get('cart')
    # if cart == None:
    #     cart = []
    # cart.append(product)
    # session['cart'] = cart


    product = Producto.query.get(id)
    cart = session.get('cart')
    if cart == None:
        cart = []
        cart.append({'id':product.id, 'nombre': product.nombre, 'precio':product.precio, 'cantidad': 1})
    
    else:
        flag = False
        for item in cart:
            if item['id'] == product.id:
                flag = True
                item['cantidad'] += 1
        if not flag:
            cart.append({'id':product.id, 'nombre': product.nombre, 'precio':product.precio, 'cantidad': 1})

    session['cart'] = cart

    return redirect('/ventas')
@ventas.route("/ventas/add", methods=['POST'])
def add_ventas():
    cart = session.get('cart')
    empleado_id = request.form['empleadoId']
    empleado = Empleado.query.get(empleado_id)
    print("testing...")
    print(cart)
    print(empleado)
    print(empleado.products)
    fecha_creacion = datetime.now()

    data = (
        ("", "LOGITEC SRL", ""),
        ("", f"Vendedor: {empleado.nombre}", ""),
        ("Producto", "cantidad", "Total"),
    )
    precio_total = 0
    for item in cart:
        # print(f"item: {item}")
        item_id = item['id']
        precio = item['precio']
        cantidad = item['cantidad']

        producto = Producto.query.get(item_id)
        producto.stock = producto.stock - cantidad
        # print(producto)
        # empleado.products.append(producto)
        # print(f"item: {item['id']}")
        precio_total += cantidad * producto.precio
        venta = Venta(id_producto=item_id, id_empleado=empleado_id, cantidad=cantidad, total=cantidad*precio, fecha_creacion=fecha_creacion)
        data = (*data, (f"{producto.nombre}", f"{cantidad}", f"{cantidad * producto.precio}"))
        db.session.add(venta)
        db.session.commit()

    data = (*data, ("", "", f"{precio_total} BS"))

    # print(empleado.products)
    # #ojo
    # db.session.add(empleado) 
    # db.session.commit()

    session.clear()
    flash('venta realizada')
    
    # generando pdf

    

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=10)
    
    line_height = pdf.font_size * 2.5
    col_width = pdf.epw / 4  # distribute content evenly
    for row in data:
        for datum in row:
            pdf.multi_cell(col_width, line_height, datum, border=1,
                    new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
        pdf.ln(line_height)
    pdf.output('factura.pdf')
    return redirect('/ventas')

@ventas.route("/ventas/dowload")
def downloadFile ():
    path = "./factura.pdf"
    return send_file(path, as_attachment=True)
    #For windows you need to use drive name [ex: F:/Example.pdf]



@ventas.route("/ventas/limpiar")
def limpiar_carrito():
    session.clear()
    return redirect("/ventas")