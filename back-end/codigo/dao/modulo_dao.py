from sqlalchemy import text
from services.db_service import db

class ModuloDAO:

    @staticmethod
    def criar_tabela_modulo():
        sql = text("""
            CREATE TABLE IF NOT EXISTS modulos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT
            );
        """)
        db.session.execute(sql)
        db.session.commit()
        ModuloDAO.popular_tabela()

    @staticmethod
    def popular_tabela():
        sql = text("""
            INSERT OR IGNORE INTO modulos (id, titulo, descricao)
            VALUES (:id, :titulo, :descricao);
        """)
        modulos_lote = [
            {"id": 1, "titulo": "Módulo 1: SELECT", "descricao": "Conceitos de banco de dados, tabelas, colunas e registros; consulta de dados; ORDER BY."},
            {"id": 2, "titulo": "Módulo 2: WHERE", "descricao": "Filtros e operadores de comparação e lógicos; LIKE, IN, BETWEEN; valores nulos."},
            {"id": 3, "titulo": "Módulo 3: JOIN", "descricao": "Chaves primárias e estrangeiras; INNER JOIN e LEFT JOIN."},
            {"id": 4, "titulo": "Módulo 4: GROUP BY", "descricao": "Funções de agregação (COUNT, SUM, AVG, MIN, MAX); GROUP BY e HAVING."},
            {"id": 5, "titulo": "Módulo 5: Subconsultas", "descricao": "Subconsultas em WHERE e em FROM; uso com IN e operadores de comparação."},
            {"id": 6, "titulo": "Módulo 6: Manipulação de dados", "descricao": "INSERT, UPDATE e DELETE."}
        ]
        db.session.execute(sql, modulos_lote)
        db.session.commit()

    @staticmethod
    def create(titulo, descricao, id_modulo=None):
        if id_modulo and ModuloDAO.retrieve_by_id(id_modulo):
            return None

        if id_modulo:
            sql = text("INSERT INTO modulos (id, titulo, descricao) VALUES (:id, :titulo, :descricao);")
            params = {"id": id_modulo, "titulo": titulo, "descricao": descricao}
        else:
            sql = text("INSERT INTO modulos (titulo, descricao) VALUES (:titulo, :descricao);")
            params = {"titulo": titulo, "descricao": descricao}

        res = db.session.execute(sql, params)
        db.session.commit()
        novo_id = id_modulo or res.lastrowid
        return ModuloDAO.retrieve_by_id(novo_id)

    @staticmethod
    def retrieve_by_id(id_modulo):
        sql = text("SELECT id, titulo, descricao FROM modulos WHERE id = :id;")
        res = db.session.execute(sql, {"id": id_modulo}).fetchone()
        return dict(res._mapping) if res else None

    @staticmethod
    def retrieve_all():
        sql = text("SELECT id, titulo, descricao FROM modulos;")
        res = db.session.execute(sql).fetchall()
        return [dict(r._mapping) for r in res]

    @staticmethod
    def delete(id_modulo):
        modulo = ModuloDAO.retrieve_by_id(id_modulo)
        if not modulo:
            return None
        sql = text("DELETE FROM modulos WHERE id = :id;")
        db.session.execute(sql, {"id": id_modulo})
        db.session.commit()
        return modulo

    @staticmethod
    def size():
        sql = text("SELECT COUNT(*) FROM modulos;")
        return db.session.execute(sql).scalar()