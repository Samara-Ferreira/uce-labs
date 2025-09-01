'''
Escreva um programa em Python que imprime a soma de todos os números inteiros entre A e
B (incluindo A e B), onde A e B são fornecidos pelo usuário.
'''
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if A > B:
    A, B = B, A

soma = 0
for i in range(A, B + 1):
    soma += i
print("A soma dos números inteiros entre", A, "e", B, "é:", soma)