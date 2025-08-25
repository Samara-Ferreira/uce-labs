'''
Considere dois números reais 𝑎 e 𝑏, sendo 𝑏 > 𝑎. Um número real 𝑥 pertence ao intervalo
[𝑎, 𝑏] se 𝑎 ≤ 𝑥 ≤ 𝑏.
Escreva um programa que leia os números reais 𝑥, 𝑎, 𝑏, nesta ordem.
● Se 𝑥 pertencer ao intervalo, imprima a seguinte mensagem:
“x pertence ao intervalo [a, b]”
● Caso contrário, imprima a seguinte mensagem:
“x não pertence ao intervalo [a, b]”
Se as entradas forem inválidas, ou seja, se 𝑏 ≤ 𝑎, imprima a seguinte mensagem:
“entradas a e b inválidas”
Nas mensagens, substitua as letras x, a, b pelos valores fornecidos como entrada
'''

x = float(input("Digite o valor de x: "))
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

if b <= a:
    print("entradas a e b inválidas")
elif a <= x <= b:
    print(f"{x} pertence ao intervalo [{a}, {b}]")
else:
    print(f"{x} não pertence ao intervalo [{a}, {b}]")
