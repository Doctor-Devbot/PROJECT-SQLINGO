from repository.atividade_repository import AtividadeRepository

class AtividadeService:

    def __init__(self):
        self.atividade_repo = AtividadeRepository()

    def obter_atividade(self, atividade_id):
        if atividade_id <= 0:
            raise ValueError("ID de atividade inválido.")

        atividade = self.atividade_repo.buscar_por_id(atividade_id)
        if not atividade:
            raise ValueError("Atividade não encontrada.")

        return atividade

    def listar_todas(self):
        if self.atividade_repo.quantidade() == 0:
            raise ValueError("Nenhuma atividade cadastrada.")

        return self.atividade_repo.buscar_todas()

    def cadastrar_atividade(self, dados):
        enunciado = dados.get("enunciado")
        alternativas = dados.get("alternativas", [])
        id_atividade = dados.get("id_atividade") or dados.get("id")

        if not enunciado:
            raise ValueError("O enunciado é obrigatório.")

        if not isinstance(alternativas, list):
            raise ValueError("O campo 'alternativas' deve ser uma lista.")

        if id_atividade and self.atividade_repo.buscar_por_id(id_atividade):
            raise ValueError("ID de atividade já cadastrado.")

        return self.atividade_repo.salvar(enunciado, alternativas, id_atividade)

    def atualizar_atividade(self, atividade_id, dados):
        if atividade_id <= 0:
            raise ValueError("ID de atividade inválido.")

        enunciado = dados.get("enunciado")
        alternativas = dados.get("alternativas")

        atividade = self.atividade_repo.buscar_por_id(atividade_id)
        if not atividade:
            raise ValueError("Atividade não encontrada.")

        return self.atividade_repo.atualizar(atividade_id, enunciado, alternativas)

    def deletar_atividade(self, atividade_id):
        if atividade_id <= 0:
            raise ValueError("ID de atividade inválido.")

        atividade = self.atividade_repo.deletar(atividade_id)
        if not atividade:
            raise ValueError("Atividade não encontrada.")

        return atividade