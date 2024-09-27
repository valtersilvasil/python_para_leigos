# Bloco 1: Lista de alunos e suas frequências
# Criamos uma lista chamada 'alunos', onde cada elemento é uma tupla contendo
# o nome do aluno e sua frequência em porcentagem.
alunos = [("Ana", 85), ("João", 70), ("Maria", 90)]

# Bloco 2: Define a frequência mínima para aprovação
# Aqui, definimos a frequência mínima necessária para que um aluno seja considerado aprovado.
frequencia_minima = 75

# Bloco 3: Verifica a frequência de cada aluno
# Usamos um loop para percorrer a lista de alunos. 
# Para cada aluno, verificamos sua frequência em relação à frequência mínima.
for aluno, frequencia in alunos:
    if frequencia >= frequencia_minima:
        # Se a frequência do aluno é maior ou igual à mínima, ele está aprovado.
        print(f"{aluno} está aprovado com {frequencia}% de frequência.")
    else:
        # Se a frequência do aluno é menor que a mínima, ele está reprovado.
        print(f"{aluno} está reprovado com {frequencia}% de frequência.")

