# A. Função para categorizar por índice par e ímpar
def categorizar_por_indice_par(lista):
    par = []
    impar = []
    for i in range(len(lista)):
        if i % 2 == 0:
            par.append(lista[i])
        else:
            impar.append(lista[i])
    return [par, impar]

# B. Função para categorizar por paridade dos elementos
def categorizar_por_paridade(lista):
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return [pares, impares]

numeros = [1, 2, 3, 4, 5, 6]

resultado_indices = categorizar_por_indice_par(numeros)
resultado_paridade = categorizar_por_paridade(numeros)

print("Categorias por índice par/ímpar:", resultado_indices)
print("Categorias por paridade:", resultado_paridade)