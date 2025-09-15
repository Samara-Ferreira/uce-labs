'''
Escreva uma função que receba dois números e retorne verdadeiro (True) ou falso (False)
indicando se o primeiro número é divisível pelo segundo. O programa principal deve imprimir
“DIVISÍVEL” ou “nop” dependendo do retorno da função. O programa deve prosseguir a
verificação até que o usuário digite 0 para o segundo número.
'''
def divisivel(a: int, b: int) -> bool:
    if b == 0:
        return False
    return a % b == 0

def exe1():
    x = int(input("Digite o primeiro número (ou 0 para sair): "))
    y = int(input("Digite o segundo número (ou 0 para sair): "))
    while y != 0:
        if divisivel(x, y):
            print("DIVISÍVEL")
        else:
            print("nop")
        x = int(input("Digite o primeiro número (ou 0 para sair): "))
        y = int(input("Digite o segundo número (ou 0 para sair): "))

'''
Escreva uma função que receba como parâmetro o ângulo que uma linha faz com o eixo
positivo X e determina e retorna o quadrante em que essa linha reside. A determinação do
quadrante é dada através da seguinte tabela:
Ângulo com o eixo positivo X Quadrante
Entre 0 e 90 graus 1
Entre 90 e 180 graus 2
Entre 180 e 270 graus 3
Entre 270 e 360 graus 4
Se o ângulo for exatamente 0, 90, 180, ou 270 graus, a linha correspondente não reside em
nenhum quadrante, mas fica em cima de um eixo. Para esta situação, sua função deve retornar
5 para eixo horizontal e 6 para eixo vertical. Um ângulo fora do intervalo entre 0 e 360 deve
resultar no retorno do valor –1. A função principal deve imprimir o número do quadrante, “eixo
vertical” ou “eixo horizontal”, ou ainda “not an angle, man!” dependendo do valor retornado pela
função.

'''

def quadrante(x: float) -> int:
    if x < 0 or x > 360:
        return -1
    elif x == 0 or x == 180 or x == 360:
        return 5
    elif x == 90 or x == 270:
        return 6
    elif 0 < x < 90:
        return 1
    elif 90 < x < 180:
        return 2
    elif 180 < x < 270:
        return 3
    return 4

def exe2():
    angulo = float(input("Digite o ângulo (0-360): "))
    q = quadrante(angulo)
    if q == -1:
        print("not an angle, man!")
    elif q == 5:
        print("eixo horizontal")
    elif q == 6:
        print("eixo vertical")
    else:
        print(f"Quadrante: {q}")


'''
Faça uma função que dado um número n, retorne o n-ésimo número de Fibonacci. O número
de fibonacci é dado por 𝑁 . O programa deve imprimir o
0 = 0, 𝑁
1 = 1, 𝑁
𝑖 = 𝑁
𝑖−1 + 𝑁
𝑖−2
'''
def fibonacci(n: int) -> int:
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
        '''
        a, b = 0, 1
        for _ in range(2, n + 1):
            temp = b
            b = a + b
            a = temp
        return b
        '''
    
def exe3():
    num: int = int(input("Digite um número inteiro não negativo: "))
    fib: int = fibonacci(num)
    if fib == -1:
        print("Número inválido")
    else:
        print(f"O {num}º número de Fibonacci é: {fib}")

'''
Soma dos pares do intervalo
Escreva um programa que contenha uma função que receba dois valores inteiros n1 e n2, e
retorne a soma de todos os valores pares entre n1 e n2 (inclusive ambos, se for o caso). A
função principal deve imprimir o resultado obtido e prosseguir enquanto n1 < n2.
'''
def soma_pares(n1: int, n2: int) -> int:
    soma = 0
    for i in range(n1, n2 + 1):
        if i % 2 == 0:
            soma += i
    return soma

def exe4():
    n1: int = int(input("Digite o primeiro número (n1): "))
    n2: int = int(input("Digite o segundo número (n2): "))
    while n1 < n2:
        resultado: int = soma_pares(n1, n2)
        print(f"A soma dos pares entre {n1} e {n2} é: {resultado}")
        n1 = int(input("Digite o primeiro número (n1): "))
        n2 = int(input("Digite o segundo número (n2): "))

'''
Escreva um programa que contenha um procedimento que recebe como parâmetro um número
inteiro, calcule e retorne a soma de todos os algarismos deste número. O programa deve
imprimir o resultado e prosseguir enquanto o número informado pelo usuário for diferente de
zero.
'''

def soma_algarismos(n: int) -> int:
    soma = 0
    n = abs(n)  # Considera o valor absoluto para lidar com números negativos
    while n > 0:
        soma += n % 10
        n //= 10
    return soma

def exe5():
    numero: int = int(input("Digite um número inteiro (ou 0 para sair): "))
    while numero != 0:
        resultado: int = soma_algarismos(numero)
        print(f"A soma dos algarismos de {numero} é: {resultado}")
        numero = int(input("Digite um número inteiro (ou 0 para sair): "))


'''
Escreva um programa que receba 3 números inteiros e os retorne em ordem crescente – sem
usar a função sort. A função principal deve imprimir o resultado na tela em uma única linha.
'''

def ordena_crescente(a: int, b: int, c: int) -> tuple[int, int, int]:
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c

def exe6():
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))
    c = int(input("Digite o terceiro número inteiro: "))

    a, b, c = ordena_crescente(a, b, c)
    print(f"Números em ordem crescente: {a} {b} {c}")

'''
Escreva um programa que receba 3 números reais, correspondentes aos comprimentos de três
segmentos, e chame uma função que receba estes valores como parâmetros.
Esta função deve retornar “não é um triângulo”, caso os valores dos segmentos informados não
constituam um triângulo. Caso constituam um triângulo, chame outra função que retorne a
classificação angular do triângulo, que pode ser: "acutangulo", "retângulo" ou "obtusangulo". A
função principal deve imprimir o valor retornado e prosseguir enquanto os 3 valores informados
forem positivos.
'''
def tipo_triangulo(a: float, b: float, c: float) -> str:
    if a + b <= c or a + c <= b or b + c <= a:
        return "não é um triângulo"
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "retângulo"
    if a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
        return "obtusangulo"
    return "acutangulo"

def exe7():
    a = float(input("Digite o comprimento do primeiro segmento: "))
    b = float(input("Digite o comprimento do segundo segmento: "))
    c = float(input("Digite o comprimento do terceiro segmento: "))

    while a > 0 and b > 0 and c > 0:
        resultado = tipo_triangulo(a, b, c)
        print(f"Classificação do triângulo: {resultado}")
        a = float(input("Digite o comprimento do primeiro segmento: "))
        b = float(input("Digite o comprimento do segundo segmento: "))
        c = float(input("Digite o comprimento do terceiro segmento: "))

'''
Crie uma função que receba um número inteiro não negativo n e retorne o seu fatorial (n!). O
fatorial de um número é o produto de todos os inteiros de 1 até o próprio número
(5!=5×4×3×2×1). Lembre-se que o fatorial de 0 é 1 (0!=1). O programa principal deve continuar
pedindo números e imprimindo seus fatoriais até que um número negativo seja inserido.
'''

def fatorial_legal(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fatorial_legal(n - 1)
    
def fatorial_iterativo(n: int) -> int:
    if n == 0:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def exe8():
    numero: int = int(input("Digite um número inteiro não negativo (ou negativo para sair): "))
    while numero >= 0:
        resultado: int = fatorial_legal(numero)
        print(f"O fatorial de {numero} é: {resultado}")
        numero = int(input("Digite um número inteiro não negativo (ou negativo para sair): "))

'''
Desenvolva uma função que receba um número inteiro como parâmetro e retorne True se o
número for primo e False caso contrário. Um número primo é aquele que é divisível apenas por
1 e por ele mesmo. O programa principal deve ler um número, chamar a função e exibir uma
mensagem indicando se o número é primo ou não. O programa deve parar quando o usuário
digitar 0.
'''

def eh_primo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def exe9():
    numero: int = int(input("Digite um número inteiro (ou 0 para sair): "))
    while numero != 0:
        if eh_primo(numero):
            print(f"{numero} é primo")
        else:
            print(f"{numero} não é primo")
        numero = int(input("Digite um número inteiro (ou 0 para sair): "))

'''
Faça uma função que receba dois números inteiros como parâmetros: a base e o expoente. A
função deve calcular e retornar o resultado da base elevada ao expoente (sem usar o operador
de potência ** ou a função pow()). O programa principal deve ler a base e o expoente, chamar
a função e imprimir o resultado. O processo se repete até que o valor 0 seja digitado para a
base.
'''

def potencia(base: int, expoente: int) -> int:
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado

def exe10():
    while True:
        base = int(input("Digite a base (ou 0 para sair): "))
        if base == 0:
            break
        expoente = int(input("Digite o expoente: "))
        resultado = potencia(base, expoente)
        print(f"{base} elevado a {expoente} é: {resultado}")


if __name__ == "__main__":
    exercicio: str = input("Qual exercício você quer executar? ")

    while exercicio != "0":
        if exercicio == "1":
            exe1()
        elif exercicio == "2":
            exe2()
        elif exercicio == "3":
            exe3()
        elif exercicio == "4":
            exe4()
        elif exercicio == "5":
            exe5()
        elif exercicio == "6":
            exe6()
        elif exercicio == "7":
            exe7()
        elif exercicio == "8":
            exe8()
        elif exercicio == "9":
            exe9()
        elif exercicio == "10":
            exe10()
        else:
            print("Exercício inválido")
        exercicio = input("Qual exercício você quer executar? ")
