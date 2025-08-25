# Exercício 10 – IMC com validação de entrada

# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Validação de entrada
if peso <= 0 or altura <= 0:
    print("Entradas inválidas")
else:
    # Cálculo do IMC
    imc = peso / (altura ** 2)

    # Classificação de acordo com a OMS
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade grau 1"
    elif imc < 40:
        classificacao = "Obesidade grau 2 (severa)"
    else:
        classificacao = "Obesidade grau 3 (mórbida)"

    # Saída
    print(f"IMC = {imc:.2f}")
    print(f"Classificação: {classificacao}")
