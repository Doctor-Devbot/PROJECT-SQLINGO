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
                "enunciado": "Uma loja virtual deseja consultar os nomes e os preços de todos os produtos cadastrados em seu catálogo. Qual comando SQL permite realizar essa consulta?",
                "alternativas": json.dumps(["SELECT nome, preco FROM produtos", "INSERT INTO produtos (nome, preco)", "DELETE FROM produtos", "UPDATE produtos SET nome"]),
                "lista_atividade_id": 1
            },
            {
                "id": 2,
                "enunciado": "Uma biblioteca precisa consultar todas as informações dos livros disponíveis em seu acervo, incluindo título, autor e ano de publicação. Qual consulta deve ser utilizada?",
                "alternativas": json.dumps(["SELECT * FROM livros", "SELECT livros FROM titulo", "SHOW livros", "GET * FROM livros"]),
                "lista_atividade_id": 1
            },
            {
                "id": 3,
                "enunciado": "A secretaria de uma escola deseja visualizar apenas os nomes e as datas de nascimento dos alunos matriculados. Qual consulta atende a essa necessidade?",
                "alternativas": json.dumps(["SELECT nome, data_nascimento FROM alunos", "SELECT * FROM nome, data_nascimento", "SELECT nome AND data_nascimento FROM alunos", "SHOW nome, data_nascimento FROM alunos"]),
                "lista_atividade_id": 1
            },

            # Lista 2 - SELECT: Ordenação com ORDER BY
            {
                "id": 4,
                "enunciado": "Uma loja virtual deseja exibir seus produtos organizados pelo preço, começando pelos mais baratos. Qual consulta realiza essa ordenação?",
                "alternativas": json.dumps(["SELECT * FROM produtos ORDER BY preco ASC", "SELECT * FROM produtos ORDER BY preco DESC", "SELECT * FROM produtos WHERE preco ASC", "SELECT * FROM produtos GROUP BY preco"]),
                "lista_atividade_id": 2
            },
            {
                "id": 5,
                "enunciado": "Uma biblioteca deseja apresentar seu catálogo em ordem alfabética, utilizando o título dos livros como critério. Qual comando deve ser utilizado?",
                "alternativas": json.dumps(["SELECT * FROM livros ORDER BY titulo ASC", "SELECT * FROM livros ORDER BY titulo DESC", "SELECT * FROM livros WHERE titulo ASC", "SELECT * FROM livros GROUP BY titulo"]),
                "lista_atividade_id": 2
            },
            {
                "id": 6,
                "enunciado": "A coordenação de uma escola deseja visualizar os alunos organizados da maior para a menor nota em uma avaliação. Considerando a coluna nota, qual consulta atende a essa necessidade?",
                "alternativas": json.dumps(["SELECT * FROM alunos ORDER BY nota DESC", "SELECT * FROM alunos ORDER BY nota ASC", "SELECT * FROM alunos WHERE nota DESC", "SELECT * FROM alunos GROUP BY nota"]),
                "lista_atividade_id": 2
            },

            # ==========================================
            # MÓDULO 2 - WHERE
            # ==========================================

            # Lista 3 - WHERE: Operadores de Comparação
            {
                "id": 7,
                "enunciado": "Uma loja virtual deseja localizar todos os produtos que custam mais de R$ 100,00. Qual consulta deve ser utilizada?",
                "alternativas": json.dumps(["SELECT * FROM produtos WHERE preco > 100", "SELECT * FROM produtos WHERE preco < 100", "SELECT * FROM produtos ORDER BY preco", "SELECT * FROM produtos WHERE preco = 100"]),
                "lista_atividade_id": 3
            },
            {
                "id": 8,
                "enunciado": "Uma biblioteca precisa localizar os empréstimos que ainda não foram devolvidos. Na tabela emprestimos, a coluna devolvido armazena o valor 'Sim' ou 'Não'. Qual consulta retorna apenas os empréstimos pendentes?",
                "alternativas": json.dumps(["SELECT * FROM emprestimos WHERE devolvido = 'Não'", "SELECT * FROM emprestimos WHERE devolvido = 'Sim'", "SELECT * FROM emprestimos ORDER BY devolvido", "SELECT * FROM emprestimos WHERE devolvido > 'Não'"]),
                "lista_atividade_id": 3
            },
            {
                "id": 9,
                "enunciado": "A secretaria de uma escola deseja identificar os alunos que obtiveram nota inferior a 6 em uma avaliação. Qual consulta permite encontrar esses alunos?",
                "alternativas": json.dumps(["SELECT * FROM alunos WHERE nota < 6", "SELECT * FROM alunos WHERE nota > 6", "SELECT * FROM alunos WHERE nota = 6", "SELECT * FROM alunos ORDER BY nota"]),
                "lista_atividade_id": 3
            },

            # Lista 4 - WHERE: Filtros Avançados (LIKE, IN, BETWEEN)
            {
                "id": 10,
                "enunciado": "Uma loja virtual deseja encontrar todos os clientes cujos nomes começam com a letra 'A'. Qual consulta utiliza corretamente o operador LIKE?",
                "alternativas": json.dumps(["SELECT * FROM clientes WHERE nome LIKE 'A%'", "SELECT * FROM clientes WHERE nome IN 'A%'", "SELECT * FROM clientes WHERE nome BETWEEN 'A' AND 'Z'", "SELECT * FROM clientes WHERE nome = '%A'"]),
                "lista_atividade_id": 4
            },
            {
                "id": 11,
                "enunciado": "Uma biblioteca deseja localizar os livros publicados entre os anos de 2010 e 2020, incluindo os dois anos. Qual consulta atende a essa necessidade?",
                "alternativas": json.dumps(["SELECT * FROM livros WHERE ano_publicacao BETWEEN 2010 AND 2020", "SELECT * FROM livros WHERE ano_publicacao IN (2010, 2020)", "SELECT * FROM livros WHERE ano_publicacao LIKE '2010-2020'", "SELECT * FROM livros WHERE ano_publicacao > 2020"]),
                "lista_atividade_id": 4
            },
            {
                "id": 12,
                "enunciado": "Uma escola deseja consultar os alunos matriculados nas turmas A, B ou C. Considerando a coluna turma, qual consulta utiliza corretamente o operador IN?",
                "alternativas": json.dumps(["SELECT * FROM alunos WHERE turma IN ('A', 'B', 'C')", "SELECT * FROM alunos WHERE turma LIKE ('A', 'B', 'C')", "SELECT * FROM alunos WHERE turma BETWEEN 'A' AND 'C'", "SELECT * FROM alunos WHERE turma = IN ('A', 'B', 'C')"]),
                "lista_atividade_id": 4
            },

            # ==========================================
            # MÓDULO 3 - JOIN
            # ==========================================

            # Lista 5 - JOIN: INNER JOIN
            {
                "id": 13,
                "enunciado": "Uma loja virtual possui uma tabela clientes e outra chamada pedidos. Para gerar um relatório com o nome de cada cliente e seus respectivos pedidos, é necessário combinar as duas tabelas. Qual comando permite isso?",
                "alternativas": json.dumps(["SELECT * FROM clientes INNER JOIN pedidos ON clientes.id = pedidos.cliente_id", "SELECT * FROM clientes WHERE pedidos.id = clientes.id", "SELECT * FROM clientes ORDER BY pedidos.id", "SELECT * FROM clientes GROUP BY pedidos"]),
                "lista_atividade_id": 5
            },
            {
                "id": 14,
                "enunciado": "Uma biblioteca armazena os dados dos livros em uma tabela e os empréstimos em outra. A coluna livro_id da tabela emprestimos referencia o id da tabela livros. Qual consulta mostra os títulos dos livros e as respectivas datas de empréstimo, considerando apenas registros relacionados?",
                "alternativas": json.dumps(["SELECT livros.titulo, emprestimos.data_emprestimo FROM livros INNER JOIN emprestimos ON livros.id = emprestimos.livro_id", "SELECT livros.titulo, emprestimos.data_emprestimo FROM livros WHERE livros.id = emprestimos.livro_id", "SELECT * FROM livros ORDER BY emprestimos.data_emprestimo", "SELECT * FROM livros GROUP BY emprestimos.livro_id"]),
                "lista_atividade_id": 5
            },
            {
                "id": 15,
                "enunciado": "Uma escola deseja gerar um relatório contendo o nome dos alunos e o nome dos cursos nos quais estão matriculados. A tabela matriculas possui as colunas aluno_id e curso_id. Qual consulta combina corretamente essas informações?",
                "alternativas": json.dumps(["SELECT alunos.nome, cursos.nome FROM matriculas INNER JOIN alunos ON matriculas.aluno_id = alunos.id INNER JOIN cursos ON matriculas.curso_id = cursos.id", "SELECT alunos.nome, cursos.nome FROM matriculas WHERE alunos.id = cursos.id", "SELECT * FROM alunos ORDER BY cursos.nome", "SELECT * FROM matriculas GROUP BY alunos.nome"]),
                "lista_atividade_id": 5
            },

            # Lista 6 - JOIN: LEFT JOIN
            {
                "id": 16,
                "enunciado": "Uma loja virtual deseja gerar um relatório com todos os clientes cadastrados, inclusive aqueles que nunca realizaram pedidos. Qual consulta permite obter esse resultado?",
                "alternativas": json.dumps(["SELECT * FROM clientes LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id", "SELECT * FROM clientes INNER JOIN pedidos ON clientes.id = pedidos.cliente_id", "SELECT * FROM pedidos INNER JOIN clientes ON pedidos.cliente_id = clientes.id", "SELECT * FROM clientes WHERE pedidos.id IS NOT NULL"]),
                "lista_atividade_id": 6
            },
            {
                "id": 17,
                "enunciado": "Uma biblioteca deseja listar todos os livros de seu acervo, inclusive aqueles que nunca foram emprestados. Quando um livro não possui empréstimos relacionados, o que aparecerá nas colunas da tabela emprestimos ao utilizar LEFT JOIN?",
                "alternativas": json.dumps(["Valores NULL", "Valores iguais a zero obrigatoriamente", "Os dados do último empréstimo", "O registro do livro será excluído"]),
                "lista_atividade_id": 6
            },
            {
                "id": 18,
                "enunciado": "A coordenação de uma escola deseja consultar todos os alunos e suas respectivas matrículas, incluindo aqueles que ainda não estão matriculados em nenhum curso. Qual consulta atende a essa necessidade?",
                "alternativas": json.dumps(["SELECT * FROM alunos LEFT JOIN matriculas ON alunos.id = matriculas.aluno_id", "SELECT * FROM alunos INNER JOIN matriculas ON alunos.id = matriculas.aluno_id", "SELECT * FROM matriculas INNER JOIN alunos ON matriculas.aluno_id = alunos.id", "SELECT * FROM alunos WHERE matriculas.id IS NOT NULL"]),
                "lista_atividade_id": 6
            },

            # ==========================================
            # MÓDULO 4 - GROUP BY
            # ==========================================

            # Lista 7 - GROUP BY: Funções de Agregação
            {
                "id": 19,
                "enunciado": "Uma loja virtual deseja descobrir quantos produtos estão cadastrados em seu catálogo. Qual função SQL permite contar esses registros?",
                "alternativas": json.dumps(["COUNT()", "SUM()", "AVG()", "MAX()"]),
                "lista_atividade_id": 7
            },
            {
                "id": 20,
                "enunciado": "Uma biblioteca deseja calcular a média de dias que os usuários permanecem com os livros emprestados. Considerando a coluna dias_emprestados, qual função deve ser utilizada?",
                "alternativas": json.dumps(["AVG(dias_emprestados)", "SUM(dias_emprestados)", "COUNT(dias_emprestados)", "MAX(dias_emprestados)"]),
                "lista_atividade_id": 7
            },
            {
                "id": 21,
                "enunciado": "Uma escola deseja calcular a soma das notas de todos os alunos de uma avaliação. Considerando a coluna nota da tabela alunos, qual consulta realiza essa operação?",
                "alternativas": json.dumps(["SELECT SUM(nota) FROM alunos", "SELECT AVG(nota) FROM alunos", "SELECT COUNT(nota) FROM alunos", "SELECT MIN(nota) FROM alunos"]),
                "lista_atividade_id": 7
            },

            # Lista 8 - GROUP BY: Filtrando Grupos com HAVING
            {
                "id": 22,
                "enunciado": "Uma loja virtual deseja gerar um relatório que apresente a quantidade de pedidos realizados por cada cliente. Considerando a tabela pedidos, qual cláusula permite agrupar os registros pelo identificador do cliente?",
                "alternativas": json.dumps(["GROUP BY cliente_id", "ORDER BY cliente_id", "WHERE cliente_id", "DELETE cliente_id"]),
                "lista_atividade_id": 8
            },
            {
                "id": 23,
                "enunciado": "Uma biblioteca deseja identificar os usuários que realizaram mais de três empréstimos. Para isso, precisa agrupar os empréstimos por usuário e filtrar os grupos pela quantidade. Qual cláusula deve ser utilizada para aplicar essa condição após o agrupamento?",
                "alternativas": json.dumps(["HAVING", "WHERE", "ORDER BY", "INSERT"]),
                "lista_atividade_id": 8
            },
            {
                "id": 24,
                "enunciado": "Uma escola deseja identificar as turmas que possuem mais de 20 alunos matriculados. Qual consulta realiza o agrupamento por turma e apresenta somente aquelas que atendem a essa condição?",
                "alternativas": json.dumps(["SELECT turma, COUNT(*) FROM matriculas GROUP BY turma HAVING COUNT(*) > 20", "SELECT turma, COUNT(*) FROM matriculas WHERE COUNT(*) > 20", "SELECT turma FROM matriculas ORDER BY COUNT(*) > 20", "SELECT turma, COUNT(*) FROM matriculas GROUP BY turma WHERE COUNT(*) > 20"]),
                "lista_atividade_id": 8
            },

            # ==========================================
            # MÓDULO 5 - SUBCONSULTAS
            # ==========================================

            # Lista 9 - Subconsultas: Uso no WHERE
            {
                "id": 25,
                "enunciado": "Uma loja virtual deseja encontrar os produtos que possuem preço superior à média de preços de todo o catálogo. Qual consulta utiliza corretamente uma subconsulta na cláusula WHERE?",
                "alternativas": json.dumps(["SELECT * FROM produtos WHERE preco > (SELECT AVG(preco) FROM produtos)", "SELECT * FROM produtos WHERE preco = AVG(preco)", "SELECT * FROM produtos ORDER BY AVG(preco)", "SELECT AVG(preco) FROM produtos WHERE preco > produtos"]),
                "lista_atividade_id": 9
            },
            {
                "id": 26,
                "enunciado": "Uma biblioteca deseja consultar os livros que já foram emprestados. Para isso, pretende verificar se o identificador de cada livro aparece na tabela emprestimos. Qual operador pode ser utilizado com uma subconsulta para verificar essa condição?",
                "alternativas": json.dumps(["IN", "ORDER BY", "UPDATE", "GROUP BY"]),
                "lista_atividade_id": 9
            },
            {
                "id": 27,
                "enunciado": "Uma escola deseja localizar os alunos que possuem nota superior à nota média da turma de código 5. Considerando que a tabela alunos possui as colunas nome, nota e turma_id, qual consulta atende a essa necessidade?",
                "alternativas": json.dumps(["SELECT * FROM alunos WHERE nota > (SELECT AVG(nota) FROM alunos WHERE turma_id = 5)", "SELECT * FROM alunos WHERE nota = AVG(nota)", "SELECT * FROM alunos WHERE turma_id IN AVG(5)", "SELECT AVG(nota) FROM alunos GROUP BY nota"]),
                "lista_atividade_id": 9
            },

            # Lista 10 - Subconsultas: Uso no FROM
            {
                "id": 28,
                "enunciado": "Uma loja virtual deseja criar um relatório que apresente a média de preços dos produtos como se fosse uma tabela temporária, permitindo consultar esse resultado na consulta principal. Qual cláusula permite utilizar uma subconsulta dessa maneira?",
                "alternativas": json.dumps(["FROM", "WHERE", "ORDER BY", "DELETE"]),
                "lista_atividade_id": 10
            },
            {
                "id": 29,
                "enunciado": "Uma biblioteca deseja consultar a quantidade de empréstimos realizados por cada usuário utilizando uma subconsulta no FROM. Por que é necessário atribuir um alias à subconsulta?",
                "alternativas": json.dumps(["Para identificar e referenciar o resultado da subconsulta como uma tabela", "Para excluir automaticamente os empréstimos", "Para transformar a subconsulta em uma chave primária", "Para impedir a utilização de outras tabelas"]),
                "lista_atividade_id": 10
            },
            {
                "id": 30,
                "enunciado": "Uma escola deseja consultar a média das notas dos alunos utilizando uma subconsulta no FROM. Qual alternativa apresenta uma consulta SQL válida para essa situação?",
                "alternativas": json.dumps(["SELECT resultado.media FROM (SELECT AVG(nota) AS media FROM alunos) AS resultado", "SELECT resultado.media FROM alunos AS (SELECT AVG(nota) AS media)", "SELECT AVG(nota) FROM (alunos) WHERE resultado", "SELECT * FROM alunos WHERE (SELECT AVG(nota) AS media)"]),
                "lista_atividade_id": 10
            },

            # ==========================================
            # MÓDULO 6 - MANIPULAÇÃO DE DADOS
            # ==========================================

            # Lista 11 - CRUD: Inserção e Atualização (INSERT e UPDATE)
            {
                "id": 31,
                "enunciado": "Uma loja virtual recebeu o cadastro de um novo cliente chamado Gabriel, com o email gabriel@email.com. Qual comando SQL permite inserir essas informações na tabela clientes?",
                "alternativas": json.dumps(["INSERT INTO clientes (nome, email) VALUES ('Gabriel', 'gabriel@email.com')", "UPDATE clientes SET nome = 'Gabriel', email = 'gabriel@email.com'", "DELETE FROM clientes WHERE nome = 'Gabriel'", "SELECT nome, email FROM clientes"]),
                "lista_atividade_id": 11
            },
            {
                "id": 32,
                "enunciado": "Um funcionário da biblioteca percebeu que a data de devolução prevista de um empréstimo foi cadastrada incorretamente. Qual comando permite atualizar essa informação no registro de id igual a 15?",
                "alternativas": json.dumps(["UPDATE emprestimos SET data_devolucao = '2026-12-10' WHERE id = 15", "INSERT INTO emprestimos (data_devolucao) VALUES ('2026-12-10')", "DELETE FROM emprestimos WHERE id = 15", "SELECT data_devolucao FROM emprestimos WHERE id = 15"]),
                "lista_atividade_id": 11
            },
            {
                "id": 33,
                "enunciado": "A secretaria de uma escola identificou que a nota de um aluno foi cadastrada incorretamente. Para corrigir a nota do aluno cujo id é 8, qual comando deve ser utilizado?",
                "alternativas": json.dumps(["UPDATE alunos SET nota = 9 WHERE id = 8", "INSERT INTO alunos (nota) VALUES (9)", "DELETE FROM alunos WHERE id = 8", "SELECT nota FROM alunos WHERE id = 8"]),
                "lista_atividade_id": 11
            },

            # Lista 12 - CRUD: Exclusão de Registros (DELETE)
            {
                "id": 34,
                "enunciado": "Uma loja virtual encerrou a parceria com um fornecedor e deseja remover do cadastro um produto descontinuado, cujo id é 25. Qual comando permite excluir somente esse produto?",
                "alternativas": json.dumps(["DELETE FROM produtos WHERE id = 25", "DELETE FROM produtos", "DROP TABLE produtos WHERE id = 25", "UPDATE produtos SET id = NULL WHERE id = 25"]),
                "lista_atividade_id": 12
            },
            {
                "id": 35,
                "enunciado": "Uma biblioteca identificou que um empréstimo foi cadastrado por engano e precisa removê-lo da tabela emprestimos. Sabendo que o registro possui id igual a 12, qual consulta realiza a exclusão correta?",
                "alternativas": json.dumps(["DELETE FROM emprestimos WHERE id = 12", "DELETE emprestimos WHERE id = 12", "DROP TABLE emprestimos", "UPDATE emprestimos SET id = NULL WHERE id = 12"]),
                "lista_atividade_id": 12
            },
            {
                "id": 36,
                "enunciado": "Uma escola deseja remover todos os registros de uma tabela temporária chamada matriculas_teste, utilizada apenas para simulações. Qual comando exclui todos os registros, mantendo a estrutura da tabela?",
                "alternativas": json.dumps(["DELETE FROM matriculas_teste", "DROP TABLE matriculas_teste", "UPDATE matriculas_teste SET id = NULL", "SELECT * FROM matriculas_teste"]),
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