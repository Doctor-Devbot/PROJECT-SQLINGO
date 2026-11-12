class Jogador:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

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

    def to_dic(self):
        return {
            "nome": self.__nome,
            "email": self.__email
        }

    def __str__(self):
        return f"Jogador(nome='{self.__nome}', email='{self.__email}')"