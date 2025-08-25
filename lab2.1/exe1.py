a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
c = float(input("Digite mais um número: "))

if ((a > 0 and b > 0 and c > 0) and (a + b > c) and (a + c > b) and (b + c > a)):
    if a == b == c:
        tipo = "equilátero"
    elif a == b or b == c or a == c:
        tipo = "isósceles"
    else:
        tipo = "escaleno"
else:
    tipo = "inválido"

print("O triângulo é:", tipo)