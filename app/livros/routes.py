from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required

from app.configuracao.auth import admin_required
from app.configuracao.db import db

from app.usuarios.schemas import UserSchema
from app.autores.schemas import AutorSchema
from .schemas import LivroSchema
from .models import Livro


livro = Blueprint('livro', __name__)

@livro.route('/', methods=['GET'])
@jwt_required()
def ver_livros():
    livroschema = LivroSchema(many=True)
    autorschema = AutorSchema(many=True)
    livros = Livro.query.all()

    if livros:
        dados = livroschema.dump(livros)
        for i,dado in enumerate(dados):
            dado['autores'] = autorschema.dump(livros[i].autores)

    else:
        dados = {
            'message': 'Nenhum livro cadastrado.'
        }

    return jsonify(dados), 200


@livro.route('/<int:id>', methods=['GET'])
@jwt_required()
def ver_livro(id):
    livroschema = LivroSchema()
    livro = Livro.query.get(id)
    
    autorschema = AutorSchema(many=True)

    if livro:
        dados = livroschema.dump(livro)
        dados['autores'] = autorschema.dump(livro.autores)
    
    else:
        dados = {
            'message': 'Livro não cadastrado.'
        }

    return jsonify(dados), 200


@livro.route('/', methods=['POST'])
@admin_required()
def adicionar_livro():
    livroschema = LivroSchema()
    autorschema = AutorSchema(many=True)
    
    try:
        livro = Livro(**request.json)
        db.session.add(livro)
        
        if 'autores' in request.json:
            livro.autores = livro.adicionar_autor(request.json['autores'])

        db.session.commit()

        dados = livroschema.dump(livro)
        dados['autores'] = autorschema.dump(livro.autores)
        livro = dados

        data = {
            'message': 'Livro adicionado com sucesso.',
            'data': livro
        }

        return jsonify(data), 201

    except (ValueError, TypeError):
        data = {
            'message': 'Erro ao adicionar livro.'
        }

        return jsonify(data), 400


@livro.route('/varios/', methods=['POST'])
@admin_required()
def adicionar_varios_livros():
    livroschema = LivroSchema()
    autorschema = AutorSchema(many=True)
    data = []

    for livro in request.json:
        _livro = Livro(**livro)

        db.session.add(_livro)
        db.session.commit()
    
        if 'autores' in livro:
            autores = _livro.adicionar_autor(livro['autores'])
            
            for autor in autores:
                _livro.autores.append(autor)

            db.session.commit()
        
        dados = livroschema.dump(_livro)
        dados['autores'] = autorschema.dump(_livro.autores)
        
        data.append(dados)

    return jsonify(data), 201


@livro.route('/<int:id>', methods=['PUT'])
@admin_required()
def atualizar_livro(id):
    livroschema = LivroSchema()
    autorschema = AutorSchema(many=True)
    livro = Livro.query.get(id)

    if livro:
        if 'autores' in request.json:
            livro.autores = livro.adicionar_autor(request.json['autores'])

        try:
            livro.titulo = request.json['titulo']
            livro.vol = request.json['vol']

            db.session.commit()

            dados = {
                'message': 'Livro atualizado com sucesso.'
            }
            dados['data'] = livroschema.dump(livro)
            dados['data']['autores'] = autorschema.dump(livro.autores)
            livro = dados

            return jsonify(livro), 200

        except (ValueError, KeyError):
            dados = {
                'message': 'Erro ao atualizar livro.'
            }

        return jsonify(dados), 400
    
    dados = {
        'message': 'Livro não encontrado.'
    }
    
    return jsonify(dados), 404


@livro.route('/<int:id>', methods=['DELETE'])
@admin_required()
def delete_livro(id):
    livroschema = LivroSchema()
    autorschema = AutorSchema(many=True)
    livro = Livro.query.get(id)

    if livro:
        try:
            db.session.delete(livro)
            db.session.commit()

            dados = {
                'message': 'Livro deletado com sucesso.'
            }
            dados['data'] = livroschema.dump(livro)
            dados['data']['autores'] = autorschema.dump(livro.autores)
            livro = dados

            return jsonify(livro), 200

        except (ValueError, TypeError):
            dados = {
                'message': 'Erro ao atualizar livro.'
            }

        return jsonify(dados), 400
    
    dados = {
        'message': 'Livro não encontrado.'
    }
    return jsonify(dados), 404