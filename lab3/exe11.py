'''
Escreva um programa em Python que leia n números inteiros positivos fornecidos e imprima na
tela uma mensagem informando se o número é ou não perfeito.
Obs.: Número perfeito é aquele cuja soma de seus divisores, exceto ele próprio, é igual ao
número
'''

n = int(input("Quantos números você quer verificar? "))

for _ in range(n):
    num = int(input("Digite um número inteiro positivo: "))
    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    if soma_divisores == num:
        print(f"O número {num} é perfeito.")
    else:
        print(f"O número {num} não é perfeito.")