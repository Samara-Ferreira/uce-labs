# Lê o primeiro número
numero = int(input("Digite um número: "))

while numero >= 0:
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print("PAR")
    else:
        print("ÍMPAR")
    
    # Lê o próximo número
    numero = int(input("Digite um número: "))

print("Programa encerrado.")
