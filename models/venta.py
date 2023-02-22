from datetime import datetime
from utils.db import db

from .empleado import Empleado
from .producto import Producto

class Venta(db.Model):
    __tablename__ = 'ventas'

    id = db.Column(db.Integer, primary_key=True)
    # relacion many to many
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id'))
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'))
    # propiedades
    cantidad = db.Column(db.Integer)
    total = db.Column(db.Float)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now())

    # user = db.relationship(Empleado, backref="orders", cascade="all, delete-orphan")
    # product = db.relationship(Producto, backref="orders", cascade="all, delete-orphan")


    def __str__(self):
        return f"<{self.id} - {self.id_producto} - {self.id_empleado}>"