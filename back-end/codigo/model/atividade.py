class Atividade:
    def __init__(self, id_atividade, enunciado, alternativas=None, jogadores=None, resposta=None):
        self.id_atividade = id_atividade
        self.enunciado = enunciado
        # Relacionamento Muitos-para-Muitos (N:N) com Jogador (Aula 14):
        # esta lista corresponde à tabela intermediária jogador_atividade.
        self.jogadores = jogadores or []
        self.resposta = resposta
        self.alternativas = alternativas or []

    def get_enunciado(self):
        return self.enunciado

    def set_enunciado(self, enunciado):
        if not enunciado:
            raise ValueError("O enunciado não pode ser vazio")
        self.enunciado = enunciado

    def get_id(self):
        return self.id_atividade

    def set_id(self, id_atividade):
        if id_atividade <= 0:
            raise ValueError("O ID deve ser maior que zero")
        self.id_atividade = id_atividade

    def get_alternativas(self):
        return self.alternativas

    def set_alternativas(self, alternativas):
        self.alternativas = alternativas

    # ------------------- Relacionamento N:N -------------------

    def get_jogadores(self):
        return self.jogadores

    def adicionar_jogador(self, jogador):
        if jogador in self.jogadores:
            raise ValueError("Jogador já vinculada a esta atividade")
        self.jogadores.append(jogador)
        # Mantém o vínculo bidirecional (o outro lado do N:N)
        if self not in jogador.get_atividades():
            jogador.adicionar_atividade(self)

    def remover_jogador(self, jogador):
        if jogador not in self.jogadores:
            raise ValueError("Jogador não vinculado a esta atividade")
        self.jogadores.remove(jogador)

    def jogadores_ids(self):
        """Lista de IDs (e-mails) dos jogadores vinculados à atividade."""
        return [jogador.get_email() for jogador in self.jogadores]

    def get_resposta(self):
        return self.resposta

    def set_resposta(self, resposta):
        self.resposta = resposta

    def gerar_questao(self):
        return {
            "id_atividade": self.id_atividade,
            "enunciado": self.enunciado,
            "alternativas": self.alternativas
        }

    def to_dic(self):
        return {
            "id_atividade": self.id_atividade,
            "enunciado": self.enunciado,
            "alternativas": self.alternativas,
            "jogadores_ids": self.jogadores_ids()
        }

    def __str__(self):
        return (
            f"Atividade(id={self.id_atividade}, enunciado='{self.enunciado}', "
            f"alternativas={self.alternativas}, jogadores={self.jogadores_ids()})"
        )
