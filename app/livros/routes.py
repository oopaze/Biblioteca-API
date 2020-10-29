from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required

from app.configuracao.auth import admin_required
from app.configuracao.db import db

from app.usuarios.schemas import UserSchema
from .schemas import LivroSchema
from .models import Livro


livro = Blueprint('livro', __name__)

@livro.route('/', methods=['GET'])
@jwt_required()
def ver_livros():
    livroschema = LivroSchema(many=True)
    userschema = UserSchema()
    livros = Livro.query.all()

    if livros:
        dados = livroschema.dump(livros)
        for i,dado in enumerate(dados):
            dado['autores'] = []
            dado['usuario_aluguel'] = userschema.dump(livros[i].usuario_aluguel)

    else:
        dados = {
            'message': 'Nenhum livro cadastrado.'
        }

    return jsonify(dados), 200

@livro.route('/<int:id>', methods=['GET'])
@jwt_required()
def ver_livro(id):
    livroschema = LivroSchema()
    userschema = UserSchema()
    livro = Livro.query.get(id)

    if livro:
        dados = livroschema.dump(livro)
        dados['autores'] = []
        dados['usuario_aluguel'] = userschema.dump(livro.usuario_aluguel)
    
    else:
        dados = {
            'message': 'Nenhum livro cadastrado.'
        }

    return jsonify(dados), 200

@livro.route('/', methods=['POST'])
@admin_required()
def adicionar_livro():
    livroschema = LivroSchema()
    
    try:
        livro = Livro(**request.json)
        db.session.add(livro)
        
        if 'autores' in request.json:
            livro.autores = livro.adicionar_autores(request.json['autores'])

        db.session.commit()

        dados = livroschema.dump(livro)
        dados['autores'] = []
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
    
@livro.route('/<int:id>', methods=['PUT'])
@admin_required()
def atualizar_livro(id):
    livroschema = LivroSchema()
    livro = Livro.query.get(id)

    if livro:
        if 'autores' in request.json:
            livro.adicionar_autor(request.json['autores'])
        try:
            livro.titulo = request.json['titulo']
            livro.vol = request.json['vol']

            db.session.commit()

            dados = {
                'message': 'Livro atualizado com sucesso.'
            }
            dados['data'] = livroschema.dump(livro)
            dados['data']['autores'] = livro.autores
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
    livro = Livro.query.get(id)

    if livro:
        try:
            db.session.delete(livro)
            db.session.commit()

            dados = {
                'message': 'Livro deletado com sucesso.'
            }
            dados['data'] = livroschema.dump(livro)
            dados['data']['autores'] = livro.autores
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