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
    disponivel = db.Column(db.Boolean, default=True)

    autores = db.relationship(Autor, 
                               secondary=autor_livro,
                               backref=db.backref('livros', lazy='dynamic'))

    emprestimo_id = db.Column(db.Integer, db.ForeignKey('emprestimos.id'))

    adicionado_em = db.Column(db.DateTime, default=datetime.now)
    atualizado_em = db.Column(db.DateTime, onupdate=datetime.now)


    def __init__(self, titulo, vol, disponivel: bool = True, *args, **kwargs):
        self.titulo = titulo
        self.vol = vol
        self.disponivel = disponivel

    def adicionar_autor(self, _autores):
        autores = []
        for autor in _autores:
            try:
                autor_novo = Autor.query.get(autor)
                autores.append(autor_novo)
            except Exception:
                pass
        
        return autores
        

    def __repr__(self):
        return self.titulo
