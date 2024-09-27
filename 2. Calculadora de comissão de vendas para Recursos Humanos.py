# Bloco 1: Define o total de vendas e a taxa de comissão
total_vendas = float(input("Digite o total de vendas: R$ "))
taxa_comissao = float(input("Digite a taxa de comissão (em %): ")) / 100  # Converte para decimal

# Bloco 2: Calcula a comissão
comissao = total_vendas * taxa_comissao

# Bloco 3: Exibe o valor da comissão
print(f"O valor da comissão é: R$ {comissao:.2f}")
