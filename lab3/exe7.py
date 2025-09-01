'''
Calcule a parte inteira da raiz quadrada de um número inteiro positivo sem usar a função sqrt.
Para isso, você precisa saber que a raiz quadrada de um número n é igual aproximadamente
à quantidade de números ímpares consecutivos (a partir do 1) cuja soma é igual a n (ou o
mais próxima possível de n).

'''

n = int(input("Digite um inteiro positivo: "))

soma = 0
k = 0

for impar in range(1, n+1, 2):  # percorre ímpares: 1, 3, 5, ...
    soma += impar
    if soma <= n:
        k += 1

print(k)  
