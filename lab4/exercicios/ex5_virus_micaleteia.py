"""
Exercício 5 - O vírus de Micaleteia

Micaleteia foi infectada por um vírus raro, mas já está sendo tratada. Quando a quantidade
de células de defesa (leucócitos) no dobro da quantidade de vírus, ela estará totalmente
curada.

Escreva um programa que leia as seguintes informações:
• Quantidade inicial de cópias do vírus no sangue de Micaleteia.
• Quantidade inicial de leucócitos no sangue.
• Percentual de multiplicação diária do vírus.
• Percentual de multiplicação diária dos leucócitos.

Como saída, determine quantos dias Micaleteia levará para ser curada.
"""

print("=== Simulação do Vírus de Micaleteia ===")

# Lê os dados iniciais
virus_inicial = int(input("Quantidade inicial de vírus: "))
leucocitos_inicial = int(input("Quantidade inicial de leucócitos: "))
multiplicacao_virus = float(input("Percentual de multiplicação diária do vírus (%): "))
multiplicacao_leucocitos = float(input("Percentual de multiplicação diária dos leucócitos (%): "))

# Converte percentuais para decimais
taxa_virus = multiplicacao_virus / 100
taxa_leucocitos = multiplicacao_leucocitos / 100

# Inicializa as quantidades atuais
virus_atual = virus_inicial
leucocitos_atual = leucocitos_inicial
dias = 0

print("\n=== Evolução diária ===")
print(f"Dia {dias}: Vírus = {virus_atual}, Leucócitos = {leucocitos_atual}")

# Simula dia a dia até a cura
while leucocitos_atual < 2 * virus_atual:
    dias += 1
    
    # Aplica a multiplicação diária
    virus_atual = int(virus_atual * (1 + taxa_virus))
    leucocitos_atual = int(leucocitos_atual * (1 + taxa_leucocitos))
    
    print(f"Dia {dias}: Vírus = {virus_atual}, Leucócitos = {leucocitos_atual}")

print(f"\nMicaleteia será curada em {dias} dias!")
print(f"Condição de cura: Leucócitos ({leucocitos_atual}) >= 2 × Vírus ({2 * virus_atual})")
