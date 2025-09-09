# Contadores e acumuladores
total_numeros = 0
soma_pares = 0
contador_pares = 0
soma_impares = 0
contador_impares = 0

# Lê o primeiro número
numero = int(input("Digite um número: "))

while numero > 0:
    # Conta o total de números
    total_numeros += 1
    
    # Verifica se é par ou ímpar
    if numero % 2 == 0:
        # Número par
        soma_pares += numero
        contador_pares += 1
    else:
        # Número ímpar
        soma_impares += numero
        contador_impares += 1
    
    # Lê o próximo número
    numero = int(input("Digite um número: "))

# Exibe os resultados
print("\n=== Resultados ===")
print(f"Total de números lidos: {total_numeros}")

if contador_pares > 0:
    media_pares = soma_pares / contador_pares
    print(f"Média dos valores pares: {media_pares:.1f}")
    print(f"Quantidade de números pares: {contador_pares}")
else:
    print("Nenhum número par foi digitado.")

if contador_impares > 0:
    media_impares = soma_impares / contador_impares
    print(f"Média dos valores ímpares: {media_impares:.1f}")
    print(f"Quantidade de números ímpares: {contador_impares}")
else:
    print("Nenhum número ímpar foi digitado.")

if total_numeros == 0:
    print("Nenhum número válido foi inserido!")
