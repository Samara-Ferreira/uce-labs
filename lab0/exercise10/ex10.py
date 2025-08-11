# --- Exercício a) Boomerang ---

# 1. Solicita que o usuário digite um nome e armazena o valor na variável 'nome'.
# A função input() lê uma linha de entrada do teclado e a converte em uma string.
nome = input("Digite um nome: ")

# 2. Imprime o nome que foi armazenado.
# A função print() exibe o valor da variável 'nome' na tela.
print("O nome digitado foi:", nome)


# --- Exercício b) Qual o dobro? ---

# 1. Solicita que o usuário digite um número inteiro.
# O valor lido pela função input() é inicialmente uma string.
entrada_usuario = input("Digite um número inteiro positivo: ")

# 2. Converte a entrada (que é uma string) para um número inteiro.
# A função int() transforma a string de texto em um número inteiro para que possamos fazer cálculos.
numero_inteiro = int(entrada_usuario)

# 3. Calcula o dobro do número.
# Multiplicamos o número por 2 e armazenamos o resultado na variável 'dobro'.
dobro = numero_inteiro * 2

# 4. Imprime o resultado final.
# Usamos uma f-string para formatar a saída de forma clara.
print(f"O dobro de {numero_inteiro} é {dobro}.")
