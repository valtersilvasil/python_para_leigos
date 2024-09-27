# Bloco 1: Define os valores da compra e o imposto
# Solicita ao usuário para digitar o valor da compra.
# A função float() é usada para garantir que o valor seja um número decimal (com casas decimais).
valor_compra = float(input("Digite o valor da compra: R$ "))
imposto = 0.1  # 10% de imposto

# Bloco 2: Calcula o valor final com imposto
# Calculamos o valor final da compra, somando o valor da compra ao imposto.
# O imposto é calculado multiplicando o valor da compra por 0.1 (10%).
valor_final = valor_compra + (valor_compra * imposto)

# Bloco 3: Exibe a fatura com o valor total
# Usamos a função print() para exibir o valor total da fatura ao usuário.
# {:.2f} formata o número para mostrar sempre duas casas decimais.
print(f"O valor total da fatura, incluindo imposto, é: R$ {valor_final:.2f}")

