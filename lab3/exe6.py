'''
Escreva um programa em Python que imprime todos os números primos entre 1 e n (n
incluso), onde n é fornecido pelo usuário.
'''

n = int(input("Digite um número natural: "))

for num in range(2, n + 1):
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
    if primo:
        print(num, end=" ")