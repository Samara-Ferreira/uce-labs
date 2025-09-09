
# Contadores e acumuladores
total_pessoas = 0
soma_idades = 0
pessoas_mais_3_filhos = 0
jovens_com_filhos = 0  # pessoas < 20 anos com filhos
total_jovens = 0       # pessoas < 20 anos

# Lê a primeira idade
idade = int(input("Idade: "))

while idade >= 0:
    # Lê a quantidade de filhos
    filhos = int(input("Quantidade de filhos: "))
    
    # Atualiza os contadores
    total_pessoas += 1
    soma_idades += idade
    
    # Verifica se tem mais de 3 filhos
    if filhos > 3:
        pessoas_mais_3_filhos += 1
    
    # Verifica se é jovem (< 20 anos)
    if idade < 20:
        total_jovens += 1
        if filhos > 0:
            jovens_com_filhos += 1
    
    print()  # Linha em branco para separar entradas
    
    # Lê a próxima idade
    idade = int(input("Idade: "))

# Calcula e exibe os resultados
print("=== Resultados da Pesquisa ===")

if total_pessoas > 0:
    # Média de idade
    media_idade = soma_idades / total_pessoas
    print(f"Média de idade do grupo: {media_idade:.1f} anos")
    
    # Quantidade de pessoas com mais de 3 filhos
    print(f"Pessoas com mais de 3 filhos: {pessoas_mais_3_filhos}")
    
    # Porcentagem de jovens com filhos (em relação ao total de pessoas entrevistadas)
    if total_pessoas > 0:
        porcentagem_jovens_com_filhos = (jovens_com_filhos / total_pessoas) * 100
        print(f"Porcentagem de pessoas < 20 anos com filhos: {porcentagem_jovens_com_filhos:.1f}%")
    else:
        print("Nenhuma pessoa foi entrevistada para calcular a porcentagem.")
    
    # Total de pessoas entrevistadas
    print(f"Total de pessoas entrevistadas: {total_pessoas}")
    
else:
    print("Nenhuma pessoa foi entrevistada!")
