from repository.lista_atividade_repository import ListaAtividadeRepository

class ListaAtividadeService:
    def __init__(self):
        self.lista_repo = ListaAtividadeRepository()

    def listar_todas(self):
        if self.lista_repo.quantidade() == 0:
            raise ValueError("Nenhuma lista de atividade cadastrada.")
        return self.lista_repo.buscar_todas()

    def obter_lista(self, lista_id):
        if lista_id <= 0:
            raise ValueError("ID de lista inválido.")
        lista = self.lista_repo.buscar_por_id(lista_id)
        if not lista:
            raise ValueError("Lista de atividade não encontrada.")
        return lista

    def cadastrar_lista(self, dados):
        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
        modulo_id = dados.get("modulo_id")

        if not titulo or not modulo_id:
            raise ValueError("Título e modulo_id são obrigatórios.")
        return self.lista_repo.salvar(titulo, descricao, modulo_id)