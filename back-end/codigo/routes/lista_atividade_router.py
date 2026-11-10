from flask import Blueprint, request
from services.lista_atividade_service import ListaAtividadeService

lista_atividade_bp = Blueprint('lista_atividade', __name__)
lista_service = ListaAtividadeService()

@lista_atividade_bp.route("/lista-atividade", methods=["GET"])
def todas_listas():
    try:
        return lista_service.listar_todas(), 200
    except ValueError as e:
        return {"erro": str(e)}, 404

@lista_atividade_bp.route("/lista-atividade/<int:id_lista>", methods=["GET"])
def buscar_lista(id_lista):
    try:
        return lista_service.obter_lista(id_lista), 200
    except ValueError as e:
        return {"erro": str(e)}, 404

@lista_atividade_bp.route("/lista-atividade", methods=["POST"])
def cadastrar_lista():
    dados = request.get_json() or {}
    try:
        return lista_service.cadastrar_lista(dados), 201
    except ValueError as e:
        return {"erro": str(e)}, 400