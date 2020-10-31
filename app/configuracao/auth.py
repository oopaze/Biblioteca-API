from datetime import timedelta
from functools import wraps
from flask_jwt import (
    JWT,
    JWTError, 
    _jwt_required, 
    current_app, 
    current_identity
)

from app.usuarios.models import User


def authenticate(username, password):
    """Função que controla a authenticacao do usuario"""
    user = User.query.filter_by(username=username).scalar()
    if user:
        if user.verify_password(password):
            return user

def identity(payload):
    """Função que mantém o login do usuário"""
    return User.query.filter(User.id == payload['identity']).scalar()

jwt = JWT(authentication_handler = authenticate, identity_handler = identity)

def configure_auth(app):
    """Função de configuracao do login dentro da nossa app"""
    jwt.init_app(app)

def admin_required(realm=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            _jwt_required(realm or current_app.config['JWT_DEFAULT_REALM'])
            if current_identity.admin:
                return fn(*args, **kwargs)

            raise JWTError(
                    'Authorization Required', 
                    'You are not admin',
                    headers={
                       'WWW-Authenticate': 'JWT realm="%s"' %current_app.config['JWT_DEFAULT_REALM']
                    }
                )
        return decorator
    return wrapper
