
# Lê o ângulo em radianos
x = float(input("Digite o ângulo x (em radianos): "))

# Lê o número de termos
k = int(input("Digite o número k de termos da série: "))

# Inicializa o seno aproximado
seno_aproximado = 0.0

# Calcula os k primeiros termos da série
for i in range(k):
    # Para o termo i: x^(2*i+1) / (2*i+1)!
    expoente = 2 * i + 1
    
    # Calcula x^expoente
    x_elevado = x ** expoente
    
    # Calcula o fatorial de (2*i+1)
    fatorial = 1
    for j in range(1, expoente + 1):
        fatorial *= j
    
    # Calcula o termo da série
    termo = x_elevado / fatorial
    
    # Alterna o sinal: positivo para i par, negativo para i ímpar
    if i % 2 == 0:
        seno_aproximado += termo
    else:
        seno_aproximado -= termo

# Exibe o resultado com 10 casas decimais
print(f"sen({x}) aproximado com {k} termos: {seno_aproximado:.10f}")