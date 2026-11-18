import math
from dao.jogador_atividade_dao import JogadorAtividadeDAO
from dao.jogador_dao import JogadorDAO


class JogadorRepository:
    """
    Repositório agregador do Jogador.

    Assim como o UsuarioRepository da Aula 14, ele orquestra a gravação
    relacional completa: insere o jogador na tabela principal e, em seguida,
    registra os vínculos Muitos-para-Muitos (N:N) na tabela intermediária
    jogador_atividade. Também monta o JSON aninhado das consultas,
    adicionando a lista "atividades_ids" de cada jogador.
    """

    def buscar_por_email(self, email):
        # 1. Busca os dados cadastrais do jogador (tabela principal)
        jogador = JogadorDAO.retrieve_by_email(email)
        # 2. Busca os IDs das atividades vinculadas (relacionamento N:N)
        if jogador:
            jogador["atividades_ids"] = list(
                JogadorAtividadeDAO.busca_atividades_ids(jogador["id"])
            )
        return jogador

    def buscar_todos(self):
        """
        Monta o JSON aninhado: para cada jogador consulta os vínculos N:N
        e compõe a lista "atividades_ids" da resposta (Aula 14).
        """
        jogadores = JogadorDAO.retrieve_all()
        for jogador in jogadores:
            jogador["atividades_ids"] = list(
                JogadorAtividadeDAO.busca_atividades_ids(jogador["id"])
            )
        return jogadores

    def salvar(self, nome, email, senha_hash, atividades_ids=None):
        """
        Orquestra a gravação relacional completa:
        1. Salva o jogador principal (JogadorDAO) e obtém o id gerado;
        2. Registra os vínculos N:N recebidos no campo "atividades_ids".
        """
        jogador = JogadorDAO.create(nome, email, senha_hash)
        if jogador and atividades_ids:
            JogadorAtividadeDAO.vincular_atividades(jogador["id"], atividades_ids)
        return jogador

    def atualizar_nome(self, email, nome):
        return JogadorDAO.update_nome(email, nome)

    def deletar(self, email):
        # ON DELETE CASCADE na tabela intermediária remove os vínculos N:N
        return JogadorDAO.delete(email)

    def quantidade(self):
        return JogadorDAO.size()

    def email_ja_cadastrado(self, email):
        return JogadorDAO.retrieve_by_email(email) is not None

    def jogadores_paginacao(self, pagina, por_pagina):
        """Calcula o offset, o total de páginas e retorna a estrutura de metadados de paginação."""
        # 1. Obtém o total de registros no banco e calcula o total de páginas
        total_jogadores = JogadorDAO.count_jogador()
        total_paginas = math.ceil(total_jogadores / por_pagina) if total_jogadores > 0 else 1

        # 2. Calcula o OFFSET (quantos registros pular)
        offset = por_pagina * (pagina - 1)
        jogadores_pagina = JogadorDAO.list_jogador_pagina(offset, por_pagina)

        # 3. Acrescenta o JSON aninhado do relacionamento N:N em cada item
        for jogador in jogadores_pagina:
            jogador["atividades_ids"] = list(
                JogadorAtividadeDAO.busca_atividades_ids(jogador["id"])
            )

        # 4. Constrói a estrutura JSON de metadados de navegação
        dados_paginacao = {
            "items": jogadores_pagina,
            "page": pagina,
            "por_pagina": por_pagina,
            "total_registros": total_jogadores,
            "total_pages": total_paginas,
            "has_prev": pagina > 1,
            "has_next": pagina < total_paginas,
            "prev_num": pagina - 1,
            "next_num": pagina + 1
        }

        return dados_paginacao
