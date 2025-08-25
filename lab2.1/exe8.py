# Programa para calcular gratificação do funcionário do ano

# Entrada de dados
horas_extras = float(input("Digite o número de horas extras: "))
horas_faltas = float(input("Digite o número de horas de faltas: "))

# Cálculo do índice H
H = horas_extras - (1/4) * horas_faltas

# Determinação da gratificação
if H > 400:
    gratificacao = 500
else:
    gratificacao = 100

# Saída
print(f"E extras {horas_extras} e F de falta {horas_faltas}")
print(f"R$ {gratificacao}")
