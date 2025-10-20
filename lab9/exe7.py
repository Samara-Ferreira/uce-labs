def diferenca_diagonais(matriz):
    """
    Calcula a diferença entre a soma da diagonal principal
    e da diagonal secundária.
    """
    n = len(matriz)
    soma_principal = 0
    soma_secundaria = 0
    
    for i in range(n):
        soma_principal += matriz[i][i]
        soma_secundaria += matriz[i][n - 1 - i]
        
    # Imprime a diferença 
    print(soma_principal - soma_secundaria)


matriz_7 = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

diferenca_diagonais(matriz_7)