a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))
c = float(input("Digite mais um número: "))

if  (a > 0 and b > 0 and c > 0) and (a + b > c) and (a + c > b) and (b + c > a):
    s = (a + b + c) / 2  # semiperímetro
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Heron
    print("A área do triângulo é:", area)
else:
    print("Os valores fornecidos não formam um triângulo válido.")

