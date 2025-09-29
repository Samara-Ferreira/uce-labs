from functions import celsius_para_fahrenheit

try:
    temp_celsius = float(input("Digite a temperatura em Celsius: "))
    temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)
    print(f"A temperatura em Fahrenheit é: {temp_fahrenheit:.2f} °F")
except ValueError:
    print("Por favor, digite um número válido.")