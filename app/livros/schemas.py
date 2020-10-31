from app.configuracao.ma import ma
from .models import Livro

class LivroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Livro