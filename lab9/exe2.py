# Matriz de temperaturas (exemplo)
matriz = [
    [27.5, 21.3, 30.5, 28.1],
    [22.3, 19.5, 24.5, 19.1],
    [31.4, 34.3, 29.5, 29.1]
]

# Número de cidades (linhas)
linhas = len(matriz)
# Número de dias (colunas) - assumindo que todas as linhas têm o mesmo tamanho
colunas = len(matriz[0])

# Vetor para armazenar as menores temperaturas
menores = []

# Percorre as linhas da matriz
for i in range(linhas):
    menor = matriz[i][0]  # começa com o primeiro valor da linha i
    for j in range(colunas):
        if matriz[i][j] < menor:
            menor = matriz[i][j]  # atualiza se encontrar menor valor
    menores.append(menor)

# Exibe o vetor com as menores temperaturas
for i in range(linhas):
    print(f"Menor temperatura da cidade {i + 1}: {menores[i]}°C")