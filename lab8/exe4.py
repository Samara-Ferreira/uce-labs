def traduzir_giria(giria, glossario):
    return glossario.get(giria, "Essa gíria não foi encontrada no dicionário.")

glossario_girias = {
    "tankar": "aguentar uma situação difícil",
    "cringe": "algo vergonhoso ou ultrapassado",
    "shippar": "torcer por um casal",
    "bolado": "estar impressionado ou bravo",
}
giria = input("Digite a gíria: ").lower()
print(traduzir_giria(giria, glossario_girias))
