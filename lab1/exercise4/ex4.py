import math

# Leitura do raio
r = float(input("Digite o valor do raio: "))

# Cálculo da área do círculo
area_circulo = math.pi * r ** 2

# Cálculo do volume da esfera
volume_esfera = (4/3) * math.pi * r ** 3

# Saída com duas casas decimais
print(f"{area_circulo:.2f}")
print(f"{volume_esfera:.2f}")