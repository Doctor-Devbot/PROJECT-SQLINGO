import json
from sqlalchemy import text
from services.db_service import db

class AtividadeDAO:

    @staticmethod
    def criar_tabela_atividade():
        sql = text("""
            CREATE TABLE IF NOT EXISTS atividades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                enunciado TEXT NOT NULL,
                alternativas TEXT NOT NULL,
                lista_atividade_id INTEGER,
                FOREIGN KEY (lista_atividade_id) REFERENCES listas_atividade(id)
            );
        """)
        db.session.execute(sql)
        db.session.commit()
        AtividadeDAO.popular_tabela()

    @staticmethod
    def popular_tabela():
        sql = text("""
            INSERT OR IGNORE INTO atividades (id, enunciado, alternativas, lista_atividade_id)
            VALUES (:id, :enunciado, :alternativas, :lista_atividade_id);
        """)
        
        # Distribuindo as atividades de exemplo para as listas correspondentes (ex: Lista 1 e Lista 2)
        atividades_lote = [
            {
                "id": 1, 
                "enunciado": "Qual comando SQL seleciona dados?", 
                "alternativas": json.dumps(["SELECT", "INSERT", "DELETE", "UPDATE"]),
                "lista_atividade_id": 1  # Pertence à Lista 1
            },
            {
                "id": 2, 
                "enunciado": "Qual cláusula filtra registros?", 
                "alternativas": json.dumps(["WHERE", "ORDER BY", "GROUP BY", "JOIN"]),
                "lista_atividade_id": 1  # Pertence à Lista 1 também, ou à Lista 2
            }
        ]
        db.session.execute(sql, atividades_lote)
        db.session.commit()

    @staticmethod
    def retrieve_by_lista_id(lista_id):
        # Novo método para buscar apenas as atividades de uma lista específica!
        sql = text("SELECT id, enunciado, alternativas, lista_atividade_id FROM atividades WHERE lista_atividade_id = :lista_id;")
        res = db.session.execute(sql, {"lista_id": lista_id}).fetchall()
        
        atividades = []
        for r in res:
            data = dict(r._mapping)
            data["alternativas"] = json.loads(data["alternativas"])
            atividades.append(data)
        return atividades

    @staticmethod
    def create(enunciado, alternativas, id_atividade=None):
        if id_atividade and AtividadeDAO.retrieve_by_id(id_atividade):
            return None

        if id_atividade:
            sql = text("""
                INSERT INTO atividades (id, enunciado, alternativas)
                VALUES (:id, :enunciado, :alternativas);
            """)
            params = {
                "id": id_atividade,
                "enunciado": enunciado,
                "alternativas": json.dumps(alternativas)
            }
        else:
            sql = text("""
                INSERT INTO atividades (enunciado, alternativas)
                VALUES (:enunciado, :alternativas);
            """)
            params = {
                "enunciado": enunciado,
                "alternativas": json.dumps(alternativas)
            }

        res = db.session.execute(sql, params)
        db.session.commit()

        novo_id = id_atividade or res.lastrowid
        return AtividadeDAO.retrieve_by_id(novo_id)

    @staticmethod
    def retrieve_by_id(id_atividade):
        sql = text("SELECT id, enunciado, alternativas FROM atividades WHERE id = :id;")
        res = db.session.execute(sql, {"id": id_atividade}).fetchone()
        
        if res:
            data = dict(res._mapping)
            data["alternativas"] = json.loads(data["alternativas"])
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
    def update(id_atividade, enunciado=None, alternativas=None):
        atividade = AtividadeDAO.retrieve_by_id(id_atividade)
        if not atividade:
            return None

        novo_enunciado = enunciado if enunciado is not None else atividade["enunciado"]
        novas_alternativas = json.dumps(alternativas) if alternativas is not None else json.dumps(atividade["alternativas"])

        sql = text("""
            UPDATE atividades 
            SET enunciado = :enunciado, alternativas = :alternativas 
            WHERE id = :id;
        """)
        db.session.execute(sql, {
            "enunciado": novo_enunciado,
            "alternativas": novas_alternativas,
            "id": id_atividade
        })
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
        return db.session.execute(sql).scalar()