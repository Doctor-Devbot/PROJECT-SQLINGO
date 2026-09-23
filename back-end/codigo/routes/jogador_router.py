from flask import Blueprint, request
from dao.jogador_dao import JogadorDAO

jogador_bp = Blueprint('jogador', __name__)

# POST /jogador
@jogador_bp.route("/jogador", methods=["POST"])
def cadastrar_jogador():
    novo_jogador = request.get_json()
    jogador_criado = JogadorDAO.create(
        novo_jogador["nome"],
        novo_jogador["email"]
    )
    if jogador_criado is None:
        return {"erro": "Email já cadastrado"}, 400
    return jogador_criado, 201


# GET /jogador
@jogador_bp.route("/jogador", methods=["GET"])
def todos_jogadores():
    if JogadorDAO.size() == 0:
        return {"erro": "Nenhum jogador cadastrado"}, 404
    return JogadorDAO.retrieve_all(), 200


# GET /jogador/email%40gmail.com
@jogador_bp.route("/jogador/<string:email>", methods=["GET"])
def buscar_jogador(email):
    jogador_encontrado = JogadorDAO.retrieve_by_email(email)
    if jogador_encontrado is None:
        return {"erro": "Jogador não encontrado"}, 404
    return jogador_encontrado, 200


# DELETE /jogador/email%40gmail.com
@jogador_bp.route("/jogador/<string:email>", methods=["DELETE"])
def remover_jogador(email):
    jogador = JogadorDAO.delete(email)
    if jogador is None:
        return {"erro": "Jogador não encontrado"}, 404
    return jogador, 200


# PUT /jogador/email%40gmail.com
@jogador_bp.route("/jogador/<string:email>", methods=["PUT"])
def atualizar_nome(email):
    dados = request.get_json()
    jogador_atualizado = JogadorDAO.update_nome(
        email,
        dados["nome"]
    )
    if jogador_atualizado is None:
        return {"erro": "Jogador não encontrado"}, 404
    return jogador_atualizado, 200