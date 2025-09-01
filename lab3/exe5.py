'''
Faça um programa em Python que leia 10 números reais, um de cada vez (ou seja, um por
linha), e conte quantos são positivos, a soma dos números negativos, e a média de todos
os valores.
● A soma dos números negativos e a média de todos os valores devem ser exibidas com
uma casa decimal.

'''

positivos = 0
soma_negativos = 0
soma_total = 0

for i in range(10):
    num = float(input("Digite um número real: "))
    if num > 0:
        positivos += 1
    else:
        soma_negativos += num
    soma_total += num

media = soma_total / 10

print("Quantidade de positivos:", positivos)
print("Soma dos negativos: {:.1f}".format(soma_negativos))
print("Média dos valores: {:.1f}".format(media))