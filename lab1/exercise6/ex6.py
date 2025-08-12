# Exercício 6 – Soma dos dígitos de um número inteiro

# Leitura do número inteiro de quatro dígitos
numero = input("Digite um número inteiro de quatro dígitos: ")

# Soma dos dígitos
soma = sum(int(digito) for digito in numero)

# Saída
print(soma)