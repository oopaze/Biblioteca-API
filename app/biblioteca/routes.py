from flask import Blueprint, request, jsonify

from app.configuracao.db import db

biblioteca = Blueprint('biblioteca', __name__)