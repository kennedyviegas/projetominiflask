# Definição dos Endpoints (Blueprints)
from flask import Blueprint, request, jsonify
from . import models

# Criamos um Blueprint para organizar as rotas de usuários
# Isso é escalável, poderíamos ter 'products_bp', 'orders_bp', etc.
users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    """
    [GET] /users
    Retorna uma lista de todos os usuários.
    """
    users = models.get_all_users()
    return jsonify(users), 200

@users_bp.route('/users', methods=['POST'])
def create_user():
    """
    [POST] /users
    Cria um novo usuário com base no JSON enviado.
    JSON esperado: {"name": "...", "email": "..."}
    """
    data = request.get_json()
    
    # Validação simples
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Dados inválidos. 'name' e 'email' são obrigatórios."}), 400
        
    new_user = models.add_user(data)
    
    # Retorna o usuário criado com o ID e status 201 (Created)
    return jsonify(new_user), 201

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    [GET] /users/<id>
    (Opcional) Retorna um usuário específico pelo ID.
    """
    user = models.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404