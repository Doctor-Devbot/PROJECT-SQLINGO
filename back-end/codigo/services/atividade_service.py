from repository.atividade_repository import AtividadeRepository

class AtividadeService:
    def __init__(self):
        self.atividade_repo = AtividadeRepository()
    def obter_perfil_atividade(self, atividade_id):
        if atividade_id <= 0:
            raise ValueError("ID de atividade inválido.")
        perfil = self.atividade_repo.obter_perfil_completo(atividade_id)
        if not perfil:
            raise ValueError("Atividade não encontrado.")
        if not perfil.ativo:
            raise ValueError("Acesso negado: Atividade inativa no sistema.")
        return perfil

    def cadastrar_atividade(self, enunciado):
        # Regra 1: Campos obrigatórios
        if not enunciado:
            raise ValueError("Enunciado é obrigatório.")
        # Salva via Repository
        self.atividade_repo.salvar(enunciado)