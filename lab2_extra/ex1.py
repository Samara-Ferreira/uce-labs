# Exercício 1 - Cálculo do Imposto de Renda
# Escreva um programa que leia o salário mensal de um funcionário.
# Com base no valor, calcule e imprima o imposto de renda a ser pago, seguindo a tabela.

salario = float(input("Digite o salário mensal: R$ "))

# Fórmula: Imposto = (Salário × Alíquota) - Parcela a Deduzir

if salario <= 2259.20:
    # Até R$ 2.259,20 - Isento
    imposto = 0.00
elif salario <= 2826.65:
    # De R$ 2.259,21 até R$ 2.826,65 - 7,50% - Parcela a deduzir: R$ 169,44
    imposto = (salario * 0.075) - 169.44
elif salario <= 3751.05:
    # De R$ 2.826,66 até R$ 3.751,05 - 15% - Parcela a deduzir: R$ 381,44
    imposto = (salario * 0.15) - 381.44
elif salario <= 4664.68:
    # De R$ 3.751,06 até R$ 4.664,68 - 22,50% - Parcela a deduzir: R$ 662,77
    imposto = (salario * 0.225) - 662.77
else:
    # Acima de R$ 4.664,68 - 27,50% - Parcela a deduzir: R$ 896
    imposto = (salario * 0.275) - 896

# Como saída: Imprima o valor do imposto a ser pago, formatado com duas casas decimais
# Para salários isentos, imprima 0.00
print(f"{imposto:.2f}")
