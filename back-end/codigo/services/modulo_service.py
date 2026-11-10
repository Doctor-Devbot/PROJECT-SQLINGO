from repository.modulo_repository import ModuloRepository

class ModuloService:
    def __init__(self):
        self.modulo_repo = ModuloRepository()

    def listar_todos(self):
        if self.modulo_repo.quantidade() == 0:
            raise ValueError("Nenhum módulo cadastrado.")
        return self.modulo_repo.buscar_todos()

    def obter_modulo(self, modulo_id):
        if modulo_id <= 0:
            raise ValueError("ID de módulo inválido.")
        modulo = self.modulo_repo.buscar_por_id(modulo_id)
        if not modulo:
            raise ValueError("Módulo não encontrado.")
        return modulo

    def cadastrar_modulo(self, dados):
        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
        if not titulo:
            raise ValueError("O título do módulo é obrigatório.")
        return self.modulo_repo.salvar(titulo, descricao)