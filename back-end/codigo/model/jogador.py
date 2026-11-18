class Jogador:

  def __init__(self, nome, email, senha=None, atividades=None):
    self.__nome = nome
    self.__email = email
    self.__senha = senha
    # Relacionamento Muitos-para-Muitos (N:N) com Atividade (Aula 14):
    # um jogador resolve várias atividades e cada atividade é resolvida
    # por vários jogadores - no banco isso vive na tabela intermediária
    # jogador_atividade; na classe, é uma lista de atividades.
    self.__atividades = atividades or []

  def get_nome(self):
    return self.__nome

  def set_nome(self, nome):
    if not nome.strip():
      raise ValueError("Nome não pode ser vazio")
    self.__nome = nome

  def get_email(self):
    return self.__email

  def set_email(self, email):
    if "@" not in email:
      raise ValueError("Email inválido")
    self.__email = email

  def get_senha(self):
    return self.__senha

  def set_senha(self, senha):
    self.__senha = senha

  # ------------------- Relacionamento N:N -------------------

  def get_atividades(self):
    return self.__atividades

  def adicionar_atividade(self, atividade):
    if atividade in self.__atividades:
      raise ValueError("Atividade já vinculada a este jogador")
    self.__atividades.append(atividade)
    # Mantém o vínculo bidirecional (o outro lado do N:N)
    if self not in atividade.get_jogadores():
      atividade.adicionar_jogador(self)

  def remover_atividade(self, atividade):
    if atividade not in self.__atividades:
      raise ValueError("Atividade não vinculada a este jogador")
    self.__atividades.remove(atividade)

  def atividades_ids(self):
    """Lista de IDs das atividades vinculadas (usada na persistência N:N)."""
    return [atividade.get_id() for atividade in self.__atividades]

  def to_dic(self):
    # Nota: nunca retorne a senha no dicionário por segurança!
    return {
        "nome": self.__nome,
        "email": self.__email,
        "atividades_ids": self.atividades_ids(),
    }

  def __str__(self):
    return (
        f"Jogador(nome='{self.__nome}', email='{self.__email}', "
        f"atividades_ids={self.atividades_ids()})"
    )
