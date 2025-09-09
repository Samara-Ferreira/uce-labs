"""
Exercício 6 - Saldo mensal

Uma pessoa investe uma quantia numa aplicação que rende 4% ao mês.

Escreva um programa que leia as seguintes informações:
1. O valor (em reais) inicialmente investido
2. A quantidade de meses da aplicação.

Como resultado, imprima repetidamente o saldo do investimento, mês a mês. Arredonde os
resultados com duas casas decimais, pois este problema envolve valores monetários.
"""

print("=== Calculadora de Investimento ===")

# Lê os dados de entrada
valor_inicial = float(input("Valor inicial investido (R$): "))
meses = int(input("Quantidade de meses da aplicação: "))

# Taxa de rendimento mensal (4%)
taxa_mensal = 0.04
saldo_atual = valor_inicial

print(f"\n=== Evolução do investimento ===")
print(f"Investimento inicial: R$ {valor_inicial:.2f}")
print(f"Taxa mensal: {taxa_mensal * 100}%")
print()

# Calcula e exibe o saldo mês a mês
for mes in range(1, meses + 1):
    # Aplica o rendimento mensal
    saldo_atual = saldo_atual * (1 + taxa_mensal)
    print(f"Mês {mes}: R$ {saldo_atual:.2f}")

print(f"\nValor final após {meses} meses: R$ {saldo_atual:.2f}")
print(f"Rendimento total: R$ {saldo_atual - valor_inicial:.2f}")
