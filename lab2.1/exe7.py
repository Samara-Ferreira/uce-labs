# Programa para calcular risco de problemas cardíacos baseado em IMC e idade

# Entrada de dados
idade = int(input("Digite a idade: "))
imc = float(input("Digite o IMC: "))

# Validação de dados
if idade <= 0 or idade > 130 or imc <= 0:
    print(f"Entradas: {idade} anos e IMC {imc}")
    print("Dados inválidos")
else:
    # Determinação do risco
    if imc < 22.0 and idade < 45:
        risco = "Baixo"
    elif imc < 22.0 and idade >= 45:
        risco = "Médio"
    elif imc >= 22.0 and idade < 45:
        risco = "Médio"
    else:  # imc >= 22.0 and idade >= 45
        risco = "Alto"

    # Saída
    print(f"Entradas: {idade} anos e IMC {imc}")
    print(f"Risco: {risco}")
