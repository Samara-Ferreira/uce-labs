import random

# Gerar 10 notas aleatórias entre 0 e 100
notas = [round(random.uniform(0, 100), 1) for _ in range(10)]

# Função para calcular a média
def calcular_media(lista_notas):
    return sum(lista_notas) / len(lista_notas)

# Função para encontrar a maior nota
def encontrar_maior_nota(lista_notas):
    maior = lista_notas[0]
    for nota in lista_notas:
        if nota > maior:
            maior = nota
    return maior

# Função para encontrar a menor nota
def encontrar_menor_nota(lista_notas):
    menor = lista_notas[0]
    for nota in lista_notas:
        if nota < menor:
            menor = nota
    return menor

# Função para exibir o resumo
def mostrar_resumo(lista_notas):
    print("Notas da turma:", lista_notas)
    print(f"Média da turma: {calcular_media(lista_notas):.2f}")
    print(f"Maior nota: {encontrar_maior_nota(lista_notas)}")
    print(f"Menor nota: {encontrar_menor_nota(lista_notas)}")

# Programa principal
mostrar_resumo(notas)
