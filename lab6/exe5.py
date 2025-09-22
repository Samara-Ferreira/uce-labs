# Lista de salas do calabouço
salas = ["Entrada", "Sala do Tesouro", "Sala dos Monstros", "Biblioteca Secreta", "Câmara Misteriosa"]

# Lista para rastrear salas visitadas
salas_visitadas = []

# Começamos na primeira sala
salas_visitadas.append(salas[0])

# Variável de controle do loop
continuar = True

while continuar:
    # Mostrar sala atual
    sala_atual = salas_visitadas[-1]
    print(f"\nVocê está na sala: {sala_atual}")

    # Opções para o jogador
    print("Salas disponíveis para explorar:")
    for i, sala in enumerate(salas):
        print(f"{i + 1}. {sala}")
    print("0. Voltar para a sala anterior / Sair do jogo")

    # Receber escolha do jogador
    escolha = input("Escolha a próxima sala (número): ")

    # Validar entrada
    if not escolha.isdigit():
        print("Escolha inválida! Digite um número.")
        continue

    escolha = int(escolha)

    if escolha == 0:
        # Voltar para a sala anterior
        if len(salas_visitadas) > 1:
            salas_visitadas.pop()
            print("Você voltou para a sala anterior.")
        else:
            print("Você está na entrada. Encerrando exploração.")
            continuar = False  # muda a variável para encerrar o loop
    elif 1 <= escolha <= len(salas):
        nova_sala = salas[escolha - 1]
        salas_visitadas.append(nova_sala)
        print(f"Você entrou na sala: {nova_sala}")
    else:
        print("Escolha inválida! Tente novamente.")

# Resumo da exploração
print("\nResumo da exploração:")
for i, sala in enumerate(salas_visitadas, start=1):
    print(f"{i}. {sala}")
