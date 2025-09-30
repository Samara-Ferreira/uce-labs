def calcula_delta(a, b, c):
    # Calcula o discriminante (Delta) da equação do 2º grau
    return b**2 - 4*a*c

def main():
    # Lê os coeficientes da equação
    a = int(input())
    b = int(input())
    c = int(input())

    delta = calcula_delta(a, b, c)

    # Verifica a quantidade de raízes reais
    if delta < 0:
        print("não existem raízes reais")
    elif delta == 0:
        print("existe uma única raiz")
    else:
        print("existem duas raizes reais")

if __name__ == "__main__":
    main()