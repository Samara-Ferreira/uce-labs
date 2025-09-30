# Exercício 7 – Rotacionador de Listas
# Objetivo: Criar uma função que rotaciona uma lista para a esquerda em n posições

def rotacionar_lista(lista, n):
    """
    Função que rotaciona uma lista para a esquerda em n posições.
    
    Args:
        lista: Lista de inteiros a ser rotacionada
        n: Número de posições para rotacionar (pode ser maior que o tamanho da lista)
    
    Returns:
        Nova lista rotacionada
    """
    if not lista:  # Lista vazia
        return lista
    
    tamanho = len(lista)
    # Normaliza n para evitar rotações desnecessárias
    # Se n > tamanho, usa o resto da divisão
    n = n % tamanho
    
    # Se n = 0, não há rotação
    if n == 0:
        return lista.copy()
    
    # Rotaciona: pega elementos de n até o fim + elementos do início até n-1
    lista_rotacionada = lista[n:] + lista[:n]
    
    return lista_rotacionada

# Programa principal
print("=== ROTACIONADOR DE LISTAS ===")

# Entrada de dados
print("Digite os elementos da lista separados por espaço:")
elementos = input().split()
lista = [int(x) for x in elementos]

print(f"Lista original: {lista}")

n = int(input("Digite o número de posições para rotacionar à esquerda: "))

# Chama a função de rotação
lista_rotacionada = rotacionar_lista(lista, n)

# Saída
print(f"Lista rotacionada {n} posições à esquerda: {lista_rotacionada}")

# Exemplos demonstrativos
print("\n=== EXEMPLOS DEMONSTRATIVOS ===")

# Exemplo do exercício
exemplo1 = [1, 2, 3, 4, 5]
resultado1 = rotacionar_lista(exemplo1, 2)
print(f"Exemplo 1: {exemplo1} rotacionada 2 posições = {resultado1}")

# Outros exemplos
exemplo2 = [1, 2, 3, 4, 5]
resultado2 = rotacionar_lista(exemplo2, 1)
print(f"Exemplo 2: {exemplo2} rotacionada 1 posição = {resultado2}")

exemplo3 = [1, 2, 3, 4, 5]
resultado3 = rotacionar_lista(exemplo3, 7)  # n > tamanho da lista
print(f"Exemplo 3: {exemplo3} rotacionada 7 posições (7%5=2) = {resultado3}")

exemplo4 = [10, 20, 30]
resultado4 = rotacionar_lista(exemplo4, 0)
print(f"Exemplo 4: {exemplo4} rotacionada 0 posições = {resultado4}")