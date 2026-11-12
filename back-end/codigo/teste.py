from model.jogador import Jogador
from model.resposta import Resposta
from model.atividade import Atividade
from model.lista_atividade import ListaAtividade
from model.modulo import Modulo
from model.comando import Comando

print("=== TESTANDO JOGADOR ===")
jogador = Jogador("Gabriel", "gabriel@email.com")
print(jogador)

jogador.set_nome("Gabriel Alves")
jogador.set_email("gabrielalves@email.com")

print("Nome:", jogador.get_nome())
print("E-mail:", jogador.get_email())

print("\n=== TESTANDO RESPOSTA ===")
resposta = Resposta(True)
print(resposta)

resposta.set_correta(False)
print("Resposta correta:", resposta.get_correta())

print("\n=== TESTANDO ATIVIDADE ===")
atividade = Atividade(
    1,
    "Qual comando SQL seleciona dados?",
    ["SELECT", "INSERT", "DELETE", "UPDATE"],
    jogador,
    resposta
)

print(atividade)

if hasattr(atividade, "get_id"):
    print("ID:", atividade.get_id())
if hasattr(atividade, "get_enunciado"):
    print("Enunciado:", atividade.get_enunciado())
if hasattr(atividade, "get_alternativas"):
    print("Alternativas:", atividade.get_alternativas())

if hasattr(atividade, "set_enunciado"):
    atividade.set_enunciado("Novo enunciado")
if hasattr(atividade, "set_alternativas"):
    atividade.set_alternativas(["A", "B", "C", "D"])

print("Atividade atualizada:", atividade)

print("\n=== TESTANDO LISTA DE ATIVIDADES ===")
lista = ListaAtividade(
    "Consultas SQL",
    "Lista de exercícios sobre SQL"
)

lista.atividades.append(atividade)

print(lista)
print("Título:", lista.get_titulo())
print("Descrição:", lista.get_descricao())

print("\n=== TESTANDO MÓDULO ===")
modulo = Modulo(
    "Banco de Dados",
    "Módulo introdutório"
)

modulo.listas_atividade.append(lista)

print(modulo)
print("Título:", modulo.get_titulo())
print("Descrição:", modulo.get_descricao())

print("\n=== TESTANDO COMANDO ===")
comando = Comando(
    "SELECT",
    "Seleciona registros de uma tabela"
)

print(comando)
print("Título:", comando.get_titulo())
print("Descrição:", comando.get_descricao())

comando.set_titulo("SELECT DISTINCT")
comando.set_descricao("Seleciona registros sem repetição")

print("Comando atualizado:", comando)

print("\n=== TESTE DE CONVERSÃO PARA DICIONÁRIO (to_dict) ===")
if hasattr(atividade, "to_dict"):
    print("Dicionário da atividade:", atividade.to_dict())
elif hasattr(atividade, "to_dic"):
    print("Dicionário da atividade:", atividade.to_dic())

if hasattr(jogador, "to_dict"):
    print("Dicionário do jogador:", jogador.to_dict())
elif hasattr(jogador, "to_dic"):
    print("Dicionário do jogador:", jogador.to_dic())

print("\n=== TESTANDO VALIDAÇÕES E EXCEÇÕES ===")

# Teste de e-mail inválido
try:
    jogador.set_email("emailinvalido")
except ValueError as e:
    print("Erro esperado (E-mail):", e)

# Teste de nome vazio
try:
    jogador.set_nome("")
except ValueError as e:
    print("Erro esperado (Nome):", e)

# Teste de validações na Atividade (caso implementadas no modelo)
if hasattr(atividade, "set_enunciado"):
    try:
        atividade.set_enunciado("")
    except ValueError as e:
        print("Erro esperado (Enunciado):", e)