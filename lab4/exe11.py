cont = "S"
while cont.upper() == "S":
    ini = int(input())
    fim = int(input())
    passo = int(input())

    c = ini
    while c <= fim:
        f = c * 9/5 + 32
        print(c, f"{f:.1f}")
        c += passo

    cont = input()
