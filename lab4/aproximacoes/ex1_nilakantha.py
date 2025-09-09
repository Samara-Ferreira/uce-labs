
# Lê o número de termos
n = int(input("Digite o número de termos (n): "))

# Inicializa π
pi_aproximado = 0.0

# O primeiro termo é 3, depois vêm as frações
if n >= 1:
    pi_aproximado = 3.0  # Primeiro termo
    
    # Calcula os termos adicionais (frações)
    for i in range(n - 1):
        # Para o termo i, os denominadores são: (2+2*i), (3+2*i), (4+2*i)
        denominador1 = 2 + 2 * i
        denominador2 = 3 + 2 * i
        denominador3 = 4 + 2 * i
        
        # Calcula o produto dos denominadores
        produto_denominadores = denominador1 * denominador2 * denominador3
        
        # Calcula o termo da série: 4 / produto_denominadores
        termo = 4.0 / produto_denominadores
        
        # Alterna o sinal: positivo para i par, negativo para i ímpar
        if i % 2 == 0:
            pi_aproximado += termo
        else:
            pi_aproximado -= termo

# Exibe o resultado com 8 casas decimais
print(f"π aproximado com {n} termos: {pi_aproximado:.8f}")
