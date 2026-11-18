import math
from dao.jogador_dao import JogadorDAO

class JogadorRepository:

    def buscar_por_email(self, email):
        return JogadorDAO.retrieve_by_email(email)

    def buscar_todos(self):
        return JogadorDAO.retrieve_all()

    def salvar(self, nome, email, senha_hash):
        return JogadorDAO.create(nome, email, senha_hash)

    def atualizar_nome(self, email, nome):
        return JogadorDAO.update_nome(email, nome)

    def deletar(self, email):
        return JogadorDAO.delete(email)

    def quantidade(self):
        return JogadorDAO.size()

    def email_ja_cadastrado(self, email):
        return JogadorDAO.retrieve_by_email(email) is not None

    def jogadores_paginacao(self, pagina, por_pagina):
        """Calcula o offset, o total de páginas e retorna a estrutura de metadados de paginação."""
        # 1. Obtém o total de registros no banco e calcula o total de páginas
        total_jogadores = JogadorDAO.count_jogador()
        total_paginas = math.ceil(total_jogadores / por_pagina) if total_jogadores > 0 else 1
        
        # 2. Calcula o OFFSET (quantos registros pular)
        offset = por_pagina * (pagina - 1)
        jogadores_pagina = JogadorDAO.list_jogador_pagina(offset, por_pagina)
        
        # 3. Constrói a estrutura JSON de metadados de navegação[cite: 53]
        dados_paginacao = {
            "items": jogadores_pagina,
            "page": pagina,
            "total_pages": total_paginas,
            "has_prev": pagina > 1,
            "has_next": pagina < total_paginas,
            "prev_num": pagina - 1,
            "next_num": pagina + 1
        }
        
        return dados_paginacao