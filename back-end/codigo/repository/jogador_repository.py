from dao.jogador_dao import JogadorDAO

class JogadorRepository:

    def buscar_por_email(self, email):
        return JogadorDAO.retrieve_by_email(email)

    def buscar_todos(self):
        return JogadorDAO.retrieve_all()

    def salvar(self, nome, email):
        return JogadorDAO.create(nome, email)

    def atualizar_nome(self, email, nome):
        return JogadorDAO.update_nome(email, nome)

    def deletar(self, email):
        return JogadorDAO.delete(email)

    def quantidade(self):
        return JogadorDAO.size()

    def email_ja_cadastrado(self, email):
        return JogadorDAO.retrieve_by_email(email) is not None