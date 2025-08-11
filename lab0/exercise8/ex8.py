
from math import sqrt

a = 5  # cm
area = (3/2) * (a ** 2) * sqrt(3)

# Exibir com até 4 casas decimais (removendo zeros e ponto finais desnecessários)
print("A área do triângulo é:", round(area, 4))
# ou
print(f"A área do triângulo é: {area:.4f}")
