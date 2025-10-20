# 1. Definir a matriz de entrada
matriz_horas = [
    [2, 4, 3, 4, 5, 8, 8],
    [7, 3, 4, 3, 3, 4, 4],
    [3, 3, 4, 3, 3, 2, 2],
    [9, 3, 4, 7, 3, 4, 1]
]

vetor_totais = []

num_funcionarios = len(matriz_horas)

num_dias = len(matriz_horas[0])

for i in range(num_funcionarios):
    soma_semanal = 0
    for j in range(num_dias):
        soma_semanal += matriz_horas[i][j]
    vetor_totais.append(soma_semanal)

print(vetor_totais)