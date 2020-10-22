from flask_marshmallow import Marshmallow

ma = Marshmallow()

def configure_ma(app):
    ma.init_app(app)