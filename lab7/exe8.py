import functions

while True:
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Listar tarefas")
    print("2. Adicionar tarefa")
    print("3. Remover tarefa")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        lista = functions.listar()
        if lista:
            print("\nLista de Tarefas:")
            for i, tarefa in enumerate(lista, start=1):
                print(f"{i}. {tarefa}")
        else:
            print("\nNenhuma tarefa na lista.")

    elif opcao == "2":
        nova_tarefa = input("Digite a nova tarefa: ")
        functions.adicionar(nova_tarefa)
        print(f"Tarefa '{nova_tarefa}' adicionada com sucesso!")

    elif opcao == "3":
        lista = functions.listar()
        if not lista:
            print("\nNenhuma tarefa para remover.")
            continue

        for i, tarefa in enumerate(lista, start=1):
            print(f"{i}. {tarefa}")

        try:
            numero = int(input("Digite o número da tarefa que deseja remover: "))
            mensagem = functions.remover(numero - 1)
            print(mensagem)
        except ValueError:
            print("Por favor, digite um número válido.")

    elif opcao == "4":
        print("Saindo do gerenciador de tarefa2s...")
        break

    else:
        print("Opção inválida. Digite 1, 2, 3 ou 4.")
