class Jogador:

  def __init__(self, nome, email, senha=None):
    self.__nome = nome
    self.__email = email
    self.__senha = senha

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

  def to_dic(self):
    # Nota: nunca retorne a senha no dicionário por segurança!
    return {"nome": self.__nome, "email": self.__email}

  def __str__(self):
    return f"Jogador(nome='{self.__nome}', email='{self.__email}')"