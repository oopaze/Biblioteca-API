from app.usuarios.models import User
from flask_jwt import JWT


def authenticate(username, password):
    """Função que controla a authenticacao do usuario"""
    user = User.query.filter_by(registration=registration).scalar()
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
    return jwt