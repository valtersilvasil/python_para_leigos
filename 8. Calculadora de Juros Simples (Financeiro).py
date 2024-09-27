# Bloco 1: Função para calcular juros simples
# Definimos uma função chamada 'calcula_juros_simples', que recebe três parâmetros:
# 'capital' (o valor inicial), 'taxa' (a taxa de juros) e 'tempo' (o tempo em meses).
def calcula_juros_simples(capital, taxa, tempo):
    # A função calcula os juros simples usando a fórmula: juros = capital * taxa * tempo.
    return capital * taxa * tempo

# Bloco 2: Solicita dados do usuário
# Aqui, pedimos ao usuário que insira o capital inicial, a taxa de juros e o tempo em meses.
capital = float(input("Digite o capital inicial: R$ "))  # O capital deve ser um número decimal.
taxa = float(input("Digite a taxa de juros (em %): ")) / 100  # A taxa é convertida de porcentagem para decimal.
tempo = int(input("Digite o tempo (em meses): "))  # O tempo deve ser um número inteiro.

# Bloco 3: Calcula os juros
# Chamamos a função 'calcula_juros_simples' passando os dados informados pelo usuário
# e armazenamos o resultado na variável 'juros'.
juros = calcula_juros_simples(capital, taxa, tempo)

# Bloco 4: Exibe o valor dos juros
# Por fim, mostramos ao usuário o valor calculado dos juros simples.
print(f"O valor dos juros simples é: R$ {juros:.2f}")  # Exibe o resultado formatado com duas casas decimais.

