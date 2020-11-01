from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required, current_identity

from app.configuracao.db import db
from app.configuracao.auth import admin_required
from app.usuarios.models import User
from app.livros.models import Livro

from .utils import take_books
from .schemas import EmprestimoSchema, LivroSchema
from .models import Emprestimo

biblioteca = Blueprint('biblioteca', __name__)

@biblioteca.route('/emprestar/', methods=['POST'])
@jwt_required()
def emprestar_livro():
    emprestimo_schema = EmprestimoSchema()
    livro_schema = LivroSchema(many=True)

    try:
        livros = take_books(request.json['livros'])
        if len(livros) == 0:
            raise KeyError(
                "Livros não encontrado."
            )
        usuario = current_identity
        if 'usuario' in request.json:
            usuario = User.query.get(request.json['usuario'])

        if isinstance(usuario.emprestimo, Emprestimo):
            raise ValueError(
                "É possível fazer somente um emprestimo por vez."
            )
            
        emprestimo = Emprestimo()

        usuario.emprestimo = emprestimo
        for i in range(len(livros)):
            if not livros[i].disponivel:
                raise ValueError()
            livros[i].disponivel = False
            emprestimo.livros.append(livros[i])

        db.session.add(emprestimo)
        db.session.commit()

        data = {}
        data['data'] = emprestimo_schema.dump(emprestimo)
        data['data']['livros'] = livro_schema.dump(livros)
        data['data']['usuario'] = usuario.name
        data['message'] = 'Livros emprestados com sucesso.'

        return jsonify(data), 201

    except KeyError:
        data = {
            'message': 'Livro não encontrado.'
        }

        return jsonify(data), 404

    except AttributeError:
        data = {
            'message': 'Usuário não encontrado.'
        }

        return jsonify(data), 404

    except ValueError:
        data = {
            'message': 'Usuario já tem um emprestimo ou livro está indisponivel.'
        }

        return jsonify(data), 400

    
@biblioteca.route('/entregar/', methods=['POST'])
@jwt_required()
def entregar_livro():
    emprestimo_schema = EmprestimoSchema()
    livro_schema = LivroSchema(many=True)

    try:
        usuario = current_identity
        if 'usuario' in request.json:
            usuario = User.query.get(request.json['usuario'])

        emprestimo = usuario.emprestimo
        emprestimo.entregue_em = datetime.now()
        usuario.emprestimo = None

        for livro in emprestimo.livros:
            livro.disponivel = True

        data = {}
        data['data'] = emprestimo_schema.dump(emprestimo)
        data['data']['livros'] = livro_schema.dump(emprestimo.livros)
        data['data']['usuario'] = usuario.name
        data['message'] = 'Livros entregues com sucesso.'

        db.session.commit()

        return jsonify(data), 200

    except AttributeError:
        data = {
            'message': 'Usuário não encontrado ou sem emprestimos pendentes.'
        }

        return jsonify(data), 404


@biblioteca.route('/pendencias/', methods=['GET'])
@admin_required()
def emprestimos_pendencias():
    emprestimo_schema = EmprestimoSchema(many=True)
    livro_schema = LivroSchema(many=True)

    emprestimos = Emprestimo.query.filter(
                        Emprestimo.data_previsao_entrega < datetime.now(), 
                        Emprestimo.data_entrega == None
                    ).all()

    data = {}

    if len(emprestimos) > 0:
        data['data'] = emprestimo_schema.dump(emprestimos)
        for i,emprestimo in enumerate(data['data']):
            emprestimo['livros'] = livro_schema.dump(emprestimos[i].livros)

        return jsonify(data), 200

    data['message'] = "Nenhum empréstimo com pendência"
    return jsonify(data)


@biblioteca.route('/emprestimos/', methods=['GET'])
@admin_required()
def ler_emprestimos():
    emprestimo_schema = EmprestimoSchema(many=True)
    livro_schema = LivroSchema(many=True)

    emprestimos = Emprestimo.query.all()

    data = emprestimo_schema.dump(emprestimos)
    for i,emprestimo in enumerate(data):
        emprestimo['livros'] = livro_schema.dump(emprestimos[i].livros)

    if not emprestimos:
        data = {'message': "Nenhum emprestimo feito."}

    return jsonify(data), 200

@biblioteca.route('/disponiveis/', methods = ['GET'])
@jwt_required()
def livro_disponiveis():
    livroschema = LivroSchema(many=True)
    disponiveis = Livro.query.filter(Livro.disponivel==True).all()
    dados = livroschema.dump(disponiveis)
    if len(disponiveis) == 0:
        dados = {'message': "Nenhum livro disponivel"}

    return disponiveis.jsonify(dados)

@biblioteca.route('/indisponiveis/', methods = ['GET'])
@adm_required()
def livro_indisponiveis():
    livroschema = LivroSchema(many=True)
    disponiveis = Livro.query.filter(Livro.disponivel==False).all()
    dados = livroschema.dump(disponiveis)
    if len(disponiveis) == 0:
        dados = {'message': "Nenhum livro indisponivel"}
    return disponiveis.jsonify(dados)
