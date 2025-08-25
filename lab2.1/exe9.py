# 3.a Dia da semana (sem lista)

# Entrada
x = int(input("Entre com o número do dia de hoje: "))

# Validação
if x < 0 or x > 6:
    print(f"A entrada {x} é inválida")
else:
    n = int(input("Entre com o número de dias após hoje: "))
    futuro = (x + n) % 7

    # Descobre o dia de hoje
    if x == 0:
        hoje = "domingo"
    elif x == 1:
        hoje = "segunda"
    elif x == 2:
        hoje = "terça"
    elif x == 3:
        hoje = "quarta"
    elif x == 4:
        hoje = "quinta"
    elif x == 5:
        hoje = "sexta"
    else:
        hoje = "sábado"

    # Descobre o dia futuro
    if futuro == 0:
        dia_futuro = "domingo"
    elif futuro == 1:
        dia_futuro = "segunda"
    elif futuro == 2:
        dia_futuro = "terça"
    elif futuro == 3:
        dia_futuro = "quarta"
    elif futuro == 4:
        dia_futuro = "quinta"
    elif futuro == 5:
        dia_futuro = "sexta"
    else:
        dia_futuro = "sábado"

    print(f"Hoje é {hoje} e o dia futuro é {dia_futuro}")


# 3.b Qual o mês? (sem lista)

m = int(input("Digite um número de mês (1 a 12): "))

if m == 1:
    print("janeiro")
elif m == 2:
    print("fevereiro")
elif m == 3:
    print("março")
elif m == 4:
    print("abril")
elif m == 5:
    print("maio")
elif m == 6:
    print("junho")
elif m == 7:
    print("julho")
elif m == 8:
    print("agosto")
elif m == 9:
    print("setembro")
elif m == 10:
    print("outubro")
elif m == 11:
    print("novembro")
elif m == 12:
    print("dezembro")
else:
    print("número de mês inválido")