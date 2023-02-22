from flask import Flask, render_template
from routes.productos import productos
from routes.contratos import contratos
from routes.sucursales import sucursales
from routes.empleados import empleados
from routes.ventas import ventas

from flask_session import Session
from utils.db import db

app = Flask(__name__)
# sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# settings
app.secret_key = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/logitecdb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

app.register_blueprint(productos)
app.register_blueprint(empleados)
app.register_blueprint(ventas)
app.register_blueprint(sucursales)
app.register_blueprint(contratos)