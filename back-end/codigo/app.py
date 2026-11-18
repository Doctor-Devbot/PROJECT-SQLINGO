import os
from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from dao.atividade_dao import AtividadeDAO
from dao.jogador_dao import JogadorDAO
from dao.lista_atividade_dao import ListaAtividadeDAO
from dao.modulo_dao import ModuloDAO
from routes.atividade_router import atividade_bp
from routes.jogador_router import jogador_bp
from routes.lista_atividade_router import lista_atividade_bp
from routes.modulo_router import modulo_bp
from services.db_service import db

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configurações do Banco de Dados
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

if __name__ == "__main__":
  with app.app_context():
    JogadorDAO.criar_tabela_jogador()
    AtividadeDAO.criar_tabela_atividade()
    ModuloDAO.criar_tabela_modulo()
    ListaAtividadeDAO.criar_tabela_lista_atividade()
  app.run(debug=True, port=5000)