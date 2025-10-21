Markdown# Mini API em Flask (Projeto)

Este projeto é uma Mini API desenvolvida em Python 3.11+ com Flask, como parte de uma atividade de avaliação. A API implementa endpoints CRUD básicos para gerenciamento de usuários (em memória) e segue uma estrutura de projeto escalável e boas práticas de versionamento.

**Status do Projeto:** Concluído (Requisitos Mínimos)

---

## 1. Estrutura de Diretórios

O projeto utiliza o padrão *Application Factory* para escalabilidade futura:

/miniapi├── /src              # Código fonte da aplicação│   ├── init.py│   ├── app.py        # Factory create_app()│   ├── routes.py     # Definição dos Blueprints (endpoints)│   ├── models.py     # Lógica de acesso a dados (em memória)│   └── config.py     # Configurações (Debug, Secret Key)├── /tests            # Testes unitários/integração│   └── test_example.py├── run.py            # Ponto de entrada para executar a app├── README.md         # Esta documentação├── requirements.txt  # Dependências└── .gitignore        # Arquivos ignorados pelo Git
## 2. Instalação e Execução

**Pré-requisitos:** Python 3.10+ e `pip`.

**1. Clone o repositório:**
```bash
git clone SUA_URL_AQUI.git
cd miniapi
2. Crie e ative um ambiente virtual:Bash# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
3. Instale as dependências:Bashpip install -r requirements.txt
4. Execute a aplicação:Bashpython run.py
A API estará rodando em http://127.0.0.1:5000.3. Endpoints da APIMétodoEndpointDescriçãoExemplo de Body (POST)GET/usersLista todos os usuários.N/APOST/usersCria um novo usuário.{"name": "Seu Nome", "email": "seu@email.com"}GET/users/<id>Busca um usuário por ID.N/A4. Estratégia de Versionamento e Comandos GitEste projeto utiliza um fluxo baseado em Git Flow simplificado (main, develop, feature/*).Fluxo de Criação e Feature (Exemplos)Criação do repositório local e primeiro push:Bashmkdir miniapi && cd miniapi
git init
git branch -M main
# ... criar virtualenv, arquivos ...
git add .
git commit -m "feat: estrutura inicial do projeto"
# ... criar repo remoto no GitHub/GitLab ...
git remote add origin <URL_DO_REPO>
git push -u origin main
Criar branches e fluxo de feature:Bash# Criar branch develop
git checkout -b develop
git push -u origin develop

# Criar feature
git checkout -b feature/users-crud

# ... desenvolver, adicionar e commitar alterações ...
git add src/
git commit -m "feat(users): adicionar endpoints GET/POST /users"

# Push e abrir PR/MR
git push -u origin feature/users-crud
# (Após revisão, mesclar feature em develop via PR/MR)
Sincronizar e atualizar branches:Bash# Atualizar develop
git checkout develop
git pull origin develop

# Rebase/merge da develop na feature (opcional)
git checkout feature/users-crud
git rebase develop
# ou
git merge develop
