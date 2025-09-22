# Função para adicionar um produto
def adicionar_produto(inventario, nome, preco, quantidade):
    inventario.append([nome, preco, quantidade])

# Função para atualizar a quantidade de um produto existente
def atualizar_quantidade(inventario, nome, nova_quantidade):
    for produto in inventario:
        if produto[0] == nome:
            produto[2] = nova_quantidade
            return True  # atualização realizada
    return False  # produto não encontrado

# Função para buscar um produto pelo nome
def buscar_produto(inventario, nome):
    for produto in inventario:
        if produto[0] == nome:
            return produto
    return None

# Função para listar todo o inventário
def listar_inventario(inventario):
    print(f"{'Produto':<15} {'Preço':>10} {'Quantidade':>10}")
    print("-" * 37)
    for produto in inventario:
        nome, preco, quantidade = produto
        print(f"{nome:<15} {preco:>10.2f} {quantidade:>10}")

# Programa principal
inventario = [['Teclado', 150.00, 10], ['Mouse', 80.00, 25]]

# Adicionar produto
adicionar_produto(inventario, 'Monitor', 900.00, 5)

# Atualizar quantidade
atualizar_quantidade(inventario, 'Mouse', 30)

# Buscar produto
produto_encontrado = buscar_produto(inventario, 'Teclado')
print("Produto encontrado:", produto_encontrado)

# Listar inventário completo
listar_inventario(inventario)
