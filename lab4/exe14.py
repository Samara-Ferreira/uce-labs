n = float(input())
total = 0
aprov = 0

while 0 <= n <= 10:
    total += 1
    if n >= 7:
        aprov += 1
    n = float(input())

print(aprov)
print(f"{(aprov/total)*100:.1f}")
