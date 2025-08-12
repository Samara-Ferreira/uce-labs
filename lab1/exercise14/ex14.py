# Exercício 14 – Ajude Skywalker

# Lê os cinco valores de entrada
print("Digite os valores das naves:")
A = int(input("Total de naves sondadas no quadrante (A): "))
B = int(input("Total de naves amigas detectadas à frente (B): "))
C = int(input("Total de naves amigas à direita (C): "))
D = int(input("Total de naves amigas à esquerda (D): "))
E = int(input("Total de naves amigas atrás (E): "))

# Calcula o total de naves inimigas no quadrante
# Naves inimigas = Total de naves - Naves amigas
# Naves amigas = B + C + D + E
naves_amigas = B + C + D + E
naves_inimigas = A - naves_amigas

# Imprime o resultado
print(f"Total de naves inimigas no quadrante: {naves_inimigas}")
