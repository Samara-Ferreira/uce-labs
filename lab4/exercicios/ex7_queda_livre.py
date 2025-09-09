# Lê a altura inicial
h0 = float(input("Altura inicial (metros): "))

# Constantes
g = 9.8  # aceleração da gravidade em m/s²
t = 0    # tempo inicial em segundos

print(f"\n=== Evolução da queda ===")
print(f"Altura inicial: {h0} metros")
print(f"Aceleração da gravidade: {g} m/s²")
print()

# Calcula a altura inicial
h = h0 - 0.5 * g * (t ** 2)

# Simula a queda segundo a segundo
while h > 0:
    # Exibe o tempo e a altura
    print(f"t = {t}")
    print(f"h = {h:.1f}")
    
    # Incrementa o tempo
    t += 1
    
    # Calcula a nova altura
    h = h0 - 0.5 * g * (t ** 2)

print(f"\nO objeto atingiu o solo após {t} segundos!")
