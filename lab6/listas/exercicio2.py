# Exercício 2 – Inversor de Palavras
# Objetivo: Criar um programa que inverte a ordem dos caracteres de uma palavra usando manipulação de listas

# Entrada de Dados
palavra = input("Digite uma palavra: ")

# Processamento
# Converte a palavra em uma lista de caracteres
lista_caracteres = list(palavra)

# Inverte a ordem dos caracteres usando manipulação de listas
lista_invertida = []
for i in range(len(lista_caracteres) - 1, -1, -1):
    lista_invertida.append(lista_caracteres[i])

# Converte a lista invertida de volta para string
palavra_invertida = ''.join(lista_invertida)

# a
print(f"Palavra original: {palavra}")
print(f"Palavra invertida: {palavra_invertida}")