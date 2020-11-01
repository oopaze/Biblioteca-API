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
    read_autores  = Autor.query.order_by(Autor.name).all()
    dados = autoreschema.dump(read_autores)
    return autoreschema.jsonify(dados)

@autor.route("/", methods=['POST'])
@admin_required()
def autor_create():
    dados = {}
    try:
        name = request.json["name"]
        newAutor = Autor(name)
        db.session.add(newAutor)
        db.session.commit()
        
        autorschema = AutorSchema()
        
        dados["data"] = autorschema.dump(newAutor)
        dados["mensagem"] = "Autor criado com sucesso!"
        return jsonify(dados), 201
    except:
        dados["mensagem"] = "Dados inválidos!"
        return jsonify(dados),400

@autor.route("/<int:id>",methods=['PUT'])
@admin_required()
def autor_upgrade(id):
    dados = {}
    autor = Autor.query.filter_by(id=id).first()
    
    
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
        return jsonify(dados),400
    


@autor.route("/<int:id>",methods=['DELETE'])
@admin_required()
def autor_delete(id):
    dados = {}
    try:
        autor = Autor.query.get(id)

        db.session.delete(autor)
        db.session.commit()

        autorschema = AutorSchema()
        
        dados["data"] = autorschema.dump(autor)
        dados["mensagem"] = "Autor deletado com sucesso!"

        return jsonify(dados)
    except: 
        dados["mensagem"] = "Impossivel excluir autor, verificar dados."
        return jsonify(dados)
