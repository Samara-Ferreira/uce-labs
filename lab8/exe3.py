def mostrar_fronteiras(estado, fronteiras):
    if estado in fronteiras:
        for e in fronteiras[estado]:
            print(e)
    else:
        print("Estado não encontrado.")

def exercicio3():
    fronteiras = {
        "MA": ["PA", "TO", "PI"],
        "PI": ["MA", "CE", "PE", "BA", "TO"],
        "CE": ["PI", "PE", "PB", "RN"],
        "RN": ["CE", "PB"],
        "PB": ["CE", "RN", "PE"],
        "PE": ["CE", "PB", "AL", "BA", "PI"],
        "AL": ["PE", "SE", "BA"],
        "SE": ["AL", "BA"],
        "BA": ["PI", "PE", "AL", "SE", "ES", "MG", "GO", "TO"]
    }
    sigla = input("Digite a sigla do estado: ").upper()
    mostrar_fronteiras(sigla, fronteiras)
exercicio3()