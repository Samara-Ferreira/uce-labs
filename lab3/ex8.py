# Exercício 8 - A média é 7
# Escreva um programa em Python que leia as 10 notas de uma avaliação dos alunos que
# cursam uma disciplina de algoritmos, calcule e imprima na tela nesta ordem:
# • A quantidade de notas maiores ou iguais a 7;
# • A quantidade de notas menores que 7;
# • A quantidade de notas menores que 5;
# • A média da turma na avaliação.

# Variáveis contadoras
notas_maiores_igual_7 = 0
notas_menores_7 = 0
notas_menores_5 = 0
soma_notas = 0

# Ler as 10 notas
for i in range(10):
    nota = float(input())
    
    # Somar para calcular a média
    soma_notas += nota
    
    # Contar as categorias
    if nota >= 7:
        notas_maiores_igual_7 += 1
    
    if nota < 7:
        notas_menores_7 += 1
        
    if nota < 5:
        notas_menores_5 += 1

# Calcular a média
media = soma_notas / 10

# Imprimir os resultados na ordem solicitada
print(notas_maiores_igual_7)
print(notas_menores_7)
print(notas_menores_5)
print(f"{media:.1f}")
