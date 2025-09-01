'''
Escreva um programa em Python que leia uma quantidade n de pessoas entrevistadas. Em
seguida, para cada pessoa leia a idade e o sexo, e calcule e mostre:
● A média de idade das pessoas;
● A média de idade das mulheres;
● A média de idade dos homens;
● A quantidade de pessoas em cada faixa etária segundo a tabela a seguir;
● A porcentagem de homens da quarta faixa etária.
Faixa Etária Idade
1 Até 15 anos
2 De 16 anos a 30 anos
3 De 31 anos a 45 anos
4 De 46 anos a 60 anos
5 Acima de 60 anos
'''

# Leitura do número de pessoas
n = int(input("Digite a quantidade de pessoas entrevistadas: "))

# Variáveis para somatórios e contagem
soma_idade_total = 0
soma_idade_mulheres = 0
soma_idade_homens = 0
qtd_mulheres = 0
qtd_homens = 0

# Contadores por faixa etária
faixa1 = faixa2 = faixa3 = faixa4 = faixa5 = 0
homens_faixa4 = 0

for i in range(1, n + 1):
    print(f"\n--- Pessoa {i} ---")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    # Soma total de idades
    soma_idade_total += idade

    # Soma por sexo
    if sexo == 'F':
        soma_idade_mulheres += idade
        qtd_mulheres += 1
    elif sexo == 'M':
        soma_idade_homens += idade
        qtd_homens += 1
    else:
        print("Sexo inválido! Ignorando para cálculos por sexo.")

    # Verifica faixa etária
    if idade <= 15:
        faixa1 += 1
    elif idade <= 30:
        faixa2 += 1
    elif idade <= 45:
        faixa3 += 1
    elif idade <= 60:
        faixa4 += 1
        if sexo == 'M':
            homens_faixa4 += 1
    else:
        faixa5 += 1

# Cálculos de médias
media_total = soma_idade_total / n
media_mulheres = soma_idade_mulheres / qtd_mulheres if qtd_mulheres > 0 else 0
media_homens = soma_idade_homens / qtd_homens if qtd_homens > 0 else 0

# Porcentagem de homens na quarta faixa
porcentagem_homens_faixa4 = (homens_faixa4 / faixa4 * 100) if faixa4 > 0 else 0

# Resultados
print("\n=== RESULTADOS ===")
print(f"Média de idade das pessoas: {media_total:.2f}")
print(f"Média de idade das mulheres: {media_mulheres:.2f}")
print(f"Média de idade dos homens: {media_homens:.2f}")
print("\nQuantidade de pessoas por faixa etária:")
print(f"Faixa 1 (até 15 anos): {faixa1}")
print(f"Faixa 2 (16 a 30 anos): {faixa2}")
print(f"Faixa 3 (31 a 45 anos): {faixa3}")
print(f"Faixa 4 (46 a 60 anos): {faixa4}")
print(f"Faixa 5 (acima de 60 anos): {faixa5}")
print(f"\nPorcentagem de homens na faixa 4: {porcentagem_homens_faixa4:.2f}%")
