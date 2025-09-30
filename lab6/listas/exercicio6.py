# Exercício 6 – Média de altura dos alunos
# Objetivo: Determinar quantos alunos com mais de 13 anos possuem altura inferior à média

print("=== ANÁLISE DE ALTURA DOS ALUNOS ===")

# Listas para armazenar os dados dos 20 alunos
idades = []
alturas = []

# Entrada de dados para 20 alunos
for i in range(20):
    print(f"\nAluno {i+1}:")
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (em metros): "))
    idades.append(idade)
    alturas.append(altura)

# Cálculo da média de altura de todos os alunos
media_altura = sum(alturas) / len(alturas)
print(f"\nMédia de altura de todos os alunos: {media_altura:.2f} metros")

# Contagem de alunos com mais de 13 anos e altura inferior à média
contador = 0
alunos_condicao = []

for i in range(20):
    if idades[i] > 13 and alturas[i] < media_altura:
        contador += 1
        alunos_condicao.append({
            'numero': i + 1,
            'idade': idades[i],
            'altura': alturas[i]
        })

# Saída dos resultados
print(f"\nQuantidade de alunos com mais de 13 anos e altura inferior à média: {contador}")

if contador > 0:
    print("\nDetalhes dos alunos que atendem à condição:")
    for aluno in alunos_condicao:
        print(f"Aluno {aluno['numero']}: {aluno['idade']} anos, {aluno['altura']:.2f}m")
else:
    print("Nenhum aluno atende à condição especificada.")

# Estatísticas adicionais
print(f"\nEstatísticas gerais:")
print(f"Altura mínima: {min(alturas):.2f}m")
print(f"Altura máxima: {max(alturas):.2f}m")
print(f"Idade mínima: {min(idades)} anos")
print(f"Idade máxima: {max(idades)} anos")