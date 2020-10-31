from app.configuracao.ma import ma
from .models import Emprestimo
from app.livros.models import Livro

class EmprestimoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Emprestimo

class LivroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Livro
        fields = ("id", "titulo", "vol")