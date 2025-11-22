# Padrão "Application Factory"
from flask import Flask
from .config import Config

def create_app():
    """
    Factory para criar e configurar a instância da aplicação Flask.
    """
    app = Flask(__name__)
    
    # 1. Carregar configurações
    app.config.from_object(Config)
    
    # 2. Registrar Blueprints (rotas)
    from . import routes
    app.register_blueprint(routes.users_bp)

    from src.routes import exchange_bp
    app.register_blueprint(exchange_bp)
    
    # 3. (Opcional) Adicionar uma rota raiz simples
    @app.route('/')
    def index():
        return "Mini API está no ar! Acesse /users"

    return app