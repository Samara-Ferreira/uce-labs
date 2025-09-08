virus = int(input())
leuc = int(input())
taxaV = float(input()) / 100
taxaL = float(input()) / 100

dias = 0
while leuc < 2 * virus:
    virus += virus * taxaV
    leuc += leuc * taxaL
    dias += 1
print(dias)
