import math

# Entrada do ângulo em graus
graus = float(input("Digite um ângulo em graus: "))

# Conversão para radianos
radianos = math.radians(graus)

# Cálculo do seno e cosseno
seno = math.sin(radianos)
cosseno = math.cos(radianos)

# Exibição dos resultados
print(f"Ângulo: {graus}°")
print(f"Em radianos: {radianos:.4f} rad")
print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
