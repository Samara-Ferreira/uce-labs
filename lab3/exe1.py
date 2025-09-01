'''
Exercício 1 – Múltiplos de 7
Faça um programa em Python que solicite dois números naturais e exiba os múltiplos de 7
existentes entre estes números (não inclui os números informados). Imprima os múltiplos em
uma única linha e com 1 espaço entre eles.
'''
n1 = int(input("Digite o primeiro número natural: "))
n2 = int(input("Digite o segundo número natural: "))

if n1 > n2:
    n1, n2 = n2, n1

for i in range(n1 + 1, n2):
    if i % 7 == 0:
        print(i, end=" ")