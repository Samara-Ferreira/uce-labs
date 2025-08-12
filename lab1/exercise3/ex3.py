# Exercício 3 – Caixa Eletrônico

# Leitura do valor a sacar
valor = int(input("Digite o valor que deseja sacar (par e maior que zero): "))

# Cálculo das notas
notas_50 = valor // 50
valor = valor % 50

notas_10 = valor // 10
valor = valor % 10

notas_2 = valor // 2

# Saída
print(notas_50)
print(notas_10)
print(notas_2)