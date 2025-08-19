# Exercício 5 - Tarifa de Transporte por App
# Escreva um programa que calcule o preço de uma corrida de aplicativo. O programa deve ler:

# 1. A distância da viagem em quilômetros
distancia = float(input("Digite a distância da viagem (km): "))

# 2. A categoria do carro ("Basic" ou "Premium")
categoria = input("Digite a categoria do carro (Basic ou Premium): ").strip()

# 3. A hora do dia (formato 24h, apenas a hora como inteiro, de 0 a 23)
hora = int(input("Digite a hora do dia (0 a 23): "))

# Regras de cálculo:
# Taxa base: R$ 4.50 (fixa para toda corrida)
taxa_base = 4.50

# Custo por quilômetro:
if categoria == "Basic":
    custo_por_km = 1.50  # Categoria "Basic": R$ 1.50 por km
else:  # categoria == "Premium"
    custo_por_km = 2.20  # Categoria "Premium": R$ 2.20 por km

# Calcular custo básico (taxa base + custo por km)
custo_basico = taxa_base + (distancia * custo_por_km)

# Multiplicador de horário de pico:
# O horário de pico é das 7h às 9h e das 17h às 19h (inclusive)
# Durante o horário de pico, o custo total é multiplicado por 1.3
if (hora >= 7 and hora <= 9) or (hora >= 17 and hora <= 19):
    # Horário de pico
    valor_final = custo_basico * 1.3
else:
    # Horário normal
    valor_final = custo_basico

# Como saída: Imprima o valor final da corrida, formatado com duas casas decimais
print(f"{valor_final:.2f}")