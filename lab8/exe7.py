contas = {}

def criar_conta():
    nome = input("Digite seu nome de usuário: ")
    if nome in contas:
        print("Usuário já existe.")
        return
    senha = input("Crie uma senha: ")
    contas[nome] = {"senha": senha, "saldo": 0.0}
    print("Conta criada com sucesso!")

def entrar():
    nome = input("Usuário: ")
    senha = input("Senha: ")
    if nome in contas and contas[nome]["senha"] == senha:
        menu_conta(nome)
    else:
        print("Usuário ou senha incorretos.")

def ler_saldo(nome):
    print(f"Saldo atual: R$ {contas[nome]['saldo']:.2f}")

def depositar(nome):
    valor = float(input("Valor para depositar: "))
    contas[nome]["saldo"] += valor
    print("Depósito realizado com sucesso.")

def sacar(nome):
    valor = float(input("Valor para sacar: "))
    if valor <= contas[nome]["saldo"]:
        contas[nome]["saldo"] -= valor
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente.")

def transferir(nome):
    destino = input("Conta de destino: ")
    valor = float(input("Valor para transferir: "))
    if destino in contas and contas[nome]["saldo"] >= valor:
        contas[nome]["saldo"] -= valor
        contas[destino]["saldo"] += valor
        print("Transferência concluída.")
    else:
        print("Erro na transferência.")

def menu_conta(nome):
    while True:
        print("\n1. Ler saldo\n2. Depositar\n3. Sacar\n4. Transferir\n5. Sair")
        op = input("Escolha: ")
        if op == "1":
            ler_saldo(nome)
        elif op == "2":
            depositar(nome)
        elif op == "3":
            sacar(nome)
        elif op == "4":
            transferir(nome)
        elif op == "5":
            return
        else:
            print("Opção inválida.")

def exercicio7():
    while True:
        print("\n1. Entrar\n2. Inscrever-se\n3. Sair")
        op = input("Escolha: ")
        if op == "1":
            entrar()
        elif op == "2":
            criar_conta()
        elif op == "3":
            return
        else:
            print("Opção inválida.")

exercicio7()
