# Exercício 4 - Classificação de Triângulos
# Escreva um programa que leia três valores reais (A, B e C).

# Leitura dos três lados do triângulo
A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))

# Primeiro, verificar se os valores podem formar um triângulo
# A condição de existência de um triângulo é que a soma de quaisquer dois lados
# seja sempre maior que o terceiro lado
if (A + B > C) and (A + C > B) and (B + C > A):
    # Se forma um triângulo, classificar o tipo:
    
    if A == B == C:
        # Três lados iguais = Equilátero
        print("Equilatero")
    elif A == B or A == C or B == C:
        # Dois lados iguais = Isósceles
        print("Isosceles")
    else:
        # Todos os lados diferentes = Escaleno
        print("Escaleno")
else:
    # Se não forma um triângulo
    print("Nao forma um triangulo")