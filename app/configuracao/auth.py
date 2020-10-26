from app.usuarios.models import User
from flask_jwt import JWT
from datetime import timedelta


def authenticate(username, password):
    """Função que controla a authenticacao do usuario"""
    user = User.query.filter_by(username=username).scalar()
    if user.verify_password(password):
        return user

def identity(payload):
    """Função que mantém o login do usuário"""
    return User.query.filter(User.id == payload['identity']).scalar()



jwt = JWT(authentication_handler = authenticate, identity_handler = identity)

def configure_auth(app):
    """Função de configuracao do login dentro da nossa app"""
    jwt.init_app(app)
    
    app.config['JWT_AUTH_USERNAME_KEY'] = 'username'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

    return jwt