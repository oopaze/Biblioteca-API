from app.configuracao.db import db
from datetime import datetime
from app.autores.models import Autor

autor_livro = db.Table(
    'autor_livro',
    db.Column('autor_id', db.Integer, db.ForeignKey('autores.id')),
    db.Column('livro_id', db.Integer, db.ForeignKey('livros.id')),
)

class Livro(db.Model):
    __tablename__ = 'livros'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    vol = db.Column(db.Integer, default=1)
    disponivel = db.Column(db.Boolean)

    autores = db.relationship(Autor, 
                               secondary=autor_livro,
                               backref=db.backref('livros', lazy='dynamic'))
    usuario_aluguel = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    criado_em = db.Column(db.DateTime, default=datetime.now)
    atualizado_em = db.Column(db.DateTime, onupdate=datetime.now)

    def __init__(self, titulo, vol, disponivel: bool = True, autores: list = []):
        self.titulo = titulo
        self.vol = vol
        self.autores = autores
        self.disponivel = disponivel
    
    def alugar(self, usuario, db):
        self.disponivel = False
        self.usuario_aluguel.append(usuario)
        db.session.commit()

    def __repr__(self):
        return self.titulo
