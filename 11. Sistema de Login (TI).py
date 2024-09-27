# Bloco 1: Define um usuário e senha válidos
# Aqui estamos criando variáveis que armazenam um nome de usuário e uma senha que consideramos válidos.
usuario_valido = "admin"  # O nome de usuário que aceitamos é "admin".
senha_valida = "1234"  # A senha que aceitamos é "1234".

# Bloco 2: Solicita nome de usuário e senha
# Agora, pedimos ao usuário que insira seu nome de usuário e sua senha.
usuario = input("Digite o nome de usuário: ")  # O que o usuário digitar será armazenado na variável 'usuario'.
senha = input("Digite a senha: ")  # O que o usuário digitar será armazenado na variável 'senha'.

# Bloco 3: Verifica se o usuário e senha estão corretos
# Neste bloco, verificamos se o que o usuário digitou é igual ao que temos como válido.
if usuario == usuario_valido and senha == senha_valida:
    # Se ambos, o nome de usuário e a senha, estiverem corretos, informamos que o login foi bem-sucedido.
    print("Login bem-sucedido!")
else:
    # Se pelo menos um dos dados estiver incorreto, informamos que o usuário ou a senha estão errados.
    print("Usuário ou senha incorretos.")

