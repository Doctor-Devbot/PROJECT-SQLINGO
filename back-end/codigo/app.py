import os
from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from dao.atividade_dao import AtividadeDAO
from dao.jogador_atividade_dao import JogadorAtividadeDAO
from dao.jogador_dao import JogadorDAO
from dao.lista_atividade_dao import ListaAtividadeDAO
from dao.modulo_dao import ModuloDAO
from routes.atividade_router import atividade_bp
from routes.jogador_router import jogador_bp
from routes.lista_atividade_router import lista_atividade_bp
from routes.modulo_router import modulo_bp
from services.db_service import db

# Carrega as variáveis do arquivo .env local (dev) ou do painel da nuvem (Render)
load_dotenv()

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Banco de Dados (Aula 15 - Gerenciamento de Segredos):
# - NUVEM (Render + MySQL Aiven): quando DB_PASSWORD está definida no painel,
#   a API conecta ao banco da nuvem via SSL, igual à URI da Aula 14:
#   mysql+pymysql://usuario:senha@host:porta/nome_do_banco
# - DESENVOLVIMENTO LOCAL: sem DB_PASSWORD no ambiente, a API cai
#   automaticamente no SQLite original, mantendo o funcionamento do projeto.
# ---------------------------------------------------------------------------
DB_PASSWORD = os.getenv("DB_PASSWORD")

if DB_PASSWORD:
    DB_USER = os.getenv("DB_USER", "avnadmin")
    DB_HOST = os.getenv("DB_HOST", "")
    DB_PORT = os.getenv("DB_PORT", "28010")
    DB_NAME = os.getenv("DB_NAME", "defaultdb")

    if not DB_HOST:
        raise RuntimeError(
            "DB_PASSWORD definida, mas DB_HOST ausente: cadastre nas variáveis "
            "de ambiente o host do serviço MySQL do Aiven (ex.: "
            "mysql-xxxx.aivencloud.com)."
        )

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    # Aula 14: bancos na nuvem exigem criptografia SSL (opção ssl ativa no PyMySQL)
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"connect_args": {"ssl": {}}}
else:
    # Desenvolvimento local: SQLite (comportamento original do projeto)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meu_banco.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Configurações de Autenticação (JWT e Bcrypt)
# Busca do .env em produção ou usa a padrão em desenvolvimento local
app.config["JWT_SECRET_KEY"] = os.getenv(
    "JWT_SECRET_KEY", "sua_chave_super_secreta"
)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# Registro de Blueprints
app.register_blueprint(atividade_bp)
app.register_blueprint(jogador_bp)
app.register_blueprint(modulo_bp)
app.register_blueprint(lista_atividade_bp)

# Aula 15: o CORS fica DEPOIS do registro dos blueprints e libera as rotas
# da API para o Front-End consumir (política de mesma origem/SOP).
CORS(app, resources={
    r"/*": {"origins": "*"},  # liberado para qualquer domínio (fase de protótipo)
})

# ---------------------------------------------------------------------------
# Criação das tabelas na INICIALIZAÇÃO (Aula 15 - Deploy com Gunicorn):
# este bloco executa no momento do import do módulo, garantindo as tabelas
# tanto com `python app.py` (dev) quanto com `gunicorn app:app` (Render),
# já que o Gunicorn NÃO executa o bloco if __name__ == "__main__".
# A ordem respeita as chaves estrangeiras: modulos -> listas -> atividades,
# e por último a tabela intermediária do relacionamento N:N (Aula 14).
# ---------------------------------------------------------------------------
with app.app_context():
    ModuloDAO.criar_tabela_modulo()                 # 1. tabela sem dependências
    ListaAtividadeDAO.criar_tabela_lista_atividade()  # 2. FK -> modulos
    AtividadeDAO.criar_tabela_atividade()           # 3. FK -> listas_atividade
    JogadorDAO.criar_tabela_jogador()               # 4. tabela sem dependências
    JogadorAtividadeDAO.criar_tabela_jogador_atividade()  # 5. N:N (FK dupla)

# Servidor de desenvolvimento: NUNCA usar em produção (Aula 15) -
# na nuvem o Render executa o Gunicorn via Procfile/Start Command.
if __name__ == "__main__":
    app.run(debug=True, port=5000)
