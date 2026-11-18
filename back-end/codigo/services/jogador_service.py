from repository.jogador_repository import JogadorRepository

class JogadorService:

    def __init__(self):
        self.jogador_repo = JogadorRepository()

    def obter_jogador_por_email(self, email):
        if not email or "@" not in email:
            raise ValueError("Formato de e-mail inválido.")

        jogador = self.jogador_repo.buscar_por_email(email)
        if not jogador:
            raise ValueError("Jogador não encontrado.")

        return jogador

    def listar_todos(self):
        if self.jogador_repo.quantidade() == 0:
            raise ValueError("Nenhum jogador cadastrado.")

        return self.jogador_repo.buscar_todos()

    def cadastrar_jogador(self, dados):
        nome = dados.get("nome")
        email = dados.get("email")
        senha = dados.get("senha")
        atividades_ids = dados.get("atividades_ids") or []

        # Regra 1: Campos obrigatórios
        if not nome or not email:
            raise ValueError("Nome e e-mail são obrigatórios.")

        # Regra 2: Formato do e-mail
        if "@" not in email:
            raise ValueError("Formato de e-mail inválido.")

        # Regra 3: Unicidade do e-mail
        if self.jogador_repo.email_ja_cadastrado(email):
            raise ValueError("Este e-mail já está em uso por outro jogador.")

        # Regra 4: Relacionamento N:N - lista de IDs de atividades
        if not isinstance(atividades_ids, list):
            raise ValueError("O campo 'atividades_ids' deve ser uma lista de inteiros.")

        return self.jogador_repo.salvar(nome, email, senha, atividades_ids)

    def atualizar_nome(self, email, dados):
        nome = dados.get("nome")

        if not nome:
            raise ValueError("O novo nome é obrigatório.")

        if not email or "@" not in email:
            raise ValueError("Formato de e-mail inválido.")

        jogador_atualizado = self.jogador_repo.atualizar_nome(email, nome)
        if not jogador_atualizado:
            raise ValueError("Jogador não encontrado.")

        return jogador_atualizado

    def listar_jogadores_paginacao(self, pagina, por_pagina):
        """Delega ao repositório a busca paginada com JSON aninhado do N:N."""
        if pagina <= 0:
            raise ValueError("O número da página deve ser maior que zero.")

        if por_pagina <= 0:
            raise ValueError("A quantidade de registros por página deve ser maior que zero.")

        return self.jogador_repo.jogadores_paginacao(pagina, por_pagina)

    def deletar_jogador(self, email):
        if not email or "@" not in email:
            raise ValueError("Formato de e-mail inválido.")

        jogador_removido = self.jogador_repo.deletar(email)
        if not jogador_removido:
            raise ValueError("Jogador não encontrado.")

        return jogador_removido