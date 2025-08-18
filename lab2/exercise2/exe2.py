'''
No universo do livro Harry Potter, o Expecto Patronum é um feitiço que cria um guardião
composto de energia positiva, na forma de um animal prateado, único para cada bruxo.
Escreva um programa que leia o nome do patrono.
Como saída:
1. Se o patrono for cervo, exiba a mensagem: “Cervo é o patrono do Harry Potter”.
2. Caso contrário, exiba a mensagem “<entrada> não é patrono do Harry Potter”,
substituindo a expressão <entrada> pela string fornecida como entrada.
'''

patrono = input("Digite o nome do patrono: ")
if patrono.lower().strip() == "cervo":
    print("Cervo é o patrono do Harry Potter.")
else:
    print(f"{patrono} não é patrono do Harry Potter.")
