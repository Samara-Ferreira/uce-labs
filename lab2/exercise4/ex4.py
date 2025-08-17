# Exercício 4.a - Tem troco?
# Escreva um programa que leia dois números reais: preço e pagamento, nessa ordem.

preco = float(input("Digite o preço do produto: R$ "))
pagamento = float(input("Digite o valor do pagamento: R$ "))

# Se o preço for maior que o pagamento, então o programa deve imprimir "Falta X"
if preco > pagamento:
    falta = preco - pagamento
    print(f"Falta X {falta}")
# Caso contrário, o programa deve imprimir "Troco de Y"
else:
    troco = pagamento - preco
    print(f"Troco de {troco}")

print("\n" + "="*50 + "\n")

# Exercício 4.b - Consumo de combustível
# Escreva um programa que leia, nesta ordem:
# - o percurso de uma viagem (em quilômetros)
# - o tipo do carro (A ou B)

percurso = int(input("Digite o percurso da viagem (em km): "))
tipo_carro = input("Digite o tipo do carro (A ou B): ").strip().upper()

# Sabe-se que um carro tipo A faz 8 km com um litro de gasolina e um tipo B faz 12 km/l.
if tipo_carro == 'A':
    consumo = percurso / 8
else:  # tipo_carro == 'B'
    consumo = percurso / 12

# Como saída, informe o consumo estimado de combustível
print(f"{consumo:.2f}")

print("\n" + "="*50 + "\n")

# Exercício 4.c - Peso Ideal
# Faça um programa que leia as seguintes informações de uma pessoa, nesta ordem:
# - Altura (em metros)
# - Sexo (M ou F)

altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (M ou F): ").strip().upper()

# Como saída, determine o peso ideal, arredondado com até duas casas decimais
if sexo == 'M':
    # Para homens: (72.7 × altura) − 58
    peso_ideal = (72.7 * altura) - 58
else:  # sexo == 'F'
    # Para mulheres: (62.1 × altura) − 44.7
    peso_ideal = (62.1 * altura) - 44.7

print(f"{peso_ideal:.2f}")

print("\n" + "="*50 + "\n")

# Exercício 4.d - Desconto
# Para atrair mais clientes, uma loja de roupas oferece um desconto de 5% para quem faz
# compras de R$200,00 ou mais.

# Escreva um programa que leia o preço sem desconto de uma compra
preco_original = float(input("Digite o preço original da compra: R$ "))

# Aplica desconto de 5% se a compra for de R$200,00 ou mais
if preco_original >= 200.00:
    desconto = preco_original * 0.05
    valor_final = preco_original - desconto
else:
    valor_final = preco_original

# Como saída, imprima o valor a ser pago pelo cliente
# Resultados em moeda devem ser arredondados em duas casas decimais de precisão
print(f"{valor_final:.2f}")