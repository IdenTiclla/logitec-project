from utils.db import db


class Contrato(db.Model):
    __tablename__ = 'contratos'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50))

    # relacion muchos empleados tienen 1 contrato
    empleados = db.relationship('Empleado', backref='contrato')


    def __str__(self):
        return f"<{self.descripcion}>"

    def guardar_contrato(self):
        db.session.add(self)
        db.session.commit()