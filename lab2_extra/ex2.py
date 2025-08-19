# Exercício 2 - Validador de Empréstimo Bancário
# Escreva um programa que analise se um cliente pode receber um empréstimo.
# O programa deve ler três informações, nesta ordem:

# 1. Score de crédito do cliente (um inteiro de 0 a 1000)
score_credito = int(input("Digite o score de crédito (0 a 1000): "))

# 2. Idade do cliente
idade = int(input("Digite a idade do cliente: "))

# 3. Valor de renda mensal do cliente
renda_mensal = float(input("Digite a renda mensal: R$ "))

# 4. Valor da parcela mensal do empréstimo desejado
parcela_mensal = float(input("Digite o valor da parcela mensal desejada: R$ "))

# Regras para aprovação:
# O empréstimo é aprovado APENAS SE TODAS as seguintes condições forem verdadeiras:
# 1. O score de crédito for de 600 ou mais;
# 2. A idade estiver entre 21 e 70 anos;
# 3. O valor da parcela não pode custar mais do que 30% do seu salário.

# Calcular 30% da renda mensal
limite_parcela = renda_mensal * 0.30

# Verificar se TODAS as condições são atendidas
if (score_credito >= 600 and 
    idade >= 21 and idade <= 70 and 
    parcela_mensal <= limite_parcela):
    print("Emprestimo Aprovado")
else:
    print("Emprestimo Negado")