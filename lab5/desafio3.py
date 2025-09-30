def eh_palindromo(palavra):
    # Retorna True se a palavra for um palíndromo
    return palavra == palavra[::-1]

def main():
    while True:
        palavra = input()
        if palavra == "fim":
            print("(programa encerra)")
            break
        if eh_palindromo(palavra):
            print("É um palíndromo")
        else:
            print("Não é um palíndromo")

if __name__ == "__main__":
    main()