from app.configuracao.ma import ma
from .models import Autor

class AutorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Autor
        fields = ("id", "name")