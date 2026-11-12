class Resposta:
    def __init__(self, correta):
        self.correta = correta

    def get_correta(self):
        return self.correta
    def set_correta(self, correta):
        self.correta = correta

    def __str__(self):
        return f"Resposta(correta={self.correta})"