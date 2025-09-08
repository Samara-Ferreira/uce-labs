valor = float(input())
meses = int(input())

i = 0
while i < meses:
    valor *= 1.04
    print(f"{valor:.2f}")
    i += 1
