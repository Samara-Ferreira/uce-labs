"""
Exercício 4 - Crescimento populacional

Escreva um programa que receba como entradas as seguintes grandezas:
• Número de habitantes de uma cidade A
• Número de habitantes de uma cidade B
• Percentual de crescimento populacional da cidade A
• Percentual de crescimento populacional da cidade B

O programa deverá determinar o número de anos necessários para que a população da
cidade A iguale ou ultrapasse a população da cidade B, mantidos os percentuais de
crescimento.
"""

print("=== Crescimento Populacional ===")

# Lê os dados de entrada
habitantes_a = int(input("Número de habitantes da cidade A: "))
habitantes_b = int(input("Número de habitantes da cidade B: "))
crescimento_a = float(input("Percentual de crescimento da cidade A (%): "))
crescimento_b = float(input("Percentual de crescimento da cidade B (%): "))

# Converte percentuais para decimais
taxa_a = crescimento_a / 100
taxa_b = crescimento_b / 100

anos = 0

# Verifica se a cidade A já tem população maior ou igual
if habitantes_a >= habitantes_b:
    print("A cidade A já possui população maior ou igual à cidade B.")
    print(f"Anos necessários: {anos}")
else:
    # Simula o crescimento ano a ano
    populacao_a = habitantes_a
    populacao_b = habitantes_b
    
    while populacao_a < populacao_b:
        anos += 1
        # Aplica o crescimento às populações
        populacao_a += populacao_a * taxa_a
        populacao_b += populacao_b * taxa_b
    
    print(f"Anos necessários: {anos}")
    print(f"População final da cidade A: {int(populacao_a)}")
    print(f"População final da cidade B: {int(populacao_b)}")
