from app.livros.models import Livro
from datetime import datetime, timedelta

def take_books(ids: list):
    livros = []
    for id in ids:
        livro = Livro.query.get(id)
        if livro:
            livros.append(livro)
            
    return livros


def gerar_prazo():
    return datetime.now() + timedelta(days=10)