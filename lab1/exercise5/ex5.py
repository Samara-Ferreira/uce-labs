# Exercício 5 – Custo da pintura de um muro

# Leitura do valor do serviço por m²
valor_m2 = float(input("Digite o custo do serviço de pintura por m²: "))

# Dados fixos do muro
comprimento = 12
altura = 3
custo_fixo = 100

# Cálculo da área
area = comprimento * altura

# Cálculo do custo total
custo_total = (valor_m2 * area) + custo_fixo

# Saída
print(custo_total)