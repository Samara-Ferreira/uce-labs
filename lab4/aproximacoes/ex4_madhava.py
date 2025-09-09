# Lê o número de termos
n = int(input("Digite o número de termos (n): "))

# Inicializa a soma da série
soma_serie = 0.0

# Calcula os n primeiros termos da série
for i in range(n):
    # Para o termo i:
    # Numerador: 1
    # Denominador: (2*i + 1) × 3^i
    denominador_parte1 = 2 * i + 1  # 1, 3, 5, 7, ...
    denominador_parte2 = 3 ** i  # 3^0, 3^1, 3^2, 3^3, ...

    denominador_total = denominador_parte1 * denominador_parte2

    # Calcula o termo da série
    termo = 1.0 / denominador_total

    # Alterna o sinal: positivo para i par, negativo para i ímpar
    if i % 2 == 0:
        soma_serie += termo
    else:
        soma_serie -= termo

# Calcula π = √12 × soma_serie
import math

pi_aproximado = math.sqrt(12) * soma_serie

# Exibe o resultado com 8 casas decimais
print(f"π aproximado com {n} termos: {pi_aproximado:.8f}")
