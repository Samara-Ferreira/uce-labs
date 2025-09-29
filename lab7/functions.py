import statistics

def celsius_para_fahrenheit(temperatura_celsius):
    """Converte temperatura em Celsius para Fahrenheit"""
    return (temperatura_celsius * 9/5) + 32

# ===============================================================
# Funções adicionais para o exercício 5
#================================================================

def calcular_media(notas):
    """Calcula a média de uma lista de números"""
    return statistics.mean(notas)

def encontrar_maior_nota(notas):
    """
    Retorna a maior nota e o índice do estudante que a obteve.
    """
    maior_nota = max(notas)
    indice = notas.index(maior_nota)
    return maior_nota, indice

# ===============================================================
# Funções adicionais para o exercício 8
#================================================================

# Lista que armazena as tarefas
lista_de_tarefas = []

def adicionar(tarefa):
    """Adiciona uma tarefa à lista"""
    lista_de_tarefas.append(tarefa)

def remover(indice):
    """Remove uma tarefa pelo índice, se válido"""
    if 0 <= indice < len(lista_de_tarefas):
        removida = lista_de_tarefas.pop(indice)
        return f"Tarefa '{removida}' removida com sucesso."
    else:
        return "Índice inválido. Nenhuma tarefa removida."

def listar():
    """Retorna a lista completa de tarefas"""
    return lista_de_tarefas

