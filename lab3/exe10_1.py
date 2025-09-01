'''
Escreva um programa em Python que leia o salário de uma pessoa, a quantidade de contas
(despesas) que uma pessoa precisa pagar em um mês e, para cada conta, leia o valor a ser
pago.
O programa deve somar todos os valores de contas que a pessoa necessita pagar e depois
verificar se a diferença entre o salário da e o valor de todas as despesas que deve pagar no
mês é positiva.
● Se a diferença (salário – despesas) for positiva, imprima: “Parabéns! Este mês você
economizou x reais”, onde x é a diferença.
● Se a diferença for negativa, imprima a mensagem “Você precisa reduzir suas despesas
em x reais”, onde x é a diferença absoluta entre salário e despesas.

'''

salario = float(input("Digite o salário da pessoa: "))

qtde_contas = int(input("Digite a quantidade de contas (despesas) que a pessoa precisa pagar no mês: "))

despesas = 0

for i in range(qtde_contas):
    valor_conta = float(input("Digite o valor da conta {}: ".format(i + 1)))
    despesas += valor_conta

diferenca = salario - despesas

if diferenca > 0:
    print("Parabéns! Este mês você economizou {} reais".format(diferenca))
else:
    print("Você precisa reduzir suas despesas em {} reais".format(abs(diferenca)))
