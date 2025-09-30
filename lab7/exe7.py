import random

# Número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)

print("Bem-vindo ao jogo 'Adivinhe o Número'!")
print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

while True:
    try:
        palpite = int(input("Digite seu palpite: "))

        if palpite < numero_secreto:
            print("Mais alto!")
        elif palpite > numero_secreto:
            print("Mais baixo!")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto}!")
            break  # Sai do loop quando o jogador acerta
    except ValueError:
        print("Por favor, digite um número válido.")
