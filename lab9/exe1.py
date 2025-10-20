import numpy as np

# Sistema:
# 3a + 12b + 1c = 23.60
# 12a +  0b + 2c = 52.60
# 0a +  2b + 3c = 27.70

# Matriz dos coeficientes (A)
A = np.array([
    [3, 12, 1],
    [12, 0, 2],
    [0, 2, 3]
])

# Matriz dos resultados (B)
B = np.array([23.60, 52.60, 27.70])

# Resolvendo A * X = B
X = np.linalg.solve(A, B)

# X = [preço_abacate, preço_banana, preço_caqui]
frutas = ["Abacate", "Banana", "Caqui"]

# Exibindo os preços
print("Preços unitários das frutas:")
for i in range(len(frutas)):
    print(f"{frutas[i]}: R$ {X[i]:.2f}")

# Determinando a fruta mais cara
indice_mais_cara = np.argmax(X)
print(f"\nFruta mais cara: {frutas[indice_mais_cara]} (R$ {X[indice_mais_cara]:.2f})")
