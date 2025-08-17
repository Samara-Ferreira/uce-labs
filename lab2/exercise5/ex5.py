# Exercício 5 - Propriedade de um número
# Escreva um programa que leia um número inteiro n de 03 dígitos, no intervalo 100 < n ≤ 999

n = int(input("Digite um número inteiro de 3 dígitos (100 < n ≤ 999): "))

# Propriedade: Se o dígito da esquerda for removido, o número restante é divisor do número original.

# Extrair o dígito da esquerda (centena)
digito_esquerda = n // 100

# Extrair o número restante (dezena e unidade)
numero_restante = n % 100

# Verificar a propriedade: o número restante deve ser divisor do número original
# E o número restante deve ser diferente de zero para evitar divisão por zero
if numero_restante != 0 and n % numero_restante == 0:
    print("SIM")
else:
    print("NAO")