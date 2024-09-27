# Bloco 1: Lista de notas dos alunos
# Neste bloco, estamos criando uma lista que irá armazenar as notas dos alunos.
# Usamos uma compreensão de lista para coletar 3 notas do usuário.
notas = [float(input(f"Digite a nota {i+1}: ")) for i in range(3)]  # Pede para o usuário digitar 3 notas.

# Bloco 2: Calcula a média das notas
# Aqui, calculamos a média das notas que foram inseridas.
media = sum(notas) / len(notas)  # A soma das notas é dividida pelo número total de notas para obter a média.

# Bloco 3: Verifica se o aluno foi aprovado
# Neste bloco, verificamos se a média é maior ou igual a 7 para decidir se o aluno foi aprovado ou não.
if media >= 7:
    # Se a média for 7 ou mais, o aluno é considerado aprovado.
    print(f"Aluno aprovado com média {media:.2f}")
else:
    # Se a média for menor que 7, o aluno é considerado reprovado.
    print(f"Aluno reprovado com média {media:.2f}")
