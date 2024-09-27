# Bloco 1: Função que converte Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Bloco 2: Solicita ao usuário a temperatura em Celsius
temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

# Bloco 3: Converte para Fahrenheit
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

# Bloco 4: Exibe o resultado
print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit:.2f}")
