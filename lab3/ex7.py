# Exercício 7 - Preparado(a) para raiz quadrada?
# Calcule a parte inteira da raiz quadrada de um número inteiro positivo sem usar a função sqrt.
# 
# Conceito matemático usado:
# A soma dos primeiros k números ímpares é igual a k²
# Exemplo: 1 + 3 + 5 + 7 + 9 = 25 = 5²
# 
# Algoritmo: Contar quantos números ímpares consecutivos conseguimos somar 
# até chegar próximo (sem ultrapassar) do número n

n = int(input())

# Variáveis de controle
soma = 0           # Soma acumulada dos números ímpares
contador = 0       # Quantidade de números ímpares somados (será nossa resposta)
numero_impar = 1   # Próximo número ímpar a ser somado (1, 3, 5, 7, ...)

# Loop: soma números ímpares enquanto não ultrapassar n
while soma + numero_impar <= n:
    soma += numero_impar    # Adiciona o número ímpar atual à soma
    contador += 1           # Incrementa a contagem
    numero_impar += 2       # Próximo número ímpar (1→3, 3→5, 5→7, ...)

# O contador representa a parte inteira da raiz quadrada de n
print(contador)
