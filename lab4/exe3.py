n = int(input())
soma = 0
cont = 0
while n != 0:
    soma += n
    cont += 1
    n = int(input())
media = soma / cont
print(f"{media:.2f}")