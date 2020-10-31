from app.configuracao.db import db
from datetime import datetime

from .utils import gerar_prazo

class Emprestimo(db.Model):
    __tablename__ = "emprestimos"
    id = db.Column(db.Integer, primary_key=True)
    data_emprestimo = db.Column(db.DateTime, default=datetime.now)
    data_entrega = db.Column(db.DateTime, default=gerar_prazo)
    entregado_em = db.Column(db.DateTime, nullable=True)
    
    usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    livros = db.relationship("Livro", backref='emprestimos', lazy=True)

