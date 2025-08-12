# Exercício 10 – Distância entre dois pontos no plano cartesiano

import math

# Lê as coordenadas do ponto A (xA, yA)
print("Digite as coordenadas do ponto A:")
xA = float(input("xA: "))
yA = float(input("yA: "))

# Lê as coordenadas do ponto B (xB, yB)
print("Digite as coordenadas do ponto B:")
xB = float(input("xB: "))
yB = float(input("yB: "))

# Calcula a distância entre os pontos A e B usando a fórmula:
# d_AB = √[(xB - xA)² + (yB - yA)²]
distancia = math.sqrt((xB - xA)**2 + (yB - yA)**2)

# Imprime o resultado com até três casas decimais de precisão
print(f"A distância entre os pontos A({xA}, {yA}) e B({xB}, {yB}) é: {distancia:.3f}")
