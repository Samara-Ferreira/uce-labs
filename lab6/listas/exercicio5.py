# Exercício 5 – Separador de Listas
# Objetivo: Separar uma lista mista de números e strings em duas listas distintas

def separar_listas(lista_mista):
    """
    Função que separa uma lista mista em duas listas:
    - Uma com números (inteiros e floats)
    - Outra com strings
    """
    lista_numeros = []
    lista_strings = []
    
    for elemento in lista_mista:
        if isinstance(elemento, (int, float)):
            lista_numeros.append(elemento)
        elif isinstance(elemento, str):
            lista_strings.append(elemento)
    
    return lista_numeros, lista_strings

# Entrada de dados
print("=== SEPARADOR DE LISTAS ===")
print("Digite os elementos da lista separados por espaço:")
print("(Números serão identificados automaticamente)")
entrada = input().split()

# Converte os elementos para seus tipos apropriados
lista_mista = []
for elemento in entrada:
    # Tenta converter para int
    try:
        lista_mista.append(int(elemento))
    except ValueError:
        # Se não for int, tenta converter para float
        try:
            lista_mista.append(float(elemento))
        except ValueError:
            # Se não for float, mantém como string
            lista_mista.append(elemento)

print(f"\nLista mista original: {lista_mista}")

# Separa a lista
numeros, strings = separar_listas(lista_mista)

# Saída
print(f"Lista de números: {numeros}")
print(f"Lista de strings: {strings}")

# Exemplo adicional para demonstração
print("\n=== EXEMPLO DEMONSTRATIVO ===")
exemplo_mista = [1, "python", 3.14, "programação", 42, "lista", 2.5, "exercício"]
exemplo_numeros, exemplo_strings = separar_listas(exemplo_mista)
print(f"Lista mista: {exemplo_mista}")
print(f"Números: {exemplo_numeros}")
print(f"Strings: {exemplo_strings}")