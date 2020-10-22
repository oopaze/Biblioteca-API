from flask_migrate import Migrate
from flask import Flask

from .configuracao.db import configure_db
from .configuracao.ma import configure_ma
from .configuracao.auth import configure_auth

def create_app():
    """Função responsável por configurar e criar nossa app"""
    app = Flask(__name__)

    app.config.from_object('config.Development')
    
    configure_db(app)
    configure_ma(app)
    configure_auth(app)

    Migrate(app, app.db)

    from app.autores.routes import autor
    from app.biblioteca.routes import biblioteca
    from app.livros.routes import livro
    from app.usuarios.routes import usuario

    app.register_blueprint(autor, prefix='/autor')
    app.register_blueprint(biblioteca, prefix='/biblioteca')
    app.register_blueprint(livro, prefix='/livro')
    app.register_blueprint(usuario, prefix='/user')

    return app

app = create_app()