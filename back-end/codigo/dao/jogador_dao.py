from sqlalchemy import text
from services.db_service import db

class JogadorDAO:

    @staticmethod
    def criar_tabela_jogador():
        sql = text("""
            CREATE TABLE IF NOT EXISTS jogadores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """)
        db.session.execute(sql)
        db.session.commit()
        JogadorDAO.popular_tabela()

    @staticmethod
    def popular_tabela():
        sql = text("""
            INSERT OR IGNORE INTO jogadores (nome, email)
            VALUES (:nome, :email);
        """)
        jogadores_lote = [
            {"nome": "Marco", "email": "marco@gmail.com"},
            {"nome": "Julia", "email": "julia@gmail.com"}
        ]
        db.session.execute(sql, jogadores_lote)
        db.session.commit()

    @staticmethod
    def create(nome, email):
        if JogadorDAO.retrieve_by_email(email):
            return None

        sql = text("""
            INSERT INTO jogadores (nome, email)
            VALUES (:nome, :email);
        """)
        db.session.execute(sql, {"nome": nome, "email": email})
        db.session.commit()

        return JogadorDAO.retrieve_by_email(email)

    @staticmethod
    def retrieve_by_email(email):
        sql = text("SELECT id, nome, email FROM jogadores WHERE email = :email;")
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