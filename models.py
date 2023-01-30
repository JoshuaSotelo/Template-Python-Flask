import datetime
from flask_login import UserMixin
from extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    apellido1 = db.Column(db.String(10))
    apellido2 = db.Column(db.String(10))
    tipo_usuario = db.Column(db.Integer)


class Cliente(db.Model, UserMixin):
    id = db.Column(db.String(20), primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    apellido1 = db.Column(db.String(10))
    apellido2 = db.Column(db.String(10))
    tipo_usuario = db.Column(db.Integer)
    expediente = db.relationship('Expediente')
    notes = db.relationship('Note')


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000))
    date = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)
    expediente = db.Column(db.String, db.ForeignKey('expediente.id'))
    cliente = db.Column(db.String(20), db.ForeignKey('cliente.id'))


class Expediente(db.Model):
    id = db.Column(db.String(90), primary_key=True)
    estado = db.Column(db.String(50))
    cliente = db.Column(db.String(20), db.ForeignKey('cliente.id'))
    parte_contraria = db.Column(db.String(50))
    proceso = db.Column(db.String(50))
    materia = db.Column(db.String(50))
    resumen = db.Column(db.String(1000))
    monto = db.Column(db.DECIMAL(6, 2))
    fecha_inicio = db.Column(db.DateTime(timezone=True))
    fecha_fin = db.Column(db.DateTime(timezone=True))

