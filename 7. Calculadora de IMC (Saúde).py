# Bloco 1: Solicita o peso e a altura
# Aqui, solicitamos ao usuário que insira seu peso em quilogramas (kg)
# e sua altura em metros (m). As entradas são convertidas para o tipo float,
# que permite números decimais.
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

# Bloco 2: Calcula o IMC
# O IMC (Índice de Massa Corporal) é calculado dividindo o peso pela altura
# ao quadrado. A fórmula é: IMC = peso / (altura ** 2).
imc = peso / (altura ** 2)

# Bloco 3: Classifica o IMC
# Aqui, utilizamos uma estrutura condicional (if-elif-else) para classificar
# o IMC de acordo com os padrões de saúde.
if imc < 18.5:
    classificacao = "Abaixo do peso"  # Se o IMC é menor que 18.5, está abaixo do peso.
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"  # Se o IMC está entre 18.5 e 24.9, é considerado peso normal.
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"  # Se o IMC está entre 25 e 29.9, a pessoa está com sobrepeso.
else:
    classificacao = "Obesidade"  # Se o IMC é 30 ou mais, é considerado obesidade.

# Bloco 4: Exibe o IMC e a classificação
# Finalmente, imprimimos o IMC calculado e a classificação correspondente.
print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")

