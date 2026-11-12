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
            # ==========================================
            # MÓDULO 1 - SELECT
            # ==========================================

            # Lista 1 - SELECT: Consultas Básicas
            {
                "id": 1,
                "enunciado": "Uma loja virtual deseja consultar todos os produtos cadastrados em seu estoque. Qual comando deve ser utilizado?",
                "alternativas": json.dumps(["SELECT * FROM produtos", "INSERT INTO produtos", "DELETE FROM produtos", "UPDATE produtos"]),
                "lista_atividade_id": 1
            },
            {
                "id": 2,
                "enunciado": "Uma biblioteca precisa consultar apenas os títulos e autores dos livros disponíveis em seu acervo. Qual consulta atende a essa necessidade?",
                "alternativas": json.dumps(["SELECT titulo, autor FROM livros", "SELECT * FROM titulo, autor", "SELECT titulo AND autor FROM livros", "GET titulo, autor FROM livros"]),
                "lista_atividade_id": 1
            },
            {
                "id": 3,
                "enunciado": "Uma escola deseja consultar os nomes e as notas dos alunos cadastrados no sistema. Qual comando realiza essa consulta?",
                "alternativas": json.dumps(["SELECT nome, nota FROM alunos", "SELECT nome, nota INTO alunos", "SHOW nome, nota FROM alunos", "SELECT alunos WHERE nome, nota"]),
                "lista_atividade_id": 1
            },

            # Lista 2 - SELECT: Ordenação com ORDER BY
            {
                "id": 4,
                "enunciado": "Uma loja virtual deseja exibir seus produtos organizados do menor para o maior preço. Qual consulta deve utilizar?",
                "alternativas": json.dumps(["SELECT * FROM produtos ORDER BY preco ASC", "SELECT * FROM produtos ORDER BY preco DESC", "SELECT * FROM produtos WHERE preco ASC", "SELECT * FROM produtos GROUP BY preco"]),
                "lista_atividade_id": 2
            },
            {
                "id": 5,
                "enunciado": "Uma biblioteca deseja organizar seu catálogo em ordem alfabética pelo título dos livros. Qual comando realiza essa ordenação?",
                "alternativas": json.dumps(["SELECT * FROM livros ORDER BY titulo ASC", "SELECT * FROM livros ORDER BY titulo DESC", "SELECT * FROM livros WHERE titulo ASC", "SELECT * FROM livros GROUP BY titulo"]),
                "lista_atividade_id": 2
            },
            {
                "id": 6,
                "enunciado": "Uma escola deseja apresentar os alunos organizados da maior para a menor nota em uma avaliação. Qual consulta deve ser utilizada?",
                "alternativas": json.dumps(["SELECT * FROM alunos ORDER BY nota DESC", "SELECT * FROM alunos ORDER BY nota ASC", "SELECT * FROM alunos WHERE nota DESC", "SELECT * FROM alunos GROUP BY nota"]),
                "lista_atividade_id": 2
            },

            # ==========================================
            # MÓDULO 2 - WHERE
            # ==========================================

            # Lista 3 - WHERE: Operadores de Comparação
            {
                "id": 7,
                "enunciado": "Uma loja virtual deseja encontrar todos os produtos que custam mais de R$ 100. Qual consulta deve ser utilizada?",
                "alternativas": json.dumps(["SELECT * FROM produtos WHERE preco > 100", "SELECT * FROM produtos WHERE preco < 100", "SELECT * FROM produtos ORDER BY preco", "SELECT * FROM produtos WHERE preco = 100"]),
                "lista_atividade_id": 3
            },
            {
                "id": 8,
                "enunciado": "Uma biblioteca precisa localizar os empréstimos que ainda estão com status 'Ativo'. Qual operador deve ser utilizado para comparar o status com esse valor?",
                "alternativas": json.dumps(["=", ">", "<", ">="]),
                "lista_atividade_id": 3
            },
            {
                "id": 9,
                "enunciado": "Uma escola deseja localizar os alunos que possuem nota maior ou igual a 7. Qual consulta atende a essa necessidade?",
                "alternativas": json.dumps(["SELECT * FROM alunos WHERE nota >= 7", "SELECT * FROM alunos WHERE nota < 7", "SELECT * FROM alunos WHERE nota = 7", "SELECT * FROM alunos ORDER BY nota"]),
                "lista_atividade_id": 3
            },

            # Lista 4 - WHERE: Filtros Avançados
            {
                "id": 10,
                "enunciado": "Uma loja virtual deseja encontrar todos os clientes cujos nomes começam com a letra 'A'. Qual condição permite realizar essa busca?",
                "alternativas": json.dumps(["WHERE nome LIKE 'A%'", "WHERE nome IN 'A%'", "WHERE nome BETWEEN 'A' AND 'Z'", "WHERE nome = '%A'"]),
                "lista_atividade_id": 4
            },
            {
                "id": 11,
                "enunciado": "Uma biblioteca deseja localizar os livros publicados entre os anos de 2010 e 2020, incluindo esses dois anos. Qual condição deve utilizar?",
                "alternativas": json.dumps(["WHERE ano_publicacao BETWEEN 2010 AND 2020", "WHERE ano_publicacao IN (2010, 2020)", "WHERE ano_publicacao LIKE '2010-2020'", "WHERE ano_publicacao > 2020"]),
                "lista_atividade_id": 4
            },
            {
                "id": 12,
                "enunciado": "Uma escola deseja consultar as matrículas dos alunos que pertencem às turmas 1, 2 ou 3. Qual consulta atende a essa necessidade?",
                "alternativas": json.dumps(["SELECT * FROM matriculas WHERE turma IN (1, 2, 3)", "SELECT * FROM matriculas WHERE turma LIKE (1, 2, 3)", "SELECT * FROM matriculas WHERE turma BETWEEN 1 AND 3", "SELECT * FROM matriculas WHERE turma = IN (1, 2, 3)"]),
                "lista_atividade_id": 4
            },

            # ==========================================
            # MÓDULO 3 - JOIN
            # ==========================================

            # Lista 5 - JOIN: INNER JOIN
            {
                "id": 13,
                "enunciado": "Uma loja virtual armazena clientes e pedidos em tabelas diferentes. Para consultar os pedidos junto aos nomes dos clientes que os realizaram, qual recurso SQL deve ser utilizado?",
                "alternativas": json.dumps(["INNER JOIN", "ORDER BY", "GROUP BY", "DELETE"]),
                "lista_atividade_id": 5
            },
            {
                "id": 14,
                "enunciado": "Uma biblioteca possui uma tabela de livros e outra de empréstimos. A coluna id da tabela livros identifica cada livro de forma única. Como essa coluna é classificada?",
                "alternativas": json.dumps(["Chave primária (PRIMARY KEY)", "Chave estrangeira (FOREIGN KEY)", "Chave duplicada", "Chave temporária"]),
                "lista_atividade_id": 5
            },
            {
                "id": 15,
                "enunciado": "Uma escola deseja consultar os nomes dos alunos junto aos nomes das disciplinas em que estão matriculados. Considerando alunos.id e matriculas.aluno_id como campos relacionados, qual consulta realiza essa operação?",
                "alternativas": json.dumps(["SELECT * FROM alunos INNER JOIN matriculas ON alunos.id = matriculas.aluno_id", "SELECT * FROM alunos WHERE matriculas.aluno_id = alunos.id", "SELECT * FROM alunos ORDER BY matriculas.aluno_id", "SELECT * FROM alunos GROUP BY matriculas.aluno_id"]),
                "lista_atividade_id": 5
            },

            # Lista 6 - JOIN: LEFT JOIN
            {
                "id": 16,
                "enunciado": "Uma loja virtual deseja consultar todos os clientes cadastrados, inclusive aqueles que nunca realizaram pedidos. Qual tipo de JOIN deve ser utilizado?",
                "alternativas": json.dumps(["LEFT JOIN", "INNER JOIN", "CROSS JOIN", "RIGHT JOIN"]),
                "lista_atividade_id": 6
            },
            {
                "id": 17,
                "enunciado": "Uma biblioteca utiliza LEFT JOIN para consultar leitores e seus empréstimos. Quando um leitor ainda não realizou nenhum empréstimo, o que será apresentado nas colunas referentes aos empréstimos?",
                "alternativas": json.dumps(["Valores NULL", "Os dados do primeiro empréstimo", "Uma mensagem de erro obrigatoriamente", "Os dados de outro leitor"]),
                "lista_atividade_id": 6
            },
            {
                "id": 18,
                "enunciado": "Uma escola deseja listar todos os alunos e suas respectivas matrículas, mesmo que alguns ainda não estejam matriculados em nenhuma disciplina. Considerando alunos.id e matriculas.aluno_id como campos relacionados, qual consulta deve ser utilizada?",
                "alternativas": json.dumps(["SELECT * FROM alunos LEFT JOIN matriculas ON alunos.id = matriculas.aluno_id", "SELECT * FROM alunos INNER JOIN matriculas ON alunos.id = matriculas.aluno_id", "SELECT * FROM matriculas INNER JOIN alunos ON alunos.id = matriculas.aluno_id", "SELECT * FROM alunos WHERE matriculas.aluno_id IS NOT NULL"]),
                "lista_atividade_id": 6
            },

            # ==========================================
            # MÓDULO 4 - GROUP BY
            # ==========================================

            # Lista 7 - GROUP BY: Funções de Agregação
            {
                "id": 19,
                "enunciado": "Uma loja virtual deseja descobrir quantos pedidos foram registrados durante o mês. Qual função SQL permite contar os registros?",
                "alternativas": json.dumps(["COUNT()", "SUM()", "AVG()", "MAX()"]),
                "lista_atividade_id": 7
            },
            {
                "id": 20,
                "enunciado": "Uma biblioteca deseja calcular a média de dias que os leitores permanecem com os livros emprestados. Qual função de agregação deve ser utilizada?",
                "alternativas": json.dumps(["AVG()", "SUM()", "MIN()", "COUNT()"]),
                "lista_atividade_id": 7
            },
            {
                "id": 21,
                "enunciado": "Uma escola deseja calcular a soma de todas as notas registradas em uma determinada avaliação. Considerando a existência da coluna nota na tabela avaliacoes, qual consulta realiza essa operação?",
                "alternativas": json.dumps(["SELECT SUM(nota) FROM avaliacoes", "SELECT COUNT(nota) FROM avaliacoes", "SELECT AVG(nota) FROM avaliacoes", "SELECT MAX(nota) FROM avaliacoes"]),
                "lista_atividade_id": 7
            },

            # Lista 8 - GROUP BY: Filtrando Grupos com HAVING
            {
                "id": 22,
                "enunciado": "Uma loja virtual deseja descobrir a quantidade de pedidos realizados por cada cliente. Qual cláusula permite agrupar os pedidos pelo identificador do cliente?",
                "alternativas": json.dumps(["GROUP BY cliente_id", "ORDER BY cliente_id", "WHERE cliente_id", "HAVING cliente_id"]),
                "lista_atividade_id": 8
            },
            {
                "id": 23,
                "enunciado": "Uma biblioteca deseja listar apenas os leitores que realizaram mais de 3 empréstimos. Qual cláusula deve ser utilizada para filtrar os grupos após a contagem dos empréstimos?",
                "alternativas": json.dumps(["HAVING", "WHERE", "ORDER BY", "INSERT"]),
                "lista_atividade_id": 8
            },
            {
                "id": 24,
                "enunciado": "Uma escola deseja identificar as disciplinas que possuem mais de 20 alunos matriculados. Considerando a coluna disciplina_id na tabela matriculas, qual consulta atende a essa necessidade?",
                "alternativas": json.dumps(["SELECT disciplina_id, COUNT(*) FROM matriculas GROUP BY disciplina_id HAVING COUNT(*) > 20", "SELECT disciplina_id, COUNT(*) FROM matriculas WHERE COUNT(*) > 20", "SELECT disciplina_id FROM matriculas ORDER BY COUNT(*) > 20", "SELECT disciplina_id, COUNT(*) FROM matriculas GROUP BY disciplina_id WHERE COUNT(*) > 20"]),
                "lista_atividade_id": 8
            },

            # ==========================================
            # MÓDULO 5 - SUBCONSULTAS
            # ==========================================

            # Lista 9 - Subconsultas: Uso no WHERE
            {
                "id": 25,
                "enunciado": "Uma loja virtual deseja encontrar os produtos que custam mais do que a média de preços de todos os produtos cadastrados. Qual consulta realiza essa operação utilizando uma subconsulta?",
                "alternativas": json.dumps(["SELECT * FROM produtos WHERE preco > (SELECT AVG(preco) FROM produtos)", "SELECT * FROM produtos WHERE preco = AVG(preco)", "SELECT * FROM produtos ORDER BY AVG(preco)", "SELECT AVG(preco) FROM produtos WHERE preco > produtos"]),
                "lista_atividade_id": 9
            },
            {
                "id": 26,
                "enunciado": "Uma biblioteca deseja localizar os livros que pertencem às categorias cadastradas na tabela categorias. Qual operador permite verificar se o código da categoria está presente no resultado de uma subconsulta?",
                "alternativas": json.dumps(["IN", "LIKE", "ORDER BY", "BETWEEN"]),
                "lista_atividade_id": 9
            },
            {
                "id": 27,
                "enunciado": "Uma escola deseja consultar os alunos que possuem nota superior à nota média da turma. Considerando que a tabela alunos possui as colunas nome, turma e nota, qual consulta pode realizar essa busca?",
                "alternativas": json.dumps(["SELECT * FROM alunos WHERE nota > (SELECT AVG(nota) FROM alunos)", "SELECT * FROM alunos WHERE nota = AVG(nota)", "SELECT * FROM alunos GROUP BY nota > AVG(nota)", "SELECT AVG(nota) FROM alunos WHERE nota > alunos"]),
                "lista_atividade_id": 9
            },

            # Lista 10 - Subconsultas: Uso no FROM
            {
                "id": 28,
                "enunciado": "Uma loja virtual deseja calcular a média de vendas de cada categoria e depois consultar esses resultados como se fossem uma tabela. Qual é a função de uma subconsulta utilizada no FROM?",
                "alternativas": json.dumps(["Permitir utilizar o resultado de outra consulta como uma tabela temporária", "Excluir automaticamente os registros consultados", "Ordenar os dados sem utilizar ORDER BY", "Substituir todas as tabelas do banco de dados"]),
                "lista_atividade_id": 10
            },
            {
                "id": 29,
                "enunciado": "Uma biblioteca utiliza uma subconsulta no FROM para calcular a quantidade de empréstimos por leitor. Por que é necessário atribuir um alias à subconsulta?",
                "alternativas": json.dumps(["Para identificar e referenciar o resultado da subconsulta", "Para excluir os empréstimos encontrados", "Para impedir a consulta de acessar outras tabelas", "Para transformar os resultados em chaves primárias"]),
                "lista_atividade_id": 10
            },
            {
                "id": 30,
                "enunciado": "Uma escola deseja consultar a média geral das notas utilizando uma subconsulta no FROM. Considerando que as notas estão na tabela alunos, qual consulta está escrita corretamente?",
                "alternativas": json.dumps(["SELECT resultado.media FROM (SELECT AVG(nota) AS media FROM alunos) AS resultado", "SELECT * FROM (SELECT AVG(nota) FROM alunos)", "SELECT FROM (SELECT * FROM alunos)", "SELECT * FROM alunos AS (SELECT AVG(nota))"]),
                "lista_atividade_id": 10
            },

            # ==========================================
            # MÓDULO 6 - MANIPULAÇÃO DE DADOS
            # ==========================================

            # Lista 11 - CRUD: INSERT e UPDATE
            {
                "id": 31,
                "enunciado": "Uma loja virtual acabou de cadastrar um novo produto e precisa adicioná-lo ao banco de dados. Qual comando SQL deve ser utilizado para inserir esse registro?",
                "alternativas": json.dumps(["INSERT INTO", "UPDATE", "DELETE", "SELECT"]),
                "lista_atividade_id": 11
            },
            {
                "id": 32,
                "enunciado": "Uma biblioteca recebeu um novo livro chamado 'Dom Casmurro', escrito por Machado de Assis. Considerando as colunas titulo e autor na tabela livros, qual comando realiza o cadastro desse livro?",
                "alternativas": json.dumps(["INSERT INTO livros (titulo, autor) VALUES ('Dom Casmurro', 'Machado de Assis')", "UPDATE livros SET titulo = 'Dom Casmurro', autor = 'Machado de Assis'", "SELECT * FROM livros WHERE titulo = 'Dom Casmurro'", "DELETE FROM livros WHERE titulo = 'Dom Casmurro'"]),
                "lista_atividade_id": 11
            },
            {
                "id": 33,
                "enunciado": "Uma escola identificou que a nota de um aluno foi registrada incorretamente. Para corrigir a nota do aluno cujo id é 5, qual comando deve ser utilizado?",
                "alternativas": json.dumps(["UPDATE alunos SET nota = 9 WHERE id = 5", "INSERT INTO alunos (nota) VALUES (9)", "SELECT * FROM alunos WHERE id = 5", "DELETE FROM alunos WHERE id = 5"]),
                "lista_atividade_id": 11
            },

            # Lista 12 - CRUD: Exclusão de Registros (DELETE)
            {
                "id": 34,
                "enunciado": "Uma loja virtual decidiu remover do catálogo um produto descontinuado, identificado pelo código 15. Qual comando permite excluir esse registro da tabela produtos?",
                "alternativas": json.dumps(["DELETE FROM produtos WHERE id = 15", "INSERT INTO produtos WHERE id = 15", "UPDATE produtos SET id = NULL WHERE id = 15", "SELECT * FROM produtos WHERE id = 15"]),
                "lista_atividade_id": 12
            },
            {
                "id": 35,
                "enunciado": "Uma biblioteca precisa excluir do sistema um empréstimo cancelado, identificado pelo número 42. Qual consulta realiza essa operação sem excluir os outros empréstimos?",
                "alternativas": json.dumps(["DELETE FROM emprestimos WHERE id = 42", "DELETE FROM emprestimos", "DROP TABLE emprestimos", "UPDATE emprestimos SET id = NULL"]),
                "lista_atividade_id": 12
            },
            {
                "id": 36,
                "enunciado": "Uma escola deseja remover todos os registros de matrículas de uma turma específica, identificada pelo código 3. Qual comando deve ser utilizado?",
                "alternativas": json.dumps(["DELETE FROM matriculas WHERE turma_id = 3", "DELETE FROM matriculas", "DROP TABLE matriculas", "UPDATE matriculas SET turma_id = NULL"]),
                "lista_atividade_id": 12
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