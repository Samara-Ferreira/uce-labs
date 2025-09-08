n = int(input())
soma = 0
cont = 0

while soma < n:
    x = int(input())
    soma += x
    cont += 1

print(cont)
print(f"{soma/cont:.1f}")
