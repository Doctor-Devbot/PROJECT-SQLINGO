from dao.jogador_dao import JogadorDAO

class JogadorRepository:
    
    def obter_perfil_completo(self, email):
        # Como o banco de dados atual de Jogador não possui tabelas separadas 
        # para segurança ou nível de acesso, apenas retornamos os dados existentes.
        jogador = JogadorDAO.retrieve_by_email(email)
        return jogador

    def salvar(self, nome, email):
        # Utiliza o método 'create' que definimos no JogadorDAO
        return JogadorDAO.create(nome, email)

    def email_ja_cadastrado(self, email):
        # Se retornar algo diferente de None, o e-mail já existe
        return JogadorDAO.retrieve_by_email(email) is not None