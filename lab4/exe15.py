idade = int(input())
somaIdade = 0
cont = 0
mais3 = 0
menos20ComFilhos = 0
menos20 = 0

while idade >= 0:
    filhos = int(input())
    somaIdade += idade
    cont += 1
    if filhos > 3:
        mais3 += 1
    if idade < 20:
        menos20 += 1
        if filhos > 0:
            menos20ComFilhos += 1
    idade = int(input())

print(f"{somaIdade/cont:.1f}")
print(mais3)
print(f"{(menos20ComFilhos/menos20)*100:.1f}" if menos20 > 0 else "0.0")
print(cont)
