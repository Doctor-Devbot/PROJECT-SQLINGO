from dao.jogador_dao import JogadorDAO
from flask import Blueprint, jsonify, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
from repository.jogador_repository import JogadorRepository
from services.db_service import db
from services.jogador_service import JogadorService

jogador_bp = Blueprint("jogador", __name__)
jogador_service = JogadorService()
jogador_repo = JogadorRepository()  # <--- ADICIONADO AQUI PARA EVITAR O ERRO
bcrypt = Bcrypt()  # Instância do Bcrypt para manipulação de hash nas rotas


@jogador_bp.route("/jogador/paginacao", methods=["GET"])
def get_jogadores_paginacao():
  # Validação: verifica se os parâmetros obrigatórios foram passados na URL
  if (
      not request.args
      or "pag" not in request.args
      or "por_pagina" not in request.args
  ):
    return jsonify({"erro": "Campos obrigatórios ausentes"}), 400

  try:
    pagina = int(request.args["pag"])
    por_pagina = int(request.args["por_pagina"])

    resultado = jogador_service.listar_jogadores_paginacao(pagina, por_pagina)
    return jsonify(resultado), 200
  except ValueError:
    return (
        jsonify({
            "erro": (
                "Os parâmetros 'pag' e 'por_pagina' devem ser números inteiros."
            )
        }),
        400,
    )


# Rota de Cadastro (Modificada para criptografar a senha)
@jogador_bp.route("/jogador", methods=["POST"])
def cadastrar_jogador():
  dados = request.get_json() or {}
  nome = dados.get("nome")
  email = dados.get("email")
  senha_pura = dados.get("senha")

  # Relacionamento N:N (Aula 14): lista opcional de IDs de atividades
  # resolvidas pelo jogador, enviada no JSON como "atividades_ids": [1, 3]
  atividades_ids = dados.get("atividades_ids") or []

  if not nome or not email or not senha_pura:
    return {"erro": "Nome, email e senha são obrigatórios"}, 400

  if JogadorDAO.retrieve_by_email(email):
    return {"erro": "Email já cadastrado"}, 400

  if not isinstance(atividades_ids, list) or not all(
      isinstance(id_ativ, int) and not isinstance(id_ativ, bool)
      for id_ativ in atividades_ids
  ):
    return {"erro": "O campo 'atividades_ids' deve ser uma lista de inteiros"}, 400

  try:
    # Criptografa a senha antes de salvar no banco
    senha_hash = bcrypt.generate_password_hash(senha_pura).decode("utf-8")

    # O Repository orquestra a gravação relacional completa:
    # jogador (tabela principal) + vínculos N:N (jogador_atividade)
    jogador_criado = jogador_repo.salvar(nome, email, senha_hash, atividades_ids)
    if jogador_criado:
      jogador_criado.pop(
          "senha", None
      )  # Remove a senha do retorno JSON por segurança
    return jogador_criado, 201
  except ValueError as e:
    return {"erro": str(e)}, 400
  except Exception as e:
    # Aula 14: falha em qualquer etapa da gravação relacional -> rollback
    db.session.rollback()
    return {"erro": f"Falha ao salvar dados: {str(e)}"}, 500


# Nova Rota de Login (Gera o Token JWT)
@jogador_bp.route("/login", methods=["POST"])
def login():
  dados = request.get_json() or {}
  email = dados.get("email")
  senha_pura = dados.get("senha")

  if not email or not senha_pura:
    return {"erro": "Email e senha são obrigatórios"}, 400

  jogador = JogadorDAO.retrieve_by_email(email)

  # Verifica se o usuário existe e se a senha confere com o hash salvo
  if jogador and bcrypt.check_password_hash(jogador["senha"], senha_pura):
    # Cria o token JWT utilizando o email como identidade
    access_token = create_access_token(identity=jogador["email"])
    return (
        jsonify({
            "message": "Login realizado com sucesso",
            "access_token": access_token,
        }),
        200,
    )

  return {"erro": "Email ou senha inválidos"}, 401


# Exemplo de Endpoint Protegido com JWT
@jogador_bp.route("/perfil/protegido", methods=["GET"])
@jwt_required()  # Exige o envio do cabeçalho: Authorization: Bearer <access_token>
def perfil_protegido():
  email_autenticado = get_jwt_identity()  # Recupera o email armazenado no token
  jogador = JogadorDAO.retrieve_by_email(email_autenticado)

  if not jogador:
    return {"erro": "Usuário não encontrado"}, 404

  jogador.pop("senha", None)
  return (
      jsonify(
          {"message": "Acesso autorizado ao conteúdo protegido!", "usuario": jogador}
      ),
      200,
  )


# Realizando o Logout
@jogador_bp.route("/logout", methods=["POST"])  # Recomendado usar POST para logout
def logout():
  return (
      jsonify(
          {
              "message": "Você saiu do sistema!",
              "access_token": (
                  ""
              ),  # Retorna um token vazio para o cliente limpar a sessão
          }
      ),
      200,
  )


@jogador_bp.route("/jogador", methods=["GET"])
def todos_jogadores():
  # JSON aninhado: cada jogador vem com a lista "atividades_ids" (N:N)
  try:
    jogadores = jogador_repo.buscar_todos()
    return jogadores, 200
  except Exception as e:
    return {"erro": f"Falha ao buscar dados: {str(e)}"}, 500


@jogador_bp.route("/jogador/<string:email>", methods=["GET"])
def buscar_jogador(email):
  jogador = jogador_repo.buscar_por_email(email)
  if not jogador:
    return {"erro": "Jogador não encontrado"}, 404
  jogador.pop("senha", None)
  return jogador, 200


# 5. CRUD COMPLETO: PUT (Atualizar Nome por Email)
@jogador_bp.route("/jogador/<string:email>", methods=["PUT"])
@jwt_required()  # Exige token JWT válido para atualizar
def atualizar_jogador(email):
  dados = request.get_json() or {}
  novo_nome = dados.get("nome")
  if not novo_nome:
    return jsonify({"erro": "Nome é obrigatório"}), 400

  atualizado = jogador_repo.atualizar_nome(email, novo_nome)
  if not atualizado:
    return jsonify({"erro": "Jogador não encontrado"}), 404

  atualizado.pop("senha", None)
  return jsonify(atualizado), 200


# DELETE /jogador/email@gmail.com
@jogador_bp.route("/jogador/<string:email>", methods=["DELETE"])
@jwt_required()
def remover_jogador(email):
  try:
    jogador_removido = jogador_service.deletar_jogador(email)
    return jogador_removido, 200
  except ValueError as e:
    return {"erro": str(e)}, 404