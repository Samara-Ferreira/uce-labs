# Exercício 10.1 - Controle de gastos
# Escreva um programa em Python que leia o salário de uma pessoa, a quantidade de contas
# (despesas) que uma pessoa precisa pagar em um mês e, para cada conta, leia o valor a ser
# pago.

# O programa deve somar todos os valores de contas que a pessoa necessita pagar e depois
# verificar se a diferença entre o salário de o valor das despesas será positiva ou não
# mais é positiva.
# • Se a diferença for positiva, imprimir "Parabéns! Este mês você
#   conseguiu economizar R$ [valor da economia]."
# • Se a diferença for negativa, imprimir a mensagem "Você precisa reduzir suas despesas
#   em R$ [valor]", onde o valor é a diferença absoluta entre salário e despesas.

print("=== Controle de Gastos ===")
salario = float(input())

# Lendo despesas
total_despesas = 0
while True:
    valor = float(input())
    if valor == 0:
        break
    total_despesas += valor

# Calculando a diferença
diferenca = salario - total_despesas

# Verificando resultado
if diferenca > 0:
    print(f"Você precisa reduzir suas despesas em {diferenca:.2f} reais")
else:
    print(f"Você precisa reduzir suas despesas em {abs(diferenca):.2f} reais")