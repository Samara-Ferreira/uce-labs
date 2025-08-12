# Exercício 18 – Contador de segundos

# Lê o número de segundos
N = int(input("Digite o número de segundos: "))

# Converte segundos para horas, minutos e segundos
horas = N // 3600        # 1 hora = 3600 segundos
minutos = (N % 3600) // 60  # Resto da divisão por 3600, dividido por 60
segundos = N % 60        # Resto da divisão por 60

# Imprime o resultado no formato "Xh Ym Zs"
print(f"{horas}h {minutos}m {segundos}s")
