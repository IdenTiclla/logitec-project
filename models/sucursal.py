from datetime import datetime
from utils.db import db


class Sucursal(db.Model):
    __tablename__ = 'sucursales'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(100))
    fecha_creacion = db.Column(db.DateTime, default=datetime.now())
    # relacion 1 sucursal tiene muchos empleados
    empleados = db.relationship('Empleado', backref='sucursal')

    def guardar_sucursal(self):
        db.session.add(self)
        db.session.commit()



    def __str__(self):
        return f"<{self.nombre}>"