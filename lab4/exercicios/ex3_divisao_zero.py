"""
Exercício 3 - Divisão por zero?!

Escreva um programa que calcula a média de uma coleção de valores digitados pelo
usuário, com precisão de duas casas decimais. O usuário irá inserir 0 para indicar que não
há mais valores a serem fornecidos.
"""

print("=== Calculadora de Média ===")
print("Digite valores para calcular a média (0 para finalizar):")

soma = 0
contador = 0

# Lê o primeiro valor
valor = float(input("Digite um valor: "))

while valor != 0:
    # Adiciona o valor à soma e incrementa o contador
    soma += valor
    contador += 1
    
    # Lê o próximo valor
    valor = float(input("Digite um valor: "))

# Verifica se foram inseridos valores antes de calcular a média
if contador > 0:
    media = soma / contador
    print(f"Média: {media:.2f}")
else:
    print("Nenhum valor foi inserido para calcular a média.")
