from model.atividade import Atividade
from model.jogador import Jogador
from model.resposta import Resposta

print("=== TESTES DA CLASSE ATIVIDADE ===\n")

atividade = Atividade(
    id_atividade=1,
    enunciado="Qual comando SQL seleciona dados?",
    alternativas=["SELECT", "INSERT", "DELETE", "UPDATE"]
)

print("[OK] Instanciação:")
print(atividade)
print(f"ID: {atividade.get_id()}")
print(f"Enunciado: {atividade.get_enunciado()}")
print(f"Alternativas: {atividade.get_alternativas()}\n")

print("[OK] Associando Jogador e Resposta:")
jogador1 = Jogador("Marco", "marco@email.com")
resposta1 = Resposta(True)

atividade.set_jogador(jogador1)
atividade.set_resposta(resposta1)

print(f"Jogador associado: {atividade.get_jogador()}")
print(f"Resposta associada: {atividade.get_resposta()}\n")

print("[OK] Teste dos métodos de dicionário:")
print("gerar_questao():", atividade.gerar_questao())
print("to_dic():", atividade.to_dic())

print("\n=== TESTANDO VALIDAÇÕES DE ERRO ===")

try:
    atividade.set_enunciado("")
    print("[ERRO] Falha: Aceitou enunciado vazio!")
except ValueError as e:
    print(f"[OK] Sucesso: Capturou erro de enunciado -> {e}")

try:
    atividade.set_id(0)
    print("[ERRO] Falha: Aceitou ID inválido!")
except ValueError as e:
    print(f"[OK] Sucesso: Capturou erro de ID -> {e}")

try:
    atividade.set_id(-5)
    print("[ERRO] Falha: Aceitou ID negativo!")
except ValueError as e:
    print(f"[OK] Sucesso: Capturou erro de ID negativo -> {e}")