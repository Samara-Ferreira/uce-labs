n = int(input())
somaP = somaI = contP = contI = total = 0

while n > 0:
    total += 1
    if n % 2 == 0:
        somaP += n
        contP += 1
    else:
        somaI += n
        contI += 1
    n = int(input())

print(f"{somaP/contP:.1f}" if contP > 0 else "0.0")
print(f"{somaI/contI:.1f}" if contI > 0 else "0.0")
print(total)
