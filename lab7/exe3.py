from datetime import date

# Entrada de dados
ano = int(input("Digite o ano do seu nascimento (YYYY): "))
mes = int(input("Digite o mês do seu nascimento (MM): "))
dia = int(input("Digite o dia do seu nascimento (DD): "))

# Criando o objeto date para nascimento
data_nascimento = date(ano, mes, dia)

# Data atual
data_atual = date.today()

# Diferença entre as datas (objeto timedelta)
diferenca = data_atual - data_nascimento

# Exibe a quantidade de dias
print(f"Você viveu aproximadamente {diferenca.days} dias até hoje.")
