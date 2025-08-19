# Exercício 3 - Diagnóstico de Média Escolar
# Escreva um programa que leia as duas notas de um aluno (de 0 a 10) e sua
# frequência em porcentagem (de 0 a 100).

# Leitura das entradas
nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))
frequencia = float(input("Digite a frequência em porcentagem (0 a 100): "))

# Regras de avaliação:
# 1. Se a frequência for menor que 75%, o aluno está automaticamente reprovado por falta
if frequencia < 75:
    print("Reprovado por Falta")
else:
    # 2. Caso a frequência seja suficiente, calcule a média das notas
    media = (nota1 + nota2) / 2
    
    # Verificar a situação do aluno baseada na média:
    if media >= 7.0:
        # Se a média for 7.0 ou superior, o aluno está aprovado
        print("Aprovado")
    elif media < 3.0:
        # Se a média for menor que 3.0, o aluno está reprovado por média
        print("Reprovado por Média")
    else:
        # Se a média estiver entre 3.0 e 6.9 (inclusive), o aluno irá para o exame final
        print("Exame Final")