from services.db_service import db
from sqlalchemy import text


class JogadorDAO:

  @staticmethod
  def criar_tabela_jogador():
    sql = text("""
            CREATE TABLE IF NOT EXISTS jogadores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL
            );
        """)
    db.session.execute(sql)
    db.session.commit()
    # Remova ou ajuste o popular_tabela caso queira inserir senhas padrão com hash

  @staticmethod
  def create(nome, email, senha_hash):
    if JogadorDAO.retrieve_by_email(email):
      return None

    sql = text("""
            INSERT INTO jogadores (nome, email, senha)
            VALUES (:nome, :email, :senha);
        """)
    db.session.execute(
        sql, {"nome": nome, "email": email, "senha": senha_hash}
    )
    db.session.commit()

    return JogadorDAO.retrieve_by_email(email)

  @staticmethod
  def retrieve_by_email(email):
    # Importante: Incluir a 'senha' na consulta para validação no login
    sql = text(
        "SELECT id, nome, email, senha FROM jogadores WHERE email = :email;"
    )
    res = db.session.execute(sql, {"email": email}).fetchone()
    return dict(res._mapping) if res else None

  @staticmethod
  def retrieve_all():
    sql = text("SELECT id, nome, email FROM jogadores;")
    res = db.session.execute(sql).fetchall()
    return [dict(r._mapping) for r in res]

  @staticmethod
  def update_nome(email, nome):
    jogador = JogadorDAO.retrieve_by_email(email)
    if not jogador:
      return None

    sql = text("UPDATE jogadores SET nome = :nome WHERE email = :email;")
    db.session.execute(sql, {"nome": nome, "email": email})
    db.session.commit()

    return JogadorDAO.retrieve_by_email(email)

  @staticmethod
  def delete(email):
    jogador = JogadorDAO.retrieve_by_email(email)
    if not jogador:
      return None

    sql = text("DELETE FROM jogadores WHERE email = :email;")
    db.session.execute(sql, {"email": email})
    db.session.commit()

    return jogador

  @staticmethod
  def size():
    sql = text("SELECT COUNT(*) FROM jogadores;")
    return db.session.execute(sql).scalar()
  @staticmethod
  def count_jogador():
    """Retorna a quantidade total de registros para o cálculo de páginas."""
    sql_count = text("SELECT COUNT(*) FROM jogadores;")
    total = db.session.execute(sql_count)
    return total.scalar()

  @staticmethod
  def list_jogador_pagina(offset, por_pagina):
    """Busca um bloco específico de registros usando LIMIT e OFFSET."""
    sql_paginacao = text("SELECT id, nome, email FROM jogadores ORDER BY id LIMIT :por_pagina OFFSET :offset;")
    resultado = db.session.execute(sql_paginacao, {"por_pagina": por_pagina, "offset": offset})
    # Converte cada linha retornada em dicionário Python
    return [dict(linha._mapping) for linha in resultado]