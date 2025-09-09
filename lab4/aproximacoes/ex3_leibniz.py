
# Lê o número de termos
n = int(input("Digite o número de termos (n): "))

# Inicializa π aproximado
pi_aproximado = 0.0

# Calcula os n primeiros termos da série
for i in range(n):
    # Para o termo i, o denominador é (2*i + 1)
    denominador = 2 * i + 1
    
    # Calcula o termo da série: 4 / denominador
    termo = 4.0 / denominador
    
    # Alterna o sinal: positivo para i par, negativo para i ímpar
    if i % 2 == 0:
        pi_aproximado += termo
    else:
        pi_aproximado -= termo

# Exibe o resultado com 8 casas decimais
print(f"π aproximado com {n} termos: {pi_aproximado:.8f}")
