from flask import Blueprint, request
from services.modulo_service import ModuloService

modulo_bp = Blueprint('modulo', __name__)
modulo_service = ModuloService()

@modulo_bp.route("/modulo", methods=["GET"])
def todos_modulos():
    try:
        return modulo_service.listar_todos(), 200
    except ValueError as e:
        return {"erro": str(e)}, 404

@modulo_bp.route("/modulo/<int:id_modulo>", methods=["GET"])
def buscar_modulo(id_modulo):
    try:
        return modulo_service.obter_modulo(id_modulo), 200
    except ValueError as e:
        return {"erro": str(e)}, 404

@modulo_bp.route("/modulo", methods=["POST"])
def cadastrar_modulo():
    dados = request.get_json() or {}
    try:
        return modulo_service.cadastrar_modulo(dados), 201
    except ValueError as e:
        return {"erro": str(e)}, 400