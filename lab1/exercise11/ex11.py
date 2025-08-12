# Exercício 11 – Ponto médio entre dois pontos no plano cartesiano

# Lê as coordenadas do ponto A (xA, yA)
print("Digite as coordenadas do ponto A:")
xA = float(input("xA: "))
yA = float(input("yA: "))

# Lê as coordenadas do ponto B (xB, yB)
print("Digite as coordenadas do ponto B:")
xB = float(input("xB: "))
yB = float(input("yB: "))

# Calcula as coordenadas do ponto médio M usando as fórmulas:
# xM = (xA + xB) / 2
# yM = (yA + yB) / 2
xM = (xA + xB) / 2
yM = (yA + yB) / 2

# Imprime o resultado com até uma casa decimal de precisão
print(f"As coordenadas do ponto médio M são: ({xM:.1f}, {yM:.1f})")
