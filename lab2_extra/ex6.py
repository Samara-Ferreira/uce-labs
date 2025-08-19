# Exercício 6 - Jogo "Pedra, Papel e Tesoura"
# Escreva um programa que leia a jogada de dois jogadores.
# As entradas serão as strings "pedra", "papel" ou "tesoura".

# Leitura das jogadas dos dois jogadores
jogador1 = input("Jogada do jogador 1: ").strip().lower()
jogador2 = input("Jogada do jogador 2: ").strip().lower()

# Regras do jogo:
# • Tesoura corta papel;
# • Papel cobre pedra;
# • Pedra quebra tesoura.

# Verificar o resultado do jogo
if jogador1 == jogador2:
    # Jogadas iguais = Empate
    print("Empate")
elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
     (jogador1 == "papel" and jogador2 == "pedra") or \
     (jogador1 == "tesoura" and jogador2 == "papel"):
    # Jogador 1 vence
    print("Jogador 1 venceu")
else:
    # Jogador 2 vence (todas as outras combinações)
    print("Jogador 2 venceu")