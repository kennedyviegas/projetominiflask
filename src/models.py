# Lógica de "banco de dados" em memória

# Usamos um dicionário simples como nosso banco de dados em memória
db = {
    "users": {
        1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
        2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
    }
}

# Contador para simular o auto-incremento de IDs
current_user_id = 2

def get_all_users():
    """Retorna todos os usuários do 'banco'."""
    # Retornamos uma lista dos valores do dicionário
    return list(db["users"].values())

def add_user(user_data):
    """Adiciona um novo usuário ao 'banco'."""
    global current_user_id
    current_user_id += 1
    
    new_user = {
        "id": current_user_id,
        "name": user_data["name"],
        "email": user_data["email"]
    }
    db["users"][current_user_id] = new_user
    return new_user

def get_user_by_id(user_id):
    """Busca um usuário pelo ID (requisito opcional)."""
    return db["users"].get(user_id)