
# Constante PI
PI = 3.14159

# Lê o primeiro raio
raio = float(input("Raio do círculo: "))

while raio > 0:
    # Calcula a área do círculo: A = PI * R²
    area = PI * raio * raio
    
    # Exibe o resultado com 2 casas decimais
    print(f"Área do círculo: {area:.2f}")
    print()  # Linha em branco para melhor visualização
    
    # Lê o próximo raio
    raio = float(input("Raio do círculo: "))

print("Programa encerrado.")
