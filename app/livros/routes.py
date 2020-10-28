from flask import Blueprint, request, jsonify

from app.usuarios.schemas import UserSchema
from app.configuracao.db import db
from .schemas import LivroSchema
from .models import Livro

livro = Blueprint('livro', __name__)


@livro.route('/', methods=['GET'])
def ver_livros():
    livroschema = LivroSchema(many=True)
    userschema = UserSchema()
    livros = Livro.query.all()

    if livros:
        dados = livroschema.dump(livros)
        dados['autores'] = []
        dados['usuario_aluguel'] = userschema.dump(livros.usuario_aluguel)
    
    else:
        dados = {
            'message': 'Nenhum livro cadastrado.'
        }

    return jsonify(dados), 200



@livro.route('/<int:id>', methods=['GET'])
def ver_livro(id):
    livroschema = LivroSchema()
    userschema = UserSchema()
    livro = Livro.query.get(id=id)

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
def adicionar_livro():
    livroschema = LivroSchema()
    
    livro = Livro(**request.json)
    if 'autores' in request.json:
        livro.autores = request.json['autores']
        
    try:
        db.session.add(livro)
        db.session.commit()

        livro = livroschema.dump(livro)
        livro['autores'] = []

        data = {
            'message': 'Livro adicionado com sucesso',
            'data': livro
        }

        return jsonify(data), 201

    except ValueError:
        data = {
            'message': 'Erro ao adicionar livro'
        }

        return jsonify(data), 400
    

@livro.route('/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    ...

@livro.route('/<int:id>', methods=['DELETE'])
def delete_livro():
    ...