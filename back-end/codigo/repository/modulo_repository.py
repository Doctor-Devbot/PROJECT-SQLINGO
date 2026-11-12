from dao.modulo_dao import ModuloDAO

class ModuloRepository:
    def buscar_por_id(self, modulo_id):
        return ModuloDAO.retrieve_by_id(modulo_id)

    def buscar_todos(self):
        return ModuloDAO.retrieve_all()

    def salvar(self, titulo, descricao, id_modulo=None):
        return ModuloDAO.create(titulo, descricao, id_modulo)

    def deletar(self, modulo_id):
        return ModuloDAO.delete(modulo_id)

    def quantidade(self):
        return ModuloDAO.size()