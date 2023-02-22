from datetime import datetime
from utils.db import db


class Empleado(db.Model):
    __tablename__ = 'empleados'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    sueldo = db.Column(db.Float)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now())

    products = db.relationship('Producto', secondary='ventas')
    # products = db.relationship('Producto')

    # relacion muchos empleados tienen 1 sucursal
    sucursal_id = db.Column(db.Integer, db.ForeignKey("sucursales.id"))

    # relacion muchos empleados tienen 1 contrato
    contrato_id = db.Column(db.Integer, db.ForeignKey("contratos.id"))




    def guardar_empleado(self):
        db.session.add(self)
        db.session.commit()


    def actualizar_empleado(self):
        db.session.commit()

    def eliminar_empleado(self):
        db.session.delete(self)
        db.session.commit()


    def __str__(self):
        return f"<{self.nombre}>"