def traduzir_natal(pais, traducoes):
    return traducoes.get(pais, "--- Não Encontrado ---")

def exercicio6():
    natal = {
        "brasil": "Feliz Natal!",
        "alemanha": "Frohliche Weihnachten!",
        "austria": "Frohe Weihnacht!",
        "coreia": "Chuk Sung Tan!",
        "espanha": "Feliz Navidad!",
        "grecia": "Kala Christougena!",
        "estados-unidos": "Merry Christmas!",
        "inglaterra": "Merry Christmas!",
        "australia": "Merry Christmas!",
        "portugal": "Feliz Natal!",
        "suecia": "God Jul!",
        "irlanda": "Nollaig Shona Dhuit!",
        "siria": "Milad Mubarak!",
        "belgica": "Zalig Kerstfeest!",
        "japao": "Merii Kurisumasu!",
        "turquia": "Mutlu Noeller",
        "argentina": "Feliz Navidad!",
        "chile": "Feliz Navidad!",
        "italia": "Buon Natale!",
        "canada": "Merry Christmas!"
    }

    pais = input("Digite o nome do país: ").lower()
    print(traduzir_natal(pais, natal))
