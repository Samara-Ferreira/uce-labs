'''
Escreva um programa em Python que leia as 10 notas de uma avaliação dos alunos que
cursam uma disciplina de algoritmos, calcule e imprima na tela (nesta ordem):
● A quantidade de notas maiores ou iguais a 7;
● A quantidade de notas maiores ou iguais a 3 e menores que 7;
● A quantidade de notas menores que 3;
● A média da turma na avaliação.
'''
acima_sete = 0
entre_tres_e_sete = 0
abaixo_tres = 0
soma = 0
for i in range(10):
    nota = float(input("Digite a nota do aluno {}: ".format(i + 1)))
    if nota >= 7:
        acima_sete += 1
    elif nota >= 3:
        entre_tres_e_sete += 1
    else:
        abaixo_tres += 1
    soma += nota

media = soma / 10
print("Quantidade de notas maiores ou iguais a 7:", acima_sete)
print("Quantidade de notas maiores ou iguais a 3 e menores que 7:", entre_tres_e_sete)
print("Quantidade de notas menores que 3:", abaixo_tres)
print("Média da turma:", round(media, 1))