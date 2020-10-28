from flask import Blueprint, request, jsonify
from .models import Autor

autor = Blueprint('autor', __name__)

@autor.route("/Autor")
def Autor():
    r  = Autor.query.order_by(Autor.name).all()
    return r

@autor.route("/create/<nameAutor>")
def AutorCreate(nameAutor):
    newAutor = Autor(name)
    db.session.add(newAutor)
    db.session.commit()
    return "Autor adicionado!"

@autor.route("/upgrade/<nameAutor>")
def AutorUpgrade(nameAutor):
    Autor = Autor.query.filter_by(name=nameAutor).first()
    Autor.name = nameAutor
    db.session.add(Autor)
    db.session.commint()
    return "Autor Atualizado"

@autor.route("/delete/<nameAutor>")
def AutorDelete(nameAutor):
    db.session.delete(nameAutor)
    db.session.commit()
    return "Autor removido"
