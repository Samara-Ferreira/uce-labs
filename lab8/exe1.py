def encontrar_grupo(aluno, grupos):
    for i in range(len(grupos)):
        grupo = grupos[i]
        if aluno in grupo:
            return f"O aluno '{aluno}' está no Grupo {chr(97 + i)}."
    return "Aluno não encontrado."


grupo_a = ("Ana", "Bruno", "Carla")
grupo_b = ("Daniel", "Eduarda", "Felipe")
grupo_c = ("Gabriela", "Henrique", "Isabela")
grupo_d = ("João", "Karen", "Lucas")

todos_os_grupos = [grupo_a, grupo_b, grupo_c, grupo_d]

aluno = input("Digite o nome do aluno: ")
print(encontrar_grupo(aluno, todos_os_grupos))
