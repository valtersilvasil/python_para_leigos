# Bloco 1: Solicita o valor da compra e o percentual de desconto
# Primeiro, pedimos ao usuário para digitar o valor da compra e convertemos essa entrada para um número decimal.
valor_compra = float(input("Digite o valor da compra: R$ "))
# Pedimos ao usuário para informar o percentual de desconto e também convertendo para decimal dividindo por 100.
percentual_desconto = float(input("Digite o percentual de desconto: ")) / 100  # Converte para decimal

# Bloco 2: Calcula o valor do desconto
# Aqui, calculamos o valor do desconto multiplicando o valor da compra pelo percentual de desconto.
desconto = valor_compra * percentual_desconto

# Bloco 3: Exibe o valor do desconto e o total final
# Calculamos o valor final da compra subtraindo o valor do desconto do valor original da compra.
valor_final = valor_compra - desconto
# Imprimimos o valor do desconto formatado com duas casas decimais.
print(f"Desconto: R$ {desconto:.2f}")
# Imprimimos o valor final da compra, também formatado com duas casas decimais.
print(f"Valor final da compra: R$ {valor_final:.2f}")

