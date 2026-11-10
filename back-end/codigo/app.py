from flask import Flask
from flask_cors import CORS  # 1. Importe o flask-cors

from routes.atividade_router import atividade_bp 
from routes.jogador_router import jogador_bp

from services.db_service import db
from dao.jogador_dao import JogadorDAO
from dao.atividade_dao import AtividadeDAO

app = Flask(__name__)

# 2. Ative o CORS para a aplicação inteira
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(atividade_bp)
app.register_blueprint(jogador_bp)

if __name__ == '__main__':
    with app.app_context(): # contexto do app inicializado para criar a tabela
        JogadorDAO.criar_tabela_jogador()
        AtividadeDAO.criar_tabela_atividade()
    app.run(debug=True, port=5000)