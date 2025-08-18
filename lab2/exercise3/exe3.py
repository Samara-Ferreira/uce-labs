'''
Escreva um programa que converta uma temperatura da escala Celsius para Fahrenheit ou
vice-versa. Use a seguinte equação para conversão:
𝐶 = 5/9 * (𝐹 − 32)
Para isso, você deverá ler duas entradas:
1. escala em que a temperatura está representada: C para Celsius, ou F para Fahrenheit.
2. valor da temperatura.
Como saída, imprima:
● a temperatura convertida para a outra escala, arredondada em uma casa decimal.
'''

escala = input("Digite a escala (C para Celsius, F para Fahrenheit): ").strip().upper()
temperatura = float(input("Digite o valor da temperatura: "))

if escala == "C":
    # Converter de Celsius para Fahrenheit
    temperatura_convertida = (temperatura * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {temperatura_convertida:.1f}")
elif escala == "F":
    # Converter de Fahrenheit para Celsius
    temperatura_convertida = 5/9 * (temperatura - 32)
    print(f"A temperatura em Celsius é: {temperatura_convertida:.1f}")
else:
    print("Escala inválida. Por favor, digite 'C' ou 'F'.")
