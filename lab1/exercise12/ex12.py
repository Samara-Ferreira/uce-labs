# Exercício 12 – Média ponderada

# Lê as quatro notas do aluno
print("Digite as quatro notas do aluno:")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

# Calcula a média ponderada com pesos 1, 2, 3 e 4 respectivamente
# Fórmula: MP = (nota1*1 + nota2*2 + nota3*3 + nota4*4) / (1+2+3+4)
# MP = (nota1 + 2*nota2 + 3*nota3 + 4*nota4) / 10
media_ponderada = (nota1 * 1 + nota2 * 2 + nota3 * 3 + nota4 * 4) / (1 + 2 + 3 + 4)

# Imprime o resultado com duas casas decimais
print(f"A média ponderada é: {media_ponderada:.2f}")
