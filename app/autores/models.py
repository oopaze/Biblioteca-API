from app.configuracao.db import db

class Autor(db.Model):
    __tablename__ = "autores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return "<Autor %r>" %self.name