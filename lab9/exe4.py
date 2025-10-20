import numpy as np

def resolver_sistema_bacterias(vetor_B):
    """
    Resolve o sistema de equações lineares para o problema das bactérias.
    """
    
    # Matriz A com os coeficientes de consumo de cada bactéria 
    # Colunas: [estafilococo, salmonela, coli]
    # Linhas: [Alimento A, Alimento B, Alimento C]
    A = np.array([
        [2, 1, 4],
        [1, 2, 0],
        [2, 3, 2]
    ])

    # Nomes das bactérias na ordem das colunas de A
    nomes_bacterias = ["estafilococo", "salmonela", "coli"]
    
    try:
        # Resolve o sistema Ax = B, onde x é o vetor de populações
        populacoes = np.linalg.solve(A, vetor_B)
        
        # Cria um dicionário para associar nomes às populações
        resultado = dict(zip(nomes_bacterias, populacoes))

        # 1. Imprime o nome e a respectiva quantidade [cite: 41]
        for bacteria, qtd in resultado.items():
            print(f"{bacteria}: {qtd:.1f}") # Arredondado em 1 casa decimal

        # 2. Encontra a bactéria com a menor população [cite: 42]
        menor_bacteria = min(resultado, key=resultado.get)
        print(menor_bacteria)

    except np.linalg.LinAlgError:
        print("Não foi possível resolver o sistema.")

# --- Testando com os Exemplos Fornecidos ---

# Exemplo 1 [cite: 43]
print("--- Exemplo 1 ---")
entrada_1 = [3955.25, 5652.36, 8562.22]
resolver_sistema_bacterias(entrada_1)

# Exemplo 2 [cite: 49]
print("\n--- Exemplo 2 ---")
entrada_2 = [2095.52, 1855.75, 11295.21]
resolver_sistema_bacterias(entrada_2)

# Exemplo 3 [cite: 55]
print("\n--- Exemplo 3 ---")
entrada_3 = [8596.14, 3212.68, 2652.11]
resolver_sistema_bacterias(entrada_3)