def calcular_media(notas):
    return sum(notas.values()) / len(notas)

def verificar_aprovacoes(notas, corte=6.0):
    for nome in notas:
        situacao = "Aprovado(a)" if notas[nome] >= corte else "Reprovado(a)"
        print(f"{nome}: {situacao}")


notas_turma = {
    "Marcos": 8.5,
    "Júlia": 9.0,
    "Pedro": 5.5,
    "Maria": 4.0
}
media = calcular_media(notas_turma)
print(f"Média da turma: {media:.2f}")
verificar_aprovacoes(notas_turma)
