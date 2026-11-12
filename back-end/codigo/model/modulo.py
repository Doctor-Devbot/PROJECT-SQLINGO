class Modulo:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.listas_atividade = [] #lista com objs da classe ListaAtividadeModel

    def get_titulo(self):
        return self.titulo
    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_descricao(self):
        return self.descricao
    def set_descricao(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return f"Modulo(titulo='{self.titulo}', descricao='{self.descricao}', qtd_listas={len(self.listas_atividade)})"