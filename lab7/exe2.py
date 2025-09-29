import math

# Entrada dos catetos
cateto_a = float(input("Digite o comprimento do primeiro cateto: "))
cateto_b = float(input("Digite o comprimento do segundo cateto: "))

# Teorema de Pitágoras: c² = a² + b²
hipotenusa = math.sqrt(math.pow(cateto_a, 2) + math.pow(cateto_b, 2))

# Saída formatada com duas casas decimais
print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")
