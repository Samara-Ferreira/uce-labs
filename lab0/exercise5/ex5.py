# Exercício 5 – Divisão inteira e resto da divisão
moedas_ouro_total = 50
guerreiros = 3

# Divisão inteira para saber quanto cada guerreiro recebe
moedas_por_guerreiro = moedas_ouro_total // guerreiros  # 16

# Resto da divisão para o informante
moedas_informante = moedas_ouro_total % guerreiros      # 2

print("Cada guerreiro receberá:", moedas_por_guerreiro, "moedas")
print("O informante receberá:", moedas_informante, "moedas")
