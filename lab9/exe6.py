def imprimir_matriz(matriz, titulo="Matriz:"):
    """Função auxiliar para imprimir matrizes de forma legível."""
    print(titulo)
    for linha in matriz:
        print(" ".join(f"{item:<6}" for item in linha))

def transpor_matriz(matriz):
    """Função auxiliar que transpõe uma matriz."""
    num_linhas_orig = len(matriz)
    num_cols_orig = len(matriz[0])
    
    matriz_transposta = [[0 for _ in range(num_linhas_orig)] for _ in range(num_cols_orig)]
    
    for i in range(num_linhas_orig):
        for j in range(num_cols_orig):
            matriz_transposta[j][i] = matriz[i][j]
    return matriz_transposta

def ordenar_colunas_decrescente(matriz):
    """
    Ordena cada coluna da matriz em ordem decrescente sem usar sort().
    """
    # Transpõe para trabalhar por linha
    matriz_transposta = transpor_matriz(matriz)

    # Para cada linha (coluna original)
    for linha in matriz_transposta:
        n = len(linha)
        # Bubble Sort decrescente
        for i in range(n - 1):
            for j in range(n - i - 1):
                if linha[j] < linha[j + 1]:  # troca se estiver fora da ordem
                    linha[j], linha[j + 1] = linha[j + 1], linha[j]

    # Transpõe de volta para forma original
    matriz_ordenada = transpor_matriz(matriz_transposta)
    return matriz_ordenada

# --- Testando com o Exemplo ---
entrada_6 = [
    [1, 10, 100, 1000],
    [2, 20, 200, 2000],
    [3, 30, 300, 3000],
    [4, 40, 400, 4000]
]

imprimir_matriz(entrada_6, "Matriz Original:")
matriz_final = ordenar_colunas_decrescente(entrada_6)
print()
imprimir_matriz(matriz_final, "Matriz com Colunas Ordenadas (Saída):")
