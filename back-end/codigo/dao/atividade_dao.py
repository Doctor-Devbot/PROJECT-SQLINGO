import json
from sqlalchemy import text
from services.db_service import db

class AtividadeDAO:

    @staticmethod
    def criar_tabela_atividade():
        sql = text("""
            CREATE TABLE IF NOT EXISTS atividades (
                id INTEGER PRIMARY KEY,
                enunciado TEXT NOT NULL,
                alternativas TEXT NOT NULL
            );
        """)
        db.session.execute(sql)
        db.session.commit()
        AtividadeDAO.popular_tabela()

    @staticmethod
    def popular_tabela():
        sql = text("""
            INSERT OR IGNORE INTO atividades (id, enunciado, alternativas)
            VALUES (:id, :enunciado, :alternativas);
        """)
        
        atividades_lote = [
            {
                "id": 1, 
                "enunciado": "Qual comando SQL seleciona dados?", 
                "alternativas": json.dumps(["SELECT", "INSERT", "DELETE", "UPDATE"])
            },
            {
                "id": 2, 
                "enunciado": "Qual cláusula filtra registros?", 
                "alternativas": json.dumps(["WHERE", "ORDER BY", "GROUP BY", "JOIN"])
            }
        ]
        db.session.execute(sql, atividades_lote)
        db.session.commit()

    @staticmethod
    def create(id_atividade, enunciado, alternativas):
        if AtividadeDAO.retrieve_by_id(id_atividade):
            return None

        sql = text("""
            INSERT INTO atividades (id, enunciado, alternativas)
            VALUES (:id, :enunciado, :alternativas);
        """)
        db.session.execute(sql, {
            "id": id_atividade,
            "enunciado": enunciado,
            "alternativas": json.dumps(alternativas)
        })
        db.session.commit()

        return AtividadeDAO.retrieve_by_id(id_atividade)

    @staticmethod
    def retrieve_by_id(id_atividade):
        sql = text("SELECT id, enunciado, alternativas FROM atividades WHERE id = :id;")
        res = db.session.execute(sql, {"id": id_atividade}).fetchone()
        
        if res:
            data = dict(res._mapping)
            data["alternativas"] = json.loads(data["alternativas"]) # Converte texto de volta para lista
            return data
        return None

    @staticmethod
    def retrieve_all():
        sql = text("SELECT id, enunciado, alternativas FROM atividades;")
        res = db.session.execute(sql).fetchall()
        
        atividades = []
        for r in res:
            data = dict(r._mapping)
            data["alternativas"] = json.loads(data["alternativas"])
            atividades.append(data)
            
        return atividades

    @staticmethod
    def update_enunciado(id_atividade, enunciado):
        atividade = AtividadeDAO.retrieve_by_id(id_atividade)
        if not atividade:
            return None

        sql = text("UPDATE atividades SET enunciado = :enunciado WHERE id = :id;")
        db.session.execute(sql, {"enunciado": enunciado, "id": id_atividade})
        db.session.commit()

        return AtividadeDAO.retrieve_by_id(id_atividade)

    @staticmethod
    def delete(id_atividade):
        atividade = AtividadeDAO.retrieve_by_id(id_atividade)
        if not atividade:
            return None

        sql = text("DELETE FROM atividades WHERE id = :id;")
        db.session.execute(sql, {"id": id_atividade})
        db.session.commit()

        return atividade

    @staticmethod
    def size():
        sql = text("SELECT COUNT(*) FROM atividades;")
        res = db.session.execute(sql).scalar()
        return res