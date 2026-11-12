from dao.atividade_dao import AtividadeDAO

class AtividadeRepository:

    def buscar_por_id(self, atividade_id):
        return AtividadeDAO.retrieve_by_id(atividade_id)

    def buscar_todas(self):
        return AtividadeDAO.retrieve_all()

    def salvar(self, enunciado, alternativas, id_atividade=None):
        return AtividadeDAO.create(enunciado, alternativas, id_atividade)

    def atualizar(self, atividade_id, enunciado=None, alternativas=None):
        return AtividadeDAO.update(atividade_id, enunciado, alternativas)

    def deletar(self, atividade_id):
        return AtividadeDAO.delete(atividade_id)

    def quantidade(self):
        return AtividadeDAO.size()