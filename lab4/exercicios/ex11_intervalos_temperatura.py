
continuar = 'S'

while continuar == 'S':
    print("\n=== Nova Conversão ===")
    
    # Lê os parâmetros da conversão
    temp_inicial = int(input("Temperatura inicial (°C): "))
    temp_final = int(input("Temperatura final (°C): "))
    intervalo = int(input("Intervalo entre temperaturas: "))
    
    # Verifica se os valores são válidos
    if temp_inicial > temp_final:
        print("Erro: Temperatura inicial deve ser menor ou igual à final!")
    elif intervalo <= 0:
        print("Erro: Intervalo deve ser maior que zero!")
    else:
        # Exibe a tabela de conversão
        print(f"\n=== Tabela de Conversão (intervalo de {intervalo}°C) ===")
        print("Celsius  | Fahrenheit")
        print("-" * 20)
        
        # Gera as conversões no intervalo especificado
        temperatura = temp_inicial
        while temperatura <= temp_final:
            # Converte temperatura de Celsius para Fahrenheit: F = C * 9/5 + 32
            fahrenheit = temperatura * 9/5 + 32
            print(f"{temperatura:7d}  | {fahrenheit:8.1f}")
            temperatura += intervalo
    
    # Pergunta se o usuário deseja continuar
    print()
    continuar = input("Deseja fazer outra conversão? (S/N): ").upper().strip()

print("Programa encerrado.")
