'''
Escreva um programa que leia 02 valores, x e y, que representam as coordenadas de um
ponto no plano cartesiano.
Como saída, determine em que quadrante (Q1, Q2, Q3 ou Q4) o ponto está situado, ou se ele
está sobre um dos eixos cartesianos (Eixo X, Eixo Y), ou se ele está na origem 𝑥 = 𝑦 = 0
(Origem).
'''

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
else:
    print("Q4")