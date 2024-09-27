# Bloco 1: Lista de produtos e seus estoques
# Criamos uma lista chamada 'estoque' que contém tuplas.
# Cada tupla representa um produto e a quantidade disponível desse produto.
estoque = [("Produto A", 10), ("Produto B", 3), ("Produto C", 7)]

# Bloco 2: Define o limite mínimo de estoque
# Aqui, definimos um limite mínimo para o estoque.
# Se a quantidade de um produto ficar abaixo desse limite, precisamos ser alertados.
limite_minimo = 5

# Bloco 3: Loop para verificar o estoque de cada produto
# Usamos um loop 'for' para percorrer cada produto e sua quantidade na lista de estoque.
for produto, quantidade in estoque:
    # Verificamos se a quantidade do produto é menor que o limite mínimo definido.
    if quantidade < limite_minimo:
        # Se a quantidade estiver abaixo do limite, exibimos um aviso.
        print(f"Atenção! {produto} está abaixo do limite mínimo com {quantidade} unidades.")
    else:
        # Se a quantidade estiver adequada, informamos que o estoque está bom.
        print(f"{produto} está com estoque adequado: {quantidade} unidades.")
