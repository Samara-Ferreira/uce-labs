# Exercício 1 – Cálculo de Médias Escolares
# Objetivo: Compreender o uso de listas, acesso de índices, inserção e remoção de elementos

# Entrada de Dados
qtd_alunos = int(input("Digite a quantidade de alunos na turma: "))
notas_p1 = []
notas_p2 = []
notas_p3 = []

for i in range(qtd_alunos):
    nota1 = float(input(f"Digite a nota P1 do aluno {i+1}: "))
    nota2 = float(input(f"Digite a nota P2 do aluno {i+1}: "))
    nota3 = float(input(f"Digite a nota P3 do aluno {i+1}: "))
    notas_p1.append(nota1)
    notas_p2.append(nota2)
    notas_p3.append(nota3)

# Processamento e Saída
for i in range(qtd_alunos):
    media = (notas_p1[i] + notas_p2[i] + notas_p3[i]) / 3
    if media >= 7:
        situacao = "Aprovado"
    elif media < 3:
        situacao = "Reprovado"
    else:
        situacao = "Prova Final"
    print(f"Aluno {i+1}: Média = {media:.2f} - Situação: {situacao}")
