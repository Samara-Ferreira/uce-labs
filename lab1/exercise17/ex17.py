# Exercício 17 – Número CDU

# Lê o número de três algarismos
N = int(input("Digite um número de três algarismos: "))

# Extrai os dígitos do número
# C (centenas) = primeiro dígito
# D (dezenas) = segundo dígito
# U (unidades) = terceiro dígito

C = N // 100        # Centenas: divisão inteira por 100
D = (N // 10) % 10  # Dezenas: divisão inteira por 10, depois resto por 10
U = N % 10          # Unidades: resto da divisão por 10

# Imprime os dígitos na ordem inversa (U D C), separados por espaços
print(f"{U} {D} {C}")
