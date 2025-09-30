# Exercício 3 – Gerenciador de Tarefas
# Objetivo: Criar um programa para gerenciar uma lista de tarefas com operações de remoção

# Lista inicial com 5 tarefas predefinidas
tarefas = [
    "Estudar Python",
    "Fazer exercícios de programação",
    "Ler documentação",
    "Praticar algoritmos",
    "Revisar conceitos de listas"
]

print("=== GERENCIADOR DE TAREFAS ===")
print("Lista inicial de tarefas:")
for i, tarefa in enumerate(tarefas, 1):
    print(f"{i}. {tarefa}")

# Solicita ao usuário o nome da tarefa a ser removida
tarefa_remover = input("\nDigite o nome da tarefa que deseja remover: ")

# Verifica se a tarefa existe na lista
if tarefa_remover in tarefas:
    tarefas.remove(tarefa_remover)
    print(f"\nTarefa '{tarefa_remover}' removida com sucesso!")
    print("\nLista atualizada de tarefas:")
    if tarefas:  # Verifica se ainda há tarefas na lista
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa restante na lista.")
else:
    print(f"\nErro: A tarefa '{tarefa_remover}' não foi encontrada na lista.")
    print("Lista de tarefas permanece inalterada:")
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")