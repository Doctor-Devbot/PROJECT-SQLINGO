from dao.jogador_dao import JogadorDAO

class JogadorRepository:
    def obter_perfil_completo(self, usuario_id):
        # 1. Busca dados cadastrais bsicos no DAO
        cadastrais = JogadorDAO.buscar_dados_cadastrais(usuario_id)
        if not cadastrais:
            return None
        # 2. Busca dados de segurança/acesso no DAO
        seguranca = JogadorDAO.buscar_dados_seguranca(usuario_id)
        # 3. Combina os resultados no objeto do usuário
        cadastrais.perfil = seguranca["ativo"]
        cadastrais.nivel_acesso = seguranca["nivel_acesso"]
        return cadastrais

    def salvar(self, nome, email):
        JogadorDAO.criar(nome, email)

    def email_ja_cadastrado(self, email):
        return JogadorDAO.buscar_id_por_email(email) is not None