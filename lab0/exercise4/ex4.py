# Exercício 4 – Arredondamento
# 6 amigos; conta total R$250 dividida igualmente.
conta_total = 250
amigos = 6
valor_bruto = conta_total / amigos 

# Arredonda para duas casas decimais.
valor_arredondado = round(valor_bruto, 2)

# Formata com no máximo duas casas (remove zeros finais desnecessários)
print("Cada amigo deve pagar: R$", valor_arredondado)
