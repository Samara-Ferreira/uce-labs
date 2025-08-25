'''
Considere dois intervalos numéricos sobre a reta real: 𝐼 . Escreva um
1 = [𝑎, 𝑏] 𝑒 𝐼
2 = [𝑐, 𝑑]
programa que leia os números reais a, b, c e d (nesta ordem) correspondentes aos intervalos 𝐼
1
e 𝐼 e verifique se existe interseção (pelo menos um ponto em comum) entre os intervalos.
2
● Se houver interseção, o programa deverá imprimir:
“Há intersecção”
● Se não houver interseção, o programa deverá imprimir:
“Não há intersecção”
● Por fim, se as entradas forem inválidas, o programa deverá imprimir:
“Entradas invalidas”
Observações:
1. Verifique se os intervalos são válidos, ou seja, se 𝑏 > 𝑎 e 𝑑 > 𝑐.
2. Não pressuponha nada com respeito à posição relativa entre os intervalos [𝑎, 𝑏] e [𝑐, 𝑑]
. Ou seja, eles podem estar situados antes ou depois um do outro.
'''
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))

if b <= a or d <= c:
    print("Entradas invalidas")
elif a <= d and c <= b:
    print("Há intersecção")
else:
    print("Não há intersecção")
