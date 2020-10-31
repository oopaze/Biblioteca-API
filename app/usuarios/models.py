from werkzeug.security import generate_password_hash, check_password_hash
from app.configuracao.db import db
from app.biblioteca.models import Emprestimo

class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, default=False)

    emprestimos = db.relationship(Emprestimo, backref='usuarios', lazy=True)

    def __init__(self, name, username, password, admin: bool = None):
        self.name = name
        self.username = username
        self.password = self.generate_hash_password(password)

        if admin:
            self.admin = admin

    def __repr__(self):
        """Função que retornar a saida de um print do nosso objeto"""
        return f'<Employee {self.username}>'

    def generate_hash_password(self, password):
        """Função responsável por encriptar o password do usuario"""
        return generate_password_hash(password)

    def verify_password(self, password):
        """Função responsável por comparar os passwords encriptados do usuario"""
        return check_password_hash(self.password, password)