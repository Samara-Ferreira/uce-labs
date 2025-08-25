
'''
Escreva um programa que determine o valor total a ser pago pela conta de energia elétrica,
com base nas seguintes entradas:
1. O consumo de energia (em kWh); e
2. O tipo de instalação (R para residências, I para indústrias, e C para comércios).
Como saída :
1. Valor total da conta de energia elétrica arredondado para duas casas decimais, caso
os dados sejam válidos OU a mensagem "Dados inválidos" caso os dados sejam
inválidos. Os dados são inválidos quando o consumo é negativo ou o tipo de
instalação é diferente das letras R, I ou C.
'''
consumo = float(input("Digite o consumo em kWh: "))
tipo = input("Digite o tipo de instalação (R, I ou C): ")

print(f"Entradas: {consumo} e tipo {tipo}")

if (consumo < 0) or (tipo != 'R' and tipo != 'I' and tipo != 'C'):
    print("Dados inválidos")
else:
    if tipo == 'R':
        preco = 0.44 if consumo <= 500 else 0.65
    elif tipo == 'I':
        preco = 0.55 if consumo <= 1000 else 0.60
    else:
        preco = 0.55 if consumo <= 5000 else 0.60

    valor = consumo * preco
    print("O valor a ser pago é: R$", round(valor, 2))