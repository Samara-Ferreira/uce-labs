'''
Escreva um programa que leia dois números reais: preço e pagamento, nessa ordem.
● Se o preço for maior que o pagamento, então o programa deve imprimir “Falta X”, onde
X é a diferença a ser paga.
● Caso contrário, o programa deve imprimir “Troco de Y”, onde Y é o valor a ser
devolvido pelo comerciante ao comprador, que pode ser zero.
'''

preco = float(input("Digite o preço: "))
pagamento = float(input("Digite o valor do pagamento: "))

if preco > pagamento:
    print(f"Falta {preco - pagamento:.2f}")
else:
    print(f"Troco de {pagamento - preco:.2f}")

'''
Escreva um programa que leia, nesta ordem:
● o percurso de uma viagem (em quilômetros)
● o tipo do carro (A ou B)
Sabe-se que um carro tipo A faz 8 km com um litro de gasolina e um tipo B faz 12 km/l.
Como saída, informe o consumo estimado de combustível
'''

percurso = float(input("Digite o percurso da viagem (em km): "))
tipo_carro = input("Digite o tipo do carro (A ou B): ").strip().upper()

if tipo_carro == "A":
    consumo = percurso / 8
    print(f"Consumo estimado de combustível: {consumo:.1f} litros")
elif tipo_carro == "B":
    consumo = percurso / 12
    print(f"Consumo estimado de combustível: {consumo:.1f} litros")
else:
    print("Tipo de carro inválido. Por favor, digite 'A' ou 'B'.")
