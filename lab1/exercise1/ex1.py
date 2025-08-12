# Exercício 1 – Custo da pintura de uma fachada

# Leitura dos dados
altura = float(input("Digite a altura da fachada (em metros): "))
comprimento = float(input("Digite o comprimento da fachada (em metros): "))
valor_m2 = float(input("Digite o valor do serviço de pintura por m²: "))

# Cálculo da área
area = altura * comprimento

# Cálculo do custo total
custo_total = area * valor_m2

# Saída
print(f"O custo total da pintura da fachada é: {custo_total}")