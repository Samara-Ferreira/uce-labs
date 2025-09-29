import random

# Entrada dos nomes dos jogadores
jogadores = input("Digite os nomes dos jogadores separados por vírgula: ").split(",")

# Remove espaços extras e padroniza os nomes
jogadores = [jogador.strip() for jogador in jogadores]

# Embaralha a lista de jogadores
random.shuffle(jogadores)

# Divide a lista em duas metades
metade = len(jogadores) // 2
time_a = jogadores[:metade]
time_b = jogadores[metade:]

# Exibe os times
print("\nTime A:")
for jogador in time_a:
    print(jogador)

print("\nTime B:")
for jogador in time_b:
    print(jogador)
