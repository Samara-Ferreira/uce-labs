def verificar_quadrado_magico(matriz):
    """
    Verifica se uma matriz é um Quadrado Mágico.
    """
    n = len(matriz)
    if n == 0 or len(matriz[0]) != n:
        print("NAO") # Não é quadrada
        return

    # --- 1. Verificar se os números não se repetem [cite: 64] ---
    numeros = []
    for linha in matriz:
        numeros.extend(linha)
    
    # Se o tamanho da lista for diferente do tamanho do 'set' (valores únicos),
    # então existem números repetidos.
    if len(numeros) != len(set(numeros)):
        print("NAO")
        return

    # --- 2. Calcular a "soma mágica" e verificar as linhas [cite: 65] ---
    soma_magica = sum(matriz[0])

    for i in range(1, n):
        if sum(matriz[i]) != soma_magica:
            print("NAO")
            return

    # --- 3. Verificar as colunas [cite: 66] ---
    for j in range(n): # Itera pelas colunas
        soma_coluna = 0
        for i in range(n): # Itera pelas linhas
            soma_coluna += matriz[i][j]
        
        if soma_coluna != soma_magica:
            print("NAO")
            return

    # --- 4. Verificar as diagonais [cite: 67] ---
    soma_diag_principal = 0
    soma_diag_secundaria = 0
    for i in range(n):
        soma_diag_principal += matriz[i][i]
        soma_diag_secundaria += matriz[i][n - 1 - i]

    if soma_diag_principal != soma_magica or soma_diag_secundaria != soma_magica:
        print("NAO")
        return

    # Se passou por todas as verificações:
    print("SIM") # [cite: 68]

# --- Testando com os Exemplos Fornecidos ---

# Exemplo 1 [cite: 70]
print("--- Exemplo 1 ---")
matriz_1 = [[4, 9, 2], [3, 5, 7], [8, 2, 6]] # "8, 2, 6" tem 2 repetido
verificar_quadrado_magico(matriz_1)

# Exemplo 2 [cite: 73]
print("\n--- Exemplo 2 ---")
matriz_2 = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
verificar_quadrado_magico(matriz_2)