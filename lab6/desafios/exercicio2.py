# Exercício 2 – Jogo de exploração
# Objetivo: Criar um jogo de aventura baseado em texto usando listas para simular entrar e sair de salas

import random

def exibir_menu():
    """Exibe o menu de opções do jogo"""
    print("\n=== MENU DE EXPLORAÇÃO ===")
    print("1. Explorar uma nova sala")
    print("2. Ver salas visitadas")
    print("3. Ver resumo da exploração")
    print("4. Converter temperatura (Desafio Extra)")
    print("5. Sair do jogo")
    return input("Escolha uma opção (1-5): ")

def converter_temperatura():
    """Desafio Extra: Converte temperatura de Fahrenheit para Celsius"""
    print("\n=== CONVERSOR DE TEMPERATURA ===")
    try:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        print("Erro: Digite um número válido!")

def main():
    # Etapa 1: Criar Lista de Salas
    salas_calabouco = [
        "Entrada do Calabouço",
        "Corredor Sombrio", 
        "Sala do Tesouro",
        "Masmorra Antiga",
        "Biblioteca Misteriosa",
        "Câmara Secreta",
        "Sala dos Espelhos",
        "Laboratório do Alquimista",
        "Cripta Assombrada",
        "Salão Principal"
    ]
    
    # Descrições das salas (Desafio Extra)
    descricoes_salas = {
        "Entrada do Calabouço": "Uma entrada úmida com tochas tremeluzentes nas paredes.",
        "Corredor Sombrio": "Um corredor estreito com ecos misteriosos.",
        "Sala do Tesouro": "Uma sala brilhante cheia de moedas douradas e joias.",
        "Masmorra Antiga": "Celas enferrujadas com correntes penduradas.",
        "Biblioteca Misteriosa": "Estantes altas repletas de livros empoeirados.",
        "Câmara Secreta": "Uma sala oculta com símbolos estranhos nas paredes.",
        "Sala dos Espelhos": "Espelhos por toda parte, criando reflexos infinitos.",
        "Laboratório do Alquimista": "Frascos borbulhantes e ingredientes exóticos.",
        "Cripta Assombrada": "Tumbas antigas com uma aura sobrenatural.",
        "Salão Principal": "Um grande salão com um trono imponente."
    }
    
    # Etapa 2: Rastrear salas exploradas
    salas_visitadas = []
    
    print("🏰 BEM-VINDO AO JOGO DE EXPLORAÇÃO DO CALABOUÇO! 🏰")
    print("Explore as salas místicas e descubra seus segredos!")
    
    while True:
        opcao = exibir_menu()
        
        if opcao == "1":
            # Etapa 3: Explorar o calabouço
            if len(salas_visitadas) == len(salas_calabouco):
                print("\n🎉 Parabéns! Você explorou todas as salas do calabouço!")
                decisao = input("Deseja reiniciar a exploração? (s/n): ").lower()
                if decisao == 's':
                    salas_visitadas.clear()
                    print("Exploração reiniciada!")
                    continue
                else:
                    continue
            
            # Escolhe uma sala aleatória que ainda não foi visitada
            salas_disponiveis = [sala for sala in salas_calabouco if sala not in salas_visitadas]
            sala_atual = random.choice(salas_disponiveis)
            
            print(f"\n🚪 Você entrou na: {sala_atual}")
            print(f"📜 {descricoes_salas[sala_atual]}")
            
            # Adiciona à lista de salas visitadas
            salas_visitadas.append(sala_atual)
            
            print(f"✅ Salas exploradas: {len(salas_visitadas)}/{len(salas_calabouco)}")
            
        elif opcao == "2":
            # Mostrar salas visitadas
            if not salas_visitadas:
                print("\n❌ Você ainda não visitou nenhuma sala.")
            else:
                print(f"\n📍 SALAS VISITADAS ({len(salas_visitadas)}):")
                for i, sala in enumerate(salas_visitadas, 1):
                    print(f"  {i}. {sala}")
                    
        elif opcao == "3":
            # Etapa 4: Imprimir Resumo da Exploração
            print("\n📊 === RESUMO DA EXPLORAÇÃO ===")
            print(f"Total de salas no calabouço: {len(salas_calabouco)}")
            print(f"Salas visitadas: {len(salas_visitadas)}")
            print(f"Salas restantes: {len(salas_calabouco) - len(salas_visitadas)}")
            
            if salas_visitadas:
                print("\n🗺️ Ordem de exploração:")
                for i, sala in enumerate(salas_visitadas, 1):
                    print(f"  {i}º - {sala}")
            
            if len(salas_visitadas) < len(salas_calabouco):
                salas_nao_visitadas = [sala for sala in salas_calabouco if sala not in salas_visitadas]
                print(f"\n🔍 Salas ainda não exploradas: {', '.join(salas_nao_visitadas)}")
            else:
                print("\n🏆 EXPLORAÇÃO COMPLETA! Todas as salas foram visitadas!")
                
        elif opcao == "4":
            # Desafio Extra: Conversor de temperatura
            converter_temperatura()
            
        elif opcao == "5":
            print("\n👋 Obrigado por jogar! Até a próxima aventura!")
            break
            
        else:
            print("\n❌ Opção inválida! Escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    main()