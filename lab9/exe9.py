# --- Função para imprimir o tabuleiro de forma organizada ---
def imprimir_tabuleiro(tabuleiro):
    print("Tabuleiro:")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)  # linha divisória

# --- Função para verificar vencedor na diagonal principal ---
def verificar_vencedor_diagonal(tabuleiro):
    # Símbolo da primeira posição da diagonal
    simbolo = tabuleiro[0][0]
    
    if simbolo == ' ':
        return None  # não pode haver vencedor se for vazio
    
    # Verifica os outros elementos da diagonal
    for i in range(1, 3):
        if tabuleiro[i][i] != simbolo:
            return None  # algum símbolo diferente
    
    return simbolo  # todos iguais, há vencedor

# --- Criando o tabuleiro de exemplo ---
tabuleiro = [
    ['X', 'O', 'O'],
    ['O', 'X', ' '],
    ['O', 'X', 'X']
]

# --- Imprime o tabuleiro ---
imprimir_tabuleiro(tabuleiro)

# --- Verifica vencedor na diagonal principal ---
vencedor = verificar_vencedor_diagonal(tabuleiro)

# --- Exibe resultado ---
if vencedor:
    print(f"O jogador '{vencedor}' venceu na diagonal principal!")
else:
    print("Não houve vencedor na diagonal principal.")
