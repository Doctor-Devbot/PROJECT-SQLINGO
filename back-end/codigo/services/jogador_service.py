from repository.jogador_repository import JogadorRepository

class JogadorService:
    def __init__(self):
        self.jogador_repo = JogadorRepository()
    def obter_perfil_jogador(self, jogador_id):
        if jogador_id <= 0:
            raise ValueError("ID de jogador inválido.")
        perfil = self.jogador_repo.obter_perfil_completo(jogador_id)
        if not perfil:
            raise ValueError("Jogador não encontrado.")
        if not perfil.ativo:
            raise ValueError("Acesso negado: Jogador inativo no sistema.")
        return perfil

    def cadastrar_jogador(self, nome, email):
        # Regra 1: Campos obrigatórios
        if not nome or not email:
            raise ValueError("Nome e e-mail são obrigatórios.")
        # Regra 2: Formato do e-mail
        if "@" not in email:
            raise ValueError("Formato de e-mail inválido.")
        # Regra 3: E-mail deve ser único (usa o repository)
        if self.jogador_repo.email_ja_cadastrado(email):
            raise ValueError("Este e-mail já está em uso por outro jogador.")
        # Salva via Repository
        self.jogador_repo.salvar(nome, email)