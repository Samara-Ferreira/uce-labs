# Exercício 9 - E aí, passou?
# Programa que leia a média parcial de 10 alunos, e escreva a fala a 
# situação de cada um "APROVADO" se NF = > 7; "FINAL" se 3 <= NF < 7; "REPROVADO" se 
# NF < 3.

print("Sistema de Avaliação de Alunos")
print("Digite as médias parciais dos 10 alunos:")

for i in range(10):
    media = float(input())
    
    if media >= 7:
        situacao = "APROVADO"
    elif media >= 3:
        situacao = "FINAL"
    else:
        situacao = "REPROVADO"
    
    print(situacao)
