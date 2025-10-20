def imprimir_matriz_formatada(matriz, titulo="Matriz:"):
    """
    Função para imprimir matrizes de forma organizada (em formato de grade)[cite: 101].
    """
    print(titulo)
    for linha in matriz:
        # Usa 'end=""' para evitar nova linha e ' ' para separar os números
        for item in linha:
            print(item, end=" ")
        print() # Pula para a próxima linha

# 1. Defina a Matriz Original [cite: 89-93]
matriz_original = [
    [1, 2, 3],
    [4, 5, 6]
]

# 2. Crie a Matriz Transposta
# Descubra as dimensões [cite: 95]
num_linhas = len(matriz_original)
num_colunas = len(matriz_original[0])

# Crie uma nova matriz com dimensões invertidas e preenchida com zeros [cite: 96-97]
# Nova dimensão: num_colunas x num_linhas (3x2)
matriz_transposta = [[0 for _ in range(num_linhas)] for _ in range(num_colunas)]

# Use laços aninhados para preencher a transposta [cite: 98-99]
for i in range(num_linhas):
    for j in range(num_colunas):
        matriz_transposta[j][i] = matriz_original[i][j]

# 3. Imprima as Matrizes [cite: 100]
imprimir_matriz_formatada(matriz_original, "Matriz Original:")
print() # Espaçamento
imprimir_matriz_formatada(matriz_transposta, "Matriz Transposta:")