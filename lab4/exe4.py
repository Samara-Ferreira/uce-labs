A = int(input())
B = int(input())
cresA = float(input()) / 100
cresB = float(input()) / 100

anos = 0
while A < B:
    A += A * cresA
    B += B * cresB
    anos += 1
print(anos)
