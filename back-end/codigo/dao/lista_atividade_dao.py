from sqlalchemy import text
from services.db_service import db

class ListaAtividadeDAO:

    @staticmethod
    def criar_tabela_lista_atividade():
        sql = text("""
            CREATE TABLE IF NOT EXISTS listas_atividade (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                modulo_id INTEGER,
                FOREIGN KEY (modulo_id) REFERENCES modulos(id)
            );
        """)
        db.session.execute(sql)
        db.session.commit()
        ListaAtividadeDAO.popular_tabela()

    @staticmethod
    def popular_tabela():
        sql = text("""
            INSERT OR IGNORE INTO listas_atividade (id, titulo, descricao, modulo_id)
            VALUES (:id, :titulo, :descricao, :modulo_id);
        """)
        listas_lote = [
            # Módulo 1 (SELECT)
            {
                "id": 1, 
                "titulo": "SELECT: Consultas Básicas", 
                "descricao": "Pratique a seleção de colunas e registros em tabelas.", 
                "modulo_id": 1
            },
            {
                "id": 2, 
                "titulo": "SELECT: Ordenação com ORDER BY", 
                "descricao": "Exercícios focados em ordenar resultados de consultas de forma ascendente e descendente.", 
                "modulo_id": 1
            },

            # Módulo 2 (WHERE)
            {
                "id": 3, 
                "titulo": "WHERE: Operadores de Comparação", 
                "descricao": "Pratique filtros com operadores lógicos e de comparação.", 
                "modulo_id": 2
            },
            {
                "id": 4, 
                "titulo": "WHERE: Filtros Avançados (LIKE, IN, BETWEEN)", 
                "descricao": "Exercícios com padrões de texto, intervalos e listas de valores.", 
                "modulo_id": 2
            },

            # Módulo 3 (JOIN)
            {
                "id": 5, 
                "titulo": "JOIN: INNER JOIN", 
                "descricao": "Pratique a junção de tabelas cruzando chaves primárias e estrangeiras.", 
                "modulo_id": 3
            },
            {
                "id": 6, 
                "titulo": "JOIN: LEFT JOIN", 
                "descricao": "Exercícios focados em trazer registros mesmo sem correspondência na outra tabela.", 
                "modulo_id": 3
            },

            # Módulo 4 (GROUP BY)
            {
                "id": 7, 
                "titulo": "GROUP BY: Funções de Agregação", 
                "descricao": "Pratique o uso de COUNT, SUM, AVG, MIN e MAX.", 
                "modulo_id": 4
            },
            {
                "id": 8, 
                "titulo": "GROUP BY: Filtrando Grupos com HAVING", 
                "descricao": "Exercícios aplicando condições sobre dados agrupados.", 
                "modulo_id": 4
            },

            # Módulo 5 (Subconsultas)
            {
                "id": 9, 
                "titulo": "Subconsultas: Uso no WHERE", 
                "descricao": "Pratique consultas aninhadas combinadas com operadores de comparação e IN.", 
                "modulo_id": 5
            },
            {
                "id": 10, 
                "titulo": "Subconsultas: Uso no FROM", 
                "descricao": "Exercícios utilizando subconsultas como tabelas temporárias.", 
                "modulo_id": 5
            },

            # Módulo 6 (Manipulação de dados)
            {
                "id": 11, 
                "titulo": "CRUD: Inserção e Atualização (INSERT e UPDATE)", 
                "descricao": "Pratique adicionar novos registros e modificar dados existentes.", 
                "modulo_id": 6
            },
            {
                "id": 12, 
                "titulo": "CRUD: Exclusão de Registros (DELETE)", 
                "descricao": "Exercícios focados em remover dados com segurança de tabelas.", 
                "modulo_id": 6
            }
        ]
        db.session.execute(sql, listas_lote)
        db.session.commit()

    @staticmethod
    def create(titulo, descricao, modulo_id, id_lista=None):
        if id_lista:
            sql = text("INSERT INTO listas_atividade (id, titulo, descricao, modulo_id) VALUES (:id, :titulo, :descricao, :modulo_id);")
            params = {"id": id_lista, "titulo": titulo, "descricao": descricao, "modulo_id": modulo_id}
        else:
            sql = text("INSERT INTO listas_atividade (titulo, descricao, modulo_id) VALUES (:titulo, :descricao, :modulo_id);")
            params = {"titulo": titulo, "descricao": descricao, "modulo_id": modulo_id}

        res = db.session.execute(sql, params)
        db.session.commit()
        novo_id = id_lista or res.lastrowid
        return ListaAtividadeDAO.retrieve_by_id(novo_id)

    @staticmethod
    def retrieve_by_id(id_lista):
        sql = text("SELECT id, titulo, descricao, modulo_id FROM listas_atividade WHERE id = :id;")
        res = db.session.execute(sql, {"id": id_lista}).fetchone()
        return dict(res._mapping) if res else None

    @staticmethod
    def retrieve_all():
        sql = text("SELECT id, titulo, descricao, modulo_id FROM listas_atividade;")
        res = db.session.execute(sql).fetchall()
        return [dict(r._mapping) for r in res]

    @staticmethod
    def size():
        sql = text("SELECT COUNT(*) FROM listas_atividade;")
        return db.session.execute(sql).scalar()