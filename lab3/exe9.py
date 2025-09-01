'''
Escreva um programa em Python que leia a média parcial de 10 alunos, e escreva na tela a
situação de cada um. “APROVADO” se NF >= 7; “FINAL” se 3 <= NF < 7; “REPROVADO” se
NF < 3.
'''

for i in range(10):
    media_parcial = float(input("Digite a média parcial do aluno {}: ".format(i + 1)))
    if media_parcial >= 7:
        situacao = "APROVADO"
    elif media_parcial >= 3:
        situacao = "FINAL"
    else:
        situacao = "REPROVADO"
    print("Aluno {}: {}".format(i + 1, situacao))