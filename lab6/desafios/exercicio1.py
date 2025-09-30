# Exercício 1 – Criptografia
# Objetivo: Implementar a Cifra de Atbash para codificar e decodificar mensagens

def cifra_atbash(texto):
    """
    Aplica a Cifra de Atbash em um texto.
    A cifra substitui cada letra pela sua "oposta" no alfabeto:
    a->z, b->y, c->x, d->w, etc.
    """
    resultado = ""
    
    for char in texto:
        if char.isalpha():  # Verifica se é uma letra
            if char.islower():  # Letra minúscula
                # Converte: a=0, b=1, ..., z=25
                posicao = ord(char) - ord('a')
                # Inverte: 0->25, 1->24, ..., 25->0
                nova_posicao = 25 - posicao
                # Converte de volta para letra
                nova_letra = chr(ord('a') + nova_posicao)
                resultado += nova_letra
            else:  # Letra maiúscula
                # Mesmo processo para maiúsculas
                posicao = ord(char) - ord('A')
                nova_posicao = 25 - posicao
                nova_letra = chr(ord('A') + nova_posicao)
                resultado += nova_letra
        else:
            # Mantém caracteres que não são letras (espaços, pontuação, etc.)
            resultado += char
    
    return resultado

# Programa principal
print("=== CIFRA DE ATBASH ===")
print("A Cifra de Atbash substitui cada letra pela sua 'oposta' no alfabeto:")
print("a ↔ z, b ↔ y, c ↔ x, d ↔ w, etc.")
print()

# Demonstração dos exemplos
print("Exemplos de codificação:")
print("a vira z")
print("b vira y") 
print("c vira x")
print("z vira a...")
print()

# Entrada do usuário
frase = input("Digite uma frase para codificar/decodificar: ")

# Aplica a cifra
frase_codificada = cifra_atbash(frase)

# Saída
print(f"\nFrase original: {frase}")
print(f"Frase codificada: {frase_codificada}")

# Demonstração de que a cifra é reversível
print(f"\nDecodificando novamente: {cifra_atbash(frase_codificada)}")

# Teste com exemplos específicos
print("\n=== TESTES ADICIONAIS ===")
testes = ["python", "HELLO", "abc xyz", "Programação123!"]

for teste in testes:
    codificado = cifra_atbash(teste)
    decodificado = cifra_atbash(codificado)
    print(f"Original: '{teste}' → Codificado: '{codificado}' → Decodificado: '{decodificado}'")