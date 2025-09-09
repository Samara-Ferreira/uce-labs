# Contadores
total_numeros = 0
positivos = 0
negativos = 0

# Lê o primeiro número
numero = int(input("Digite um número: "))

while numero != 0:
    # Conta o total de números
    total_numeros += 1
    
    # Classifica como positivo ou negativo
    if numero > 0:
        positivos += 1
    else:
        negativos += 1
    
    # Lê o próximo número
    numero = int(input("Digite um número: "))

# Verifica se foram inseridos números
if total_numeros == 0:
    print("Nenhum número foi inserido!")
else:
    # Calcula os percentuais
    percentual_positivos = (positivos / total_numeros) * 100
    percentual_negativos = (negativos / total_numeros) * 100
    
    # Exibe os resultados
    print("\n=== Resultados ===")
    print(f"Total de números inseridos: {total_numeros}")
    print(f"Números positivos: {positivos}")
    print(f"Números negativos: {negativos}")
    print(f"Percentual de positivos: {percentual_positivos:.1f}%")
    print(f"Percentual de negativos: {percentual_negativos:.1f}%")
