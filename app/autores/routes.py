from flask import Blueprint, request, jsonify
from .models import Autor
from .schemas import AutorSchema
from app.configuracao.db import db
from app.configuracao.auth import admin_required
from flask_jwt import jwt_required

autor = Blueprint('autor', __name__)

@autor.route("/",methods= ['GET'])
@jwt_required()
def autor_read():
    autoreschema = AutorSchema(many=True)
    readAutores  = Autor.query.order_by(Autor.name).all()
    dados = autoreschema.dump(readAutores)
    return autoreschema.jsonify(dados)

@autor.route("/", methods=['POST'])
@admin_required()
def autor_create():
    name = request.json["name"]
    newAutor = Autor(name)
    db.session.add(newAutor)
    db.session.commit()
    
    autorschema = AutorSchema()
    dados = {}
    dados["data"] = autorschema.dump(newAutor)
    dados["mensagem"] = "Autor criado com sucesso!"
    return jsonify(dados)

@autor.route("/<int:id>",methods=['PUT'])
@admin_required()
def autor_upgrade(id):
    dados = {}
    autor = Autor.query.filter_by(id=id).first()
    
    
    #importante
    try:
        name = request.json["name"]
        autor.name = name
        db.session.commit()
        autorschema = AutorSchema()

        dados["data"] = autorschema.dump(autor)
        dados["mensagem"] = "Autor atualizado com sucesso!"
        return jsonify(dados), 200

    except AttributeError:
        dados["mensagem"] = "Autor não existe."
        return jsonify(dados), 404

    except KeyError:
        dados["mensagem"] = "Dados inválidos!"
        #lembrar
        return jsonify(dados),400
    


@autor.route("/<int:id>",methods=['DELETE'])
@admin_required()
def autor_delete(id):
    autor = Autor.query.get(id)

    db.session.delete(autor)
    db.session.commit()

    autorschema = AutorSchema()
    dados = {}
    dados["data"] = autorschema.dump(autor)
    dados["mensagem"] = "Autor deletado com sucesso!"

    return jsonify(dados)
