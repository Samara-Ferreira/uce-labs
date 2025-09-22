def filtrar_palavras(texto, bloqueadas):
    palavras = texto.split()  # separa o texto em palavras
    for i in range(len(palavras)):
        if palavras[i] in bloqueadas:  # se a palavra estiver na lista de bloqueadas
            palavras[i] = "***"        # substitui por ***
    return " ".join(palavras)         # junta tudo de volta em uma string

#
texto = "O jogo de Minecraft é muito divertido mas alguns consideram muito viciante"
palavras_bloqueadas = ["viciante", "divertido"]

resultado = filtrar_palavras(texto, palavras_bloqueadas)
print(resultado)
