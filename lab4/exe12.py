n = int(input())
total = 0
pos = 0
neg = 0

while n != 0:
    total += 1
    if n > 0:
        pos += 1
    else:
        neg += 1
    n = int(input())

print(f"{(pos/total)*100:.1f}")
print(f"{(neg/total)*100:.1f}")
