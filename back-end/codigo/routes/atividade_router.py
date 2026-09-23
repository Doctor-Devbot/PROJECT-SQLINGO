from flask import Blueprint, request
from dao.atividade_dao import AtividadeDAO

atividade_bp = Blueprint('atividade', __name__)

# POST /atividade
@atividade_bp.route("/atividade", methods=["POST"])
def cadastrar_atividade():
    nova_atividade = request.get_json()
    atividade_criada = AtividadeDAO.create(nova_atividade["id_atividade"], nova_atividade["enunciado"], nova_atividade.get("alternativas", []))
    if atividade_criada is None:
        return {"erro": "ID de atividade já cadastrado"}, 400
    return atividade_criada, 201

# GET /atividade
@atividade_bp.route("/atividade", methods=["GET"])
def todas_atividades():
    if AtividadeDAO.size() == 0:
        return {"erro": "Nenhuma atividade cadastrada"}, 404
    return AtividadeDAO.retrieve_all(), 200

# GET /atividade/1
@atividade_bp.route("/atividade/<int:id_atividade>", methods=["GET"])
def buscar_atividade(id_atividade):
    atividade_encontrada = AtividadeDAO.retrieve_by_id(id_atividade)
    if atividade_encontrada is None:
        return {"erro": "Atividade não encontrada"}, 404
    return atividade_encontrada, 200

# DELETE /atividade/1
@atividade_bp.route("/atividade/<int:id_atividade>", methods=["DELETE"])
def remover_atividade(id_atividade):
    atividade = AtividadeDAO.delete(id_atividade)
    if atividade is None:
        return {"erro": "Atividade não encontrada"}, 404
    return atividade, 200

# PUT /atividade/1
@atividade_bp.route("/atividade/<int:id_atividade>", methods=["PUT"])
def atualizar_enunciado(id_atividade):
    dados = request.get_json()
    atividade_atualizada = AtividadeDAO.update_enunciado(id_atividade, dados["enunciado"])
    if atividade_atualizada is None:
        return {"erro": "Atividade não encontrada"}, 404
    return atividade_atualizada, 200