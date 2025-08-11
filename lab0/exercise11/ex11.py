# --- Exercício 11 - Impressão de várias expressões em uma só chamada ---

# 1. Armazena o ano de fundação da UEFS em uma variável.
# Este é o nosso valor "XXXX".
ano_fundacao_uefs = 1976

# 2. Pede ao usuário para digitar o ano corrente.
# Este será o nosso valor "YYYY".
# A entrada é convertida para um número inteiro com int() para permitir cálculos.
ano_corrente = int(input("Digite o ano corrente: "))

# 3. Executa o comando print exatamente como solicitado no exercício.
# - O primeiro "YYYY" é substituído pela variável ano_corrente.
# - A expressão "YYYY - XXXX" é calculada (ano_corrente - ano_fundacao_uefs).
# - A função print() imprime cada um dos itens separados por vírgula, adicionando
#   um espaço entre eles.
print("Em ", ano_corrente, "a UEFS completou", ano_corrente - ano_fundacao_uefs, "anos de fundacao.")
