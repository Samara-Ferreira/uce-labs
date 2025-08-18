'''
Escreva um programa que leia dois números inteiros.
Como saída:
● Se o produto dos dois números for par, imprima a soma deles.
● Caso contrário, ou seja, se for ímpar, imprima a diferença do segundo pelo primeiro
número
'''
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
produto = num1 * num2
if produto % 2 == 0:
    print("A soma dos números é:", num1 + num2)
else:
    print("A diferença do segundo pelo primeiro é:", num2 - num1)