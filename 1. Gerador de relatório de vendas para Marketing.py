# Bloco 1: Lista de vendas com região e valor
vendas = [("Sul", 1200), ("Norte", 1000), ("Centro-Oeste", 700), ("Sul", 450), ("Norte", 800)]

# Bloco 2: Dicionário para somar vendas por região
total_por_regiao = {}

# Bloco 3: Loop para calcular o total por região
for regiao, valor in vendas:
    if regiao in total_por_regiao:
        total_por_regiao[regiao] += valor  # Soma valor para a região
    else:
        total_por_regiao[regiao] = valor  # Adiciona nova região no dicionário

# Bloco 4: Exibe o relatório de vendas por região
print("Relatório de Vendas por Região:")
for regiao, total in total_por_regiao.items():
    print(f"Região {regiao}: R$ {total}")




