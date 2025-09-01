'''
Uma fábrica tem um vendedor que recebe uma comissão calculada a partir do número de itens
de um pedido, segundo os seguintes critérios:
● Para pedidos com menos de 5 itens, a comissão é de 10% do valor total do pedido;
● Para pedidos de 5 a 9 itens, a comissão é de 15% do valor total do pedido;
● Para pedidos de 10 a 12 itens, a comissão é de 20% do valor total do pedido;
● Para pedidos iguais ou superiores a 13 itens, a comissão é de 25%.
Escreva um programa em Python que processe n pedidos vinculados a esse vendedor (n deve
ser lido, portanto). Para cada pedido, o programa deve ler a quantidade de itens vendidos e o
valor total.
O programa deve informar:
● A soma total das comissões;
● A média de itens vendidos;
● Porcentagem de pedidos com menos de 10 itens.
'''

n = int(input("Digite a quantidade de pedidos: "))

soma_comissoes = 0
soma_itens = 0
pedidos_menos_10 = 0

for i in range(n):
    itens_vendidos = int(input("Digite a quantidade de itens vendidos no pedido {}: ".format(i + 1)))
    valor_total = float(input("Digite o valor total do pedido {}: ".format(i + 1)))

    soma_itens += itens_vendidos

    if itens_vendidos < 5:
        comissao = valor_total * 0.1
    elif itens_vendidos < 10:
        comissao = valor_total * 0.15
    elif itens_vendidos < 13:
        comissao = valor_total * 0.2
    else:
        comissao = valor_total * 0.25

    soma_comissoes += comissao

    if itens_vendidos < 10:
        pedidos_menos_10 += 1

media_itens = soma_itens / n

porcentagem_menos_10 = (pedidos_menos_10 / n) * 100

print("Soma total das comissões: {}".format(soma_comissoes))
print("Média de itens vendidos: {}".format(media_itens))
print("Porcentagem de pedidos com menos de 10 itens: {}".format(porcentagem_menos_10))