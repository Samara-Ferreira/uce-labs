# Exercício 6 - O número do meio
# Escreva um programa que leia 3 números inteiros distintos.
# Como saída, imprima o número do meio, isto é, o número cujo valor está entre o maior e o menor número.

# Leitura dos 3 números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Encontrar o número do meio usando estruturas condicionais
if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    # num1 está no meio
    numero_meio = num1
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    # num2 está no meio
    numero_meio = num2
else:
    # num3 está no meio
    numero_meio = num3

print(numero_meio)
