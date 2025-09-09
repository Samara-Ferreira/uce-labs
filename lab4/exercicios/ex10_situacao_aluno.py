
contador_aluno = 1
aprovados = 0
final = 0
reprovados = 0

# Lê a primeira nota
nota = float(input(f"Média parcial do aluno {contador_aluno}: "))

# Continua lendo notas enquanto forem válidas (entre 0 e 10)
while 0 <= nota <= 10:
    # Determina a situação do aluno e incrementa o contador correspondente
    if nota >= 7:
        situacao = "APROVADO"
        aprovados += 1
    elif nota >= 3:
        situacao = "FINAL"
        final += 1
    else:
        situacao = "REPROVADO"
        reprovados += 1
    
    print(f"Aluno {contador_aluno}: {situacao}")
    print()
    
    contador_aluno += 1
    
    # Lê a próxima nota
    nota = float(input(f"Média parcial do aluno {contador_aluno}: "))

print("Nota inválida! Programa encerrado.")

# Exibe o resumo final
print("\n=== Resumo Final ===")
print(f"Total de alunos avaliados: {contador_aluno - 1}")
print(f"Aprovados: {aprovados}")
print(f"Final: {final}")
print(f"Reprovados: {reprovados}")
