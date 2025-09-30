# Exercício 4 – Inversor Parcial
# Objetivo: Criar um programa que inverte apenas uma sub-lista entre dois índices específicos

def inverter_parcial(lista, i, j):
    """
    Função que inverte apenas a sub-lista entre os índices i e j (inclusive)
    """
    # Cria uma cópia da lista original para não modificar a original
    lista_resultado = lista.copy()
    
    # Inverte apenas a sub-lista entre os índices i e j
    while i < j:
        # Troca os elementos nas posições i e j
        lista_resultado[i], lista_resultado[j] = lista_resultado[j], lista_resultado[i]
        i += 1
        j -= 1
    
    return lista_resultado

# Entrada de dados
print("=== INVERSOR PARCIAL ===")
print("Digite os elementos da lista separados por espaço:")
elementos = input().split()
# Converte para números se possível, senão mantém como string
lista = []
for elemento in elementos:
    try:
        lista.append(int(elemento))
    except ValueError:
        lista.append(elemento)

print(f"Lista original: {lista}")

# Solicita os índices
i = int(input("Digite o índice inicial (i): "))
j = int(input("Digite o índice final (j): "))

# Validação dos índices
if i < 0 or j >= len(lista) or i > j:
    print("Erro: Índices inválidos!")
    print(f"Os índices devem estar entre 0 e {len(lista)-1} e i deve ser menor ou igual a j")
else:
    # Chama a função para inverter parcialmente
    lista_invertida = inverter_parcial(lista, i, j)
    
    # Saída
    print(f"Lista com sub-lista invertida entre índices {i} e {j}: {lista_invertida}")

# Exemplo do exercício
print("\n=== EXEMPLO DO EXERCÍCIO ===")
exemplo_lista = [1, 2, 3, 4, 5]
exemplo_i = 1
exemplo_j = 3
resultado_exemplo = inverter_parcial(exemplo_lista, exemplo_i, exemplo_j)
print(f"Entrada: {exemplo_lista}, i={exemplo_i}, j={exemplo_j}")
print(f"Saída: {resultado_exemplo}")