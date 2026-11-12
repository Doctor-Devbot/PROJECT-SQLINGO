class Atividade:
    def __init__(self, id_atividade, enunciado, alternativas=None, jogador=None, resposta=None):
        self.id_atividade = id_atividade
        self.enunciado = enunciado
        self.jogador = jogador
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

    def get_jogador(self):
        return self.jogador

    def set_jogador(self, jogador):
        self.jogador = jogador

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
            "alternativas": self.alternativas
        }

    def __str__(self):
        return f"Atividade(id={self.id_atividade}, enunciado='{self.enunciado}', alternativas={self.alternativas})"