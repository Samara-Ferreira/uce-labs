'''
Faça um programa em Python que mostre uma tabela de conversão de graus fahrenheit para
celsius para todos valores inteiros de n a m (n e m deverão ser digitados pelo usuário)
fahrenheit, mostrando o valor em fahrenheit e ao lado o valor em celsius.
A conversão de graus fahrenheit para celsius é obtida pela fórmula:
celsius = (fahrenheit - 32)*5/9
'''
n = int(input("Digite o valor de n: "))
m = int(input("Digite o valor de m: "))

if n > m:
    n, m = m, n

print("Fahrenheit\tCelsius")
for f in range(n, m + 1):
    c = (f - 32) * 5 / 9
    print(f"{f}\t\t{c:.2f}")