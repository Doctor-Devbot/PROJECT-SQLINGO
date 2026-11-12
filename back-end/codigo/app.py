from flask import Flask
from flask_cors import CORS

from routes.atividade_router import atividade_bp 
from routes.jogador_router import jogador_bp
from routes.modulo_router import modulo_bp
from routes.lista_atividade_router import lista_atividade_bp

from services.db_service import db
from dao.jogador_dao import JogadorDAO
from dao.atividade_dao import AtividadeDAO
from dao.modulo_dao import ModuloDAO
from dao.lista_atividade_dao import ListaAtividadeDAO

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(atividade_bp)
app.register_blueprint(jogador_bp)
app.register_blueprint(modulo_bp)
app.register_blueprint(lista_atividade_bp)

if __name__ == '__main__':
    with app.app_context():
        JogadorDAO.criar_tabela_jogador()
        AtividadeDAO.criar_tabela_atividade()
        ModuloDAO.criar_tabela_modulo()
        ListaAtividadeDAO.criar_tabela_lista_atividade()
<<<<<<< HEAD
    app.run(debug=True, port=5001)
=======
    app.run(debug=True, port=5000)
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
