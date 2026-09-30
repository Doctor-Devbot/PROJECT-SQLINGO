from flask import Blueprint, request
from services.atividade_service import AtividadeService

atividade_bp = Blueprint('atividade', __name__)
atividade_service = AtividadeService()

# POST /atividade
@atividade_bp.route("/atividade", methods=["POST"])
def cadastrar_atividade():
    dados = request.get_json() or {}
    try:
        atividade_criada = atividade_service.cadastrar_atividade(dados)
        return atividade_criada, 201
    except ValueError as e:
        return {"erro": str(e)}, 400

# GET /atividade
@atividade_bp.route("/atividade", methods=["GET"])
def todas_atividades():
    try:
        atividades = atividade_service.listar_todas()
        return atividades, 200
    except ValueError as e:
        return {"erro": str(e)}, 404

# GET /atividade/1
@atividade_bp.route("/atividade/<int:id_atividade>", methods=["GET"])
def buscar_atividade(id_atividade):
    try:
        atividade = atividade_service.obter_atividade(id_atividade)
        return atividade, 200
    except ValueError as e:
        return {"erro": str(e)}, 404

# PUT /atividade/1
@atividade_bp.route("/atividade/<int:id_atividade>", methods=["PUT"])
def atualizar_atividade(id_atividade):
    dados = request.get_json() or {}
    try:
        atividade_atualizada = atividade_service.atualizar_atividade(id_atividade, dados)
        return atividade_atualizada, 200
    except ValueError as e:
        return {"erro": str(e)}, 404

# DELETE /atividade/1
@atividade_bp.route("/atividade/<int:id_atividade>", methods=["DELETE"])
def remover_atividade(id_atividade):
    try:
        atividade_removida = atividade_service.deletar_atividade(id_atividade)
        return atividade_removida, 200
    except ValueError as e:
        return {"erro": str(e)}, 404