from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required, current_identity
from app.configuracao.db import db

from app.usuarios.models import User

from .utils import take_books
from .schemas import EmprestimoSchema, LivroSchema
from .models import Emprestimo

biblioteca = Blueprint('biblioteca', __name__)

@biblioteca.route('/', methods=['POST'])
@jwt_required()
def emprestar_livro():
    emprestimo_schema = EmprestimoSchema()
    livro_schema = LivroSchema(many=True)

    livros = take_books(request.json['livros'])
    usuario = current_identity
    if 'usuario' in request.json:
        usuario = User.query.get(request.json['usuario'])
        
    emprestimo = Emprestimo()

    db.session.add(emprestimo)
    db.session.commit()

    usuario.emprestimos.append(emprestimo)
    for i in range(len(livros)):
        livros[i].disponivel = False
        emprestimo.livros.append(livros[i])

    db.session.commit()

    data = emprestimo_schema.dump(emprestimo)
    data['livros'] = livro_schema.dump(livros)
    data['usuario'] = usuario.name


    return jsonify(data), 201

    
