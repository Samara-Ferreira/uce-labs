print("=== Levantamento de Produção - Fábrica WK ===")
print("Digite a quantidade de automóveis produzidos por dia")
print("(número negativo para finalizar):")

# Contadores e acumuladores
total_automoveis = 0
dias_producao = 0

# Lê a produção do primeiro dia
producao_dia = int(input(f"Produção do dia: "))

while producao_dia >= 0:
    # Atualiza os totais
    total_automoveis += producao_dia
    dias_producao += 1
    
    # Lê a produção do próximo dia
    producao_dia = int(input(f"Produção do dia: "))

# Calcula e exibe os resultados
print("\n=== Relatório de Produção ===")

if dias_producao > 0:
    media_producao = total_automoveis / dias_producao
    
    print(f"Total de automóveis produzidos: {total_automoveis}")
    print(f"Quantidade de dias na pesquisa: {dias_producao}")
    print(f"Média de carros produzidos por dia: {media_producao:.1f}")
    
    # Informações adicionais
    if dias_producao > 1:
        print(f"\nProdução diária variou de {total_automoveis // dias_producao - (total_automoveis % dias_producao)} a {total_automoveis}")
    
else:
    print("Nenhum dado de produção foi inserido!")
