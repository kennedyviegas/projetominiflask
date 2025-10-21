# Ponto de entrada para executar a aplicação
from src import create_app

app = create_app()

if __name__ == '__main__':
    # O debug=True é pego do config.py
    app.run(debug=app.config['DEBUG'])