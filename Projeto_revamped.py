conjuntos = {}


# Função do menu principal, printa as opções e pede um input (entrada) do usuário
def mostrar_menu_principal():
    return input(
        "\nO que você quer fazer hoje?\n"
        "1 - Pertinência\n"
        "2 - Subconjunto\n"
        "3 - Conjunto Verdade\n"
        "4 - Proposição composta e Quantificadores\n"
        "5 - Sair\n"
    )

# Função do menu de pertinência, printa as opções e pede um input (opção) do usuário
def mostrar_menu_pertinencia():
    return input(
        "\nVocê escolheu Pertinência.\n"
        "1 - Adicionar um conjunto\n"
        "2 - Adicionar um elemento a um conjunto\n"
        "3 - Verificar se um elemento pertence a um conjunto\n"
        "4 - Listar conjuntos\n"
        "5 - Voltar ao menu principal\n"
    )

# Função para listar os conjuntos criados, mostrando o nome do conjunto e seus elementos
def listar_conjuntos(conjuntos):
    print("\nCONJUNTOS")

    if len(conjuntos) == 0: # Lê o dicionário e verifica se ele está vazio
        print("Nenhum conjunto criado.")    # Se o dicionário estiver vazio, printa a mensagem "Nenhum conjunto criado."
    else:
        for nome, elementos in conjuntos.items():   # Para cada nome e seus elementos no dicionário
            print(f"{nome} -> {elementos}")         # Printa o nome do conjunto e seus elementos

    print("=====================\n")

# Função para criar um conjunto
def criar_conjunto(conjuntos):
    nome = input("Digite o nome do conjunto:\n")    # Pede o nome do conjunto

    if nome not in conjuntos:   # Se o nome não estiver no dicionário, ou não existir
        conjuntos[nome] = []    # Cria um novo conjunto com o nome dado e uma lista vazia para os elementos
        print("Conjunto criado com sucesso.\n")     #printa a mensagem de sucesso
    else:
        print("Esse conjunto já existe.\n")     # Se o nome já existir no dicionário, printa um aviso

#Função para adicionar um ou mais elementos a algum conjunto
def adicionar_elemento(conjuntos):
    listar_conjuntos(conjuntos) # Lista os conjuntos para melhor visualização

    nome = input("Digite o nome do conjunto:\n")    # Pede o nome do conjunto

    if nome in conjuntos:       # Se o nome do conjunto estiver no dicionário, ou seja, existir

        elemento = input(   # Pede os elementos a serem adicionados, separados por vírgula para mais de um elemento
            "Digite os elementos numéricos separados por vírgula:\n"
        )

        vetor = list(map(float, elemento.split(",")))   # Separa o vetor (string) em uma lista separados por , além de converter para float
        for numero in vetor:    # Para número no vetor, ou seja, para cada número na lista de elementos a serem adicionados
            if numero not in conjuntos[nome]:   # Se o número não estiver no conjunto com o nome dado
                conjuntos[nome].append(numero)  # Coloca o número no conjunto
                print(f"Elemento {numero} adicionado.\n")   # Mostra o elemento que foi adicionado
            else:
                print(f"Esse elemento {numero} já pertence ao conjunto.\n") # Se não mostra um aviso de que o elemento já pertence ao conjunto

    else:
        print("Esse conjunto não existe.\n")    # Se o nome do conjunto não estiver no dicionário, ou seja, não existir, printa um aviso

# Função para verificar se um elemento pertence a um conjunto
def verificar_pertinencia(conjuntos):
    listar_conjuntos(conjuntos) # Lista os conjuntos para melhor visualização   

    nome = input(   # Pede o nome do conjunto para verificar a pertinência do elemento
        "Digite o nome do conjunto:\n"
    )

    if nome in conjuntos:   # Se o nome do conjunto estiver no dicionário, ou seja, existir

        elemento = input(   # Pede o nome do elemento pra ser verificado
            "Digite o elemento para verificar:\n"
        )

        vetor = list(map(float, elemento.split(",")))   # Separa o vetor (string) em uma lista separado por , além de converter para float

        if vetor in conjuntos[nome]:    # Se o vetor (lista com os elemetos) estiver no conjunto com o nome dado
            print("O elemento pertence ao conjunto.\n") # Printa a mensagem de que o elemento pertence ao conjunto
        else:
            print("O elemento NÃO pertence ao conjunto.\n") # Se não printa a mensagem de que o elemento não pertence ao conjunto

    else:
        print("Esse conjunto não existe.\n")    # Se o nome do conjunto não estiver no dicionário, ou seja, não existir, printa um aviso

# Função do menu de subconjunto, printa as opções e pede um input (opção) do usuário
def menu_pertinencia(conjuntos):

    while True:     # Enquanto o usuário não escolher a opção de voltar ao menu principal, o menu de pertinência continuará aparecendo

        opcao = mostrar_menu_pertinencia()

        if opcao == "1":
            criar_conjunto(conjuntos)   # Chama a função criar conjunto para criar um novo conjunto

        elif opcao == "2":
            adicionar_elemento(conjuntos)   # Chama a função para adicionar um ou mais elementos a um conjunto

        elif opcao == "3":
            verificar_pertinencia(conjuntos)    # Chama a função para verificar se um elemento pertence a um conjunto

        elif opcao == "4":
            listar_conjuntos(conjuntos)     # Chama a função para listar os conjuntos e elementos criados

        elif opcao == "5":      # Para o código do menu de pertinência e volta para o menu principal
            break

        else:
            print("Opção inválida.\n")  # Se o usuário digitar uma opção que não existe, printa a mensagem de opção inválida

# Função do menu de subconjunto, printa as opções e pede um input (opção) do usuário
def menu_subconjunto(conjuntos):
    
    while True: # Enquanto o usuário não escolher a opção de voltar ao menu principal, o menu de subconjunto continuará aparecendo

        opcao = input(  # Pede o input do usuário para escolher a opção do menu de subconjunto
            "\nVocê escolheu Subconjunto.\n"
            "1 - Verificar se um conjunto é subconjunto de outro\n"
            "2 - Voltar ao menu principal\n"
        )

        if opcao == "1":
            for nome, elementos in conjuntos.items():   # Se o nome do conjunto estiver no dicionário com os elementos estiver no dicionário
                print(f"{nome} -> {elementos}") # Printa o nome do conjunto e seus elementos para melhor visualização
            conjuntos_escolhidos = input("Digite os nomes dos conjuntos separados por vírgula e sem espaços (ex: A,B):\n"   # Pede o input
                                         "O primeiro conjunto será verificado se é subconjunto do segundo.\n")
            nomes = [nome.strip() for nome in conjuntos_escolhidos.split(",")]  # Separa os nomes dos conjuntos escolhidos em uma lista, 
                                                                                # removendo espaços em branco
            quantidade = len(nomes) # Conta a quantidade de conjuntos escolhidos para verificar se é subconjunto ou não
                
            if quantidade < 2:
                print("Escolha mais conjuntos para verificar.\n")
                break
            if quantidade > 2:
                print("Escolha apenas dois conjuntos para verificar.\n")
                break
            nome_conjunto1 = nomes[0]   # Define o nome do primeiro conjunto como o primeiro nome da lista de nomes escolhidos
            nome_conjunto2 = nomes[1]   # Define o nome do segundo conjunto como o segundo nome da lista de nomes escolhidos        
            if nome_conjunto1 in conjuntos and nome_conjunto2 in conjuntos: # Se o nome do primeiro conjunto e do segundo estiverem no dicionário segue
                conjunto1 = set(conjuntos[nome_conjunto1])  # Setta o primeiro conjunto, pega os seus elementos sem repetição e coloca em uma variável
                conjunto2 = set(conjuntos[nome_conjunto2])  # Setta o segundo conjunto, pega os seus elementos sem repetição e coloca em uma variável
                for numero in conjunto1:    # Para cada número no primeiro conjunto, ou seja, para cada elemento do primeiro conjunto
                    if numero not in conjunto2: # Se o número não estiver no segundo conjunto, ou seja, se o elemento do primeiro conjunto não estiver no segundo conjunto, segue
                        Nao_subconjunto = True  # Define a variável de que o primeiro conjunto não é subconjunto do segundo como verdadeira
                        if Nao_subconjunto:     # Se a variável acima for verdadeira
                            print(f"O conjunto {nome_conjunto1} NÃO é subconjunto de {nome_conjunto2}.\n")  # Printa que o conjunto 1 não é subconjunto do conjunto 2
                        break
                        
                    else:
                        print(f"O conjunto {nome_conjunto1} é subconjunto de {nome_conjunto2}.\n")  # Se todos os número estiver no segundo 
                        #conjunto, ou seja, se o elemento do primeiro conjunto estiver no segundo conjunto, printa que o conjunto 1 
                        # é subconjunto do conjunto 2

        elif opcao == "2":  # Se o usuário escolher a opção de sair volta ao menu principal
            break

        else:
            print("Opção inválida.\n")  # Se o usuário digitar uma opção que não existe, printa a mensagem de opção inválida


while True: # Enquanto o usuário não escolher a opção de sair, o menu principal continuará aparecendo

    entrada = mostrar_menu_principal()

    if entrada == "1":
        menu_pertinencia(conjuntos)

    elif entrada == "2":
        menu_subconjunto(conjuntos)

    elif entrada == "3":
        print("Conjunto Verdade ainda não implementado.\n")

    elif entrada == "4":
        print("Proposição composta ainda não implementada.\n")

    elif entrada == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.\n")