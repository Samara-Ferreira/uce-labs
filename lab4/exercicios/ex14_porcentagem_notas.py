# Contadores
total_notas = 0
notas_acima_7 = 0

# Lê a primeira nota
nota = float(input("Digite uma nota: "))

# Continua lendo notas enquanto forem válidas (entre 0.0 e 10.0)
while 0.0 <= nota <= 10.0:
    # Conta o total de notas
    total_notas += 1
    
    # Verifica se a nota é maior ou igual a 7
    if nota >= 7.0:
        notas_acima_7 += 1
    
    # Lê a próxima nota
    nota = float(input("Digite uma nota: "))

print("Nota inválida! Encerrando programa...")

# Exibe os resultados
print("\n=== Resultados ===")
if total_notas > 0:
    porcentagem = (notas_acima_7 / total_notas) * 100
    
    print(f"Total de notas digitadas: {total_notas}")
    print(f"Notas >= 7.0: {notas_acima_7}")
    print(f"Porcentagem de notas >= 7.0: {porcentagem:.1f}%")
else:
    print("Nenhuma nota válida foi inserida!")
