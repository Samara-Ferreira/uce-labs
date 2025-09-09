# Exercício 11 - Sequência de Fibonacci
# Programa que gera os primeiros N termos da sequência de Fibonacci

n = int(input("Digite quantos termos da sequência de Fibonacci deseja ver: "))

if n <= 0:
    print("Por favor, digite um número positivo!")
elif n == 1:
    print("Sequência de Fibonacci:")
    print("1º termo: 0")
elif n == 2:
    print("Sequência de Fibonacci:")
    print("1º termo: 0")
    print("2º termo: 1")
else:
    print(f"\nPrimeiros {n} termos da sequência de Fibonacci:")
    
    # Primeiros dois termos
    termo1, termo2 = 0, 1
    
    print(f"1º termo: {termo1}")
    print(f"2º termo: {termo2}")
    
    # Calcular e mostrar os próximos termos
    for i in range(3, n + 1):
        proximo_termo = termo1 + termo2
        print(f"{i}º termo: {proximo_termo}")
        
        # Atualizar para próxima iteração
        termo1 = termo2
        termo2 = proximo_termo
    
    # Mostrar a sequência completa em uma linha
    print(f"\nSequência completa: ", end="")
    a, b = 0, 1
    print(a, end="")
    
    if n > 1:
        print(f", {b}", end="")
        
    for i in range(2, n):
        c = a + b
        print(f", {c}", end="")
        a, b = b, c
    
    print()  # Nova linha no final
