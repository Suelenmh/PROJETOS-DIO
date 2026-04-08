comando = input("Digite o comando: ").strip().lower()
if comando == "ls":
    print("lista arquivos do estoque")
elif comando == "rm":
    print("remover arquivo antigo")
elif comando == "cat":
    print("mostrar conteudo do arquivo vendas.txt")
elif comando == "mkdir":
    print("criar nova pasta para promocoes")
else:
    print("comando desconhecido")
'''''''''''''''''
comando = input("Digite o comando: ").strip().lower()

# Estrutura de decisão para os comandos solicitados
if comando == "ls":
    print("lista arquivos e diretorios")
elif comando == "cd":
    print("altera o diretorio atual")
elif comando == "pwd":
    print("mostra o caminho do diretorio atual")
elif comando == "mkdir":
    print("cria um novo diretorio")
else:
    print("comando invalido")

 '''''''''
