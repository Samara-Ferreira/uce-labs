from functions import calcular_media, encontrar_maior_nota

# Listas de exemplo
nome_dos_estudantes = ["Alice", "Bruno", "Carla", "Daniel"]
notas_do_exame = [7.5, 9.0, 8.2, 10.0]

# Cálculos usando funções do módulo utilidades
media = calcular_media(notas_do_exame)
maior_nota, indice = encontrar_maior_nota(notas_do_exame)
estudante_maior_nota = nome_dos_estudantes[indice]

# Exibindo resultados
print(f"A média de nota foi: {media:.1f}; A nota mais alta foi {maior_nota:.1f}, alcançada pelo estudante {estudante_maior_nota}.")
