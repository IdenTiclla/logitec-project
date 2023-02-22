from datetime import datetime
from utils.db import db


class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10), unique=True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))
    stock = db.Column(db.Integer)
    precio = db.Column(db.Float)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now())

    # relacion con empleados para muchos y muchos
    empleados = db.relationship("Empleado", secondary="ventas")
    # empleados = db.relationship("Empleado")


    def __str__(self):
        return f"<{self.codigo} - {self.nombre}>"

    
    def guardar_producto(self):
        db.session.add(self)
        db.session.commit()

    def actualizar_producto(self):
        db.session.commit()

    def eliminar_producto(self):
        db.session.delete(self)
        db.session.commit()

    


