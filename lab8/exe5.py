def cadastrar_filmes(qtd=10):
    filmes = {}
    for _ in range(qtd):
        nome = input("Nome do filme: ")
        duracao = int(input("Duração (min): "))
        filmes[nome] = duracao
    return filmes

def calcular_tempo_total(filmes, qtd=3):
    total = 0
    for _ in range(qtd):
        nome_filme = input("Filme a assistir: ")
        total += filmes.get(nome_filme, 0)
    return total

def exercicio5():
    filmes = cadastrar_filmes()
    tempo = calcular_tempo_total(filmes)
    print(f"Tempo total: {tempo} minutos")
exercicio5()