# Bloco 1: Função para adicionar tarefas
# Definimos uma função chamada 'adicionar_tarefa', que recebe dois parâmetros:
# 'agenda' (a lista onde as tarefas serão armazenadas) e 'tarefa' (a tarefa a ser adicionada).
def adicionar_tarefa(agenda, tarefa):
    # Usamos o método 'append' para adicionar a nova tarefa ao final da lista 'agenda'.
    agenda.append(tarefa)

# Bloco 2: Cria uma lista vazia para a agenda
# Aqui, criamos uma lista vazia chamada 'agenda', que servirá para armazenar as tarefas que o usuário adicionar.
agenda = []

# Bloco 3: Solicita ao usuário para adicionar tarefas
# Utilizamos um loop 'for' que irá se repetir 3 vezes, permitindo que o usuário adicione 3 tarefas.
for i in range(3):
    # Pedimos ao usuário para digitar a tarefa. O índice 'i' é usado para mostrar ao usuário qual tarefa ele está adicionando.
    tarefa = input(f"Digite a tarefa {i+1}: ")
    # Chamamos a função 'adicionar_tarefa', passando a lista 'agenda' e a 'tarefa' que o usuário informou.
    adicionar_tarefa(agenda, tarefa)

# Bloco 4: Exibe a agenda do dia
# Imprimimos uma mensagem informando que vamos mostrar a agenda do dia.
print("Sua agenda para hoje:")
# Usamos um loop 'for' para percorrer cada tarefa armazenada na lista 'agenda'.
for tarefa in agenda:
    # Para cada tarefa, imprimimos a tarefa precedida por um traço.
    print(f"- {tarefa}")
