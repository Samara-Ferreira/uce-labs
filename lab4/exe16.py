n = int(input())
soma = 0
dias = 0

while n >= 0:
    soma += n
    dias += 1
    n = int(input())

print(soma)
print(dias)
print(f"{soma/dias:.1f}")
