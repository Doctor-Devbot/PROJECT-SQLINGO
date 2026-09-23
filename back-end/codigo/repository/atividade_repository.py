from dao.atividade_dao import AtividadeDAO

class AtividadeRepository:
    def obter_perfil_completo(self, atividade_id):
        # 1. Busca dados cadastrais bsicos no DAO
        cadastrais = AtividadeDAO.buscar_dados_cadastrais(atividade_id)
        if not cadastrais:
            return None
        # 2. Busca dados de segurança/acesso no DAO
        seguranca = AtividadeDAO.buscar_dados_seguranca(atividade_id)
        # 3. Combina os resultados no objeto do usuário
        cadastrais.perfil = seguranca["ativo"]
        cadastrais.nivel_acesso = seguranca["nivel_acesso"]
        return cadastrais

    def salvar(self, enunciado):
        AtividadeDAO.criar(enunciado)

    #def email_ja_cadastrado(self, email):
        #return AtividadeDAO.buscar_id_por_email(email) is not None