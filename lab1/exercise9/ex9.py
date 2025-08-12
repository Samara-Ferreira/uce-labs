import math

# Leitura dos pontos de vida iniciais e dos dados
vida_inicial = int(input("Digite os pontos de vida iniciais do monstro: "))
d1 = int(input("Digite o valor do primeiro dado (D1): "))
d2 = int(input("Digite o valor do segundo dado (D2): "))

# Cálculo do dano conforme a fórmula correta
dano = math.floor(math.sqrt(5 * d1) + math.pi ** (d2 / 3))

# Pontos de vida restantes
vida_restante = vida_inicial - dano

# Saída
print(vida_restante)