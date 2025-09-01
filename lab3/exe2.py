'''
Exercício 2 – Maior ou menor?
Escreva um programa em Python que lê uma sequência de 10 números reais e imprime qual o
maior e qual o menor valor dessa sequência.
'''
for i in range(10):
    num = float(input("Digite um número real: "))
    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
            
        if num < menor:
            menor = num

print("Maior:", maior)
print("Menor:", menor)