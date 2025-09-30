def calcula_fct(idade, fcr):
    # Calcula a frequência cardíaca mínima de treinamento para potência aeróbica
    return fcr + 0.6 * (220 - idade - fcr)

def main():
    # Repete enquanto idade não for negativa
    idade = int(input())
    while idade >= 0:
        fcr = int(input())
        fct = calcula_fct(idade, fcr)
        print(int(fct))
        idade = int(input())

if __name__ == "__main__":
    main()