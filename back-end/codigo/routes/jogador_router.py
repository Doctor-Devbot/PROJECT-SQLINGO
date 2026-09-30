from flask import Blueprint, request
from services.jogador_service import JogadorService

jogador_bp = Blueprint('jogador', __name__)
jogador_service = JogadorService()

# POST /jogador
@jogador_bp.route("/jogador", methods=["POST"])
def cadastrar_jogador():
    dados = request.get_json() or {}
    try:
        jogador_criado = jogador_service.cadastrar_jogador(dados)
        return jogador_criado, 201
    except ValueError as e:
        return {"erro": str(e)}, 400

# GET /jogador
@jogador_bp.route("/jogador", methods=["GET"])
def todos_jogadores():
    try:
        jogadores = jogador_service.listar_todos()
        return jogadores, 200
    except ValueError as e:
        return {"erro": str(e)}, 404

# GET /jogador/email@gmail.com
@jogador_bp.route("/jogador/<string:email>", methods=["GET"])
def buscar_jogador(email):
    try:
        jogador = jogador_service.obter_jogador_por_email(email)
        return jogador, 200
    except ValueError as e:
        return {"erro": str(e)}, 404

# PUT /jogador/email@gmail.com
@jogador_bp.route("/jogador/<string:email>", methods=["PUT"])
def atualizar_nome(email):
    dados = request.get_json() or {}
    try:
        jogador_atualizado = jogador_service.atualizar_nome(email, dados)
        return jogador_atualizado, 200
    except ValueError as e:
        return {"erro": str(e)}, 404

# DELETE /jogador/email@gmail.com
@jogador_bp.route("/jogador/<string:email>", methods=["DELETE"])
def remover_jogador(email):
    try:
        jogador_removido = jogador_service.deletar_jogador(email)
        return jogador_removido, 200
    except ValueError as e:
        return {"erro": str(e)}, 404