numero = int(input("Digite um número inteiro de quatro dígitos: "))

# Extrai os dígitos usando divisão e módulo
milhar = numero // 1000
centena = (numero // 100) % 10
dezena = (numero // 10) % 10
unidade = numero % 10

soma = milhar + centena + dezena + unidade

print(soma)