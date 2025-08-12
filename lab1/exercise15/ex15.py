# Exercício 15 – Contabilizando Pokémons

# Lê os valores de entrada em 6 linhas
print("Digite os valores para cada região:")

# Primeiras 3 linhas: quantidades atuais de pokémons registrados
kanto_atual = int(input("Kanto (atual): "))
johto_atual = int(input("Johto (atual): "))
hoenn_atual = int(input("Hoenn (atual): "))

# Próximas 3 linhas: quantidades de novos pokémons descobertos
kanto_novos = int(input("Kanto (novos): "))
johto_novos = int(input("Johto (novos): "))
hoenn_novos = int(input("Hoenn (novos): "))

# Calcula o total de pokémons para cada região após a nova contagem
kanto_total = kanto_atual + kanto_novos
johto_total = johto_atual + johto_novos
hoenn_total = hoenn_atual + hoenn_novos

# Imprime os resultados na ordem solicitada (Kanto, Johto e Hoenn)
print(f"{kanto_total}")
print(f"{johto_total}")
print(f"{hoenn_total}")
