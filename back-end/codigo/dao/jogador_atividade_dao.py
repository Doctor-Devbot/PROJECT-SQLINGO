from sqlalchemy import text
from services.db_service import db, prefixo_insert_ignorado


class JogadorAtividadeDAO:
    """
    DAO da tabela intermediária jogador_atividade.

    Relacionamento Muitos-para-Muitos (N:N) entre jogadores e atividades
    (Aula 14): um jogador pode resolver várias atividades e uma atividade
    pode ser resolvida por vários jogadores. Assim como o exemplo
    usuario_grupo dos slides, a tabela intermediária guarda apenas as duas
    chaves estrangeiras e possui chave primária composta.
    """

    @staticmethod
    def criar_tabela_jogador_atividade():
        # DDL válido tanto em SQLite quanto em MySQL (chave composta + FKs)
        sql = text("""
            CREATE TABLE IF NOT EXISTS jogador_atividade (
                jogador_id INTEGER NOT NULL,
                atividade_id INTEGER NOT NULL,
                PRIMARY KEY (jogador_id, atividade_id),
                FOREIGN KEY (jogador_id) REFERENCES jogadores(id) ON DELETE CASCADE,
                FOREIGN KEY (atividade_id) REFERENCES atividades(id) ON DELETE CASCADE
            );
        """)
        db.session.execute(sql)
        db.session.commit()

    @staticmethod
    def busca_atividades_ids(jogador_id):
        """
        Busca apenas a lista de IDs das atividades resolvidas pelo jogador.
        O método .scalars().all() extrai diretamente o valor escalar de cada
        linha (igual ao GruposDAO.busca_grupos da Aula 14).
        """
        sql = text(
            "SELECT atividade_id FROM jogador_atividade WHERE jogador_id = :jogador_id;"
        )
        return db.session.execute(sql, {"jogador_id": jogador_id}).scalars().all()

    @staticmethod
    def busca_jogadores_ids(atividade_id):
        """Busca a lista de IDs dos jogadores que resolveram a atividade."""
        sql = text(
            "SELECT jogador_id FROM jogador_atividade WHERE atividade_id = :atividade_id;"
        )
        return db.session.execute(sql, {"atividade_id": atividade_id}).scalars().all()

    @staticmethod
    def vincular(jogador_id, atividade_id):
        """
        Registra um vínculo N:N na tabela intermediária.
        INSERT IGNORE / INSERT OR IGNORE evita duplicar o mesmo vínculo
        (a chave primária composta já barraria a duplicação).
        """
        sql = text(f"""
            {prefixo_insert_ignorado()} INTO jogador_atividade (jogador_id, atividade_id)
            VALUES (:jogador_id, :atividade_id);
        """)
        db.session.execute(sql, {"jogador_id": jogador_id, "atividade_id": atividade_id})

    @staticmethod
    def vincular_atividades(jogador_id, atividades_ids):
        """
        Insere todos os vínculos N:N recebidos no JSON da requisição
        (lista "atividades_ids"), commitando ao final - igual ao
        UsuarioDAO.adiciona_grupos da Aula 14.
        """
        for atividade_id in atividades_ids:
            JogadorAtividadeDAO.vincular(jogador_id, atividade_id)
        db.session.commit()

    @staticmethod
    def desvincular(jogador_id, atividade_id):
        """Remove um vínculo N:N específico da tabela intermediária."""
        sql = text("""
            DELETE FROM jogador_atividade
            WHERE jogador_id = :jogador_id AND atividade_id = :atividade_id;
        """)
        db.session.execute(sql, {"jogador_id": jogador_id, "atividade_id": atividade_id})
        db.session.commit()
