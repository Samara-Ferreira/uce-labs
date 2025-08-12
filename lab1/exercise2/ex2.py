# Exercício 2 – Outro Caixa Eletrônico

# Leitura do valor a sacar
valor = int(input("Digite o valor que deseja sacar (múltiplo de 10): "))

# Cálculo das notas
notas_100 = valor // 100
valor = valor % 100

notas_50 = valor // 50
valor = valor % 50

notas_10 = valor // 10

# Saída
print(f"Notas de R$100: {notas_100}")
print(f"Notas de R$50: {notas_50}")
print(f"Notas de R$10: {notas_10}")