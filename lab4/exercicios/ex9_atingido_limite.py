
# Lê o valor limite
n = int(input("Digite o valor limite (n): "))

soma = 0
contador = 0

print(f"Digite números inteiros até que a soma atinja pelo menos {n}:")

# Lê números até atingir o limite
while soma < n:
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1
    print(f"Soma atual: {soma}")

# Calcula a média
media = soma / contador

print("\n=== Resultado ===")
print(f"Limite atingido!")
print(f"Números lidos: {contador}")
print(f"Soma final: {soma}")
print(f"Média: {media:.1f}")
