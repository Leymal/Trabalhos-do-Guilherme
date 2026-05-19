conjunto = {}
entrada1 = input ("O que você quer fazer hoje?\n1 - Pertinência\n2 - Subconjunto\n3 - Conjunto Verdade\n4 - Proposição composta e Quantificadores\n5 - Sair\n")

while entrada1 != "5":
    if entrada1 == "1":
        
        entrada2 = input ("Você escolheu Pertinência.\nDigite o que você quer fazer:\n1 - Adicionar um conjunto\n2- Adicionar um elemento a um conjunto\n3 - Verificar se um elemento pertence a um conjunto\n4 - Voltar ao menu principal\n",)
        while entrada2 != "4":
            if entrada2 == "1":
                nomeconjunto = input ("Digite o nome do conjunto que você quer criar:\n")
                print("Conjuntos:", conjunto, "\n")
                if nomeconjunto not in conjunto:
                    conjunto[nomeconjunto] = []
                else: print ("Esse conjunto já existe.\n")
                entrada2 = input ("Você escolheu Pertinência.\nDigite o que você quer fazer:\n1 - Adicionar um conjunto\n2- Adicionar um elemento a um conjunto\n3 - Verificar se um elemento pertence a um conjunto\n4 - Voltar ao menu principal\n")
                  

            elif entrada2 == "2":
                print("Conjuntos:", conjunto, "\n")
                nomeconjunto = input ("Digite o nome do conjunto que você quer adicionar um elemento:\n")
                elemento = input ("Digite o elemento que você quer adicionar ao conjunto:\n")
                vetor =  list(map(float, elemento.split(",")))
                if nomeconjunto in conjunto:
                        if vetor not in conjunto[nomeconjunto]:
                            conjunto[nomeconjunto].append(vetor)
                        else:
                            print("Esse elemento já pertence ao conjunto.\n")
                else: print("Esse conjunto não existe.\n")
                entrada2 = input ("Você escolheu Pertinência.\nDigite o que você quer fazer:\n1 - Adicionar um conjunto\n2- Adicionar um elemento a um conjunto\n3 - Verificar se um elemento pertence a um conjunto\n4 - Voltar ao menu principal\n")
                
            elif entrada2 == "3":
                
                nomeconjunto = input ("Digite o nome do conjunto que você quer verificar a pertinência de um elemento:\n")
                elemento = input ("Digite o elemento que você quer verificar se pertence ao conjunto:\n")
                vetor = list(map(float, elemento.split(",")))
                if nomeconjunto in conjunto:
                    if vetor in conjunto[nomeconjunto]:
                        print("O elemento pertence ao conjunto.\n")
                    else: print("O elemento não pertence ao conjunto.\n")
                entrada2 = input ("Você escolheu Pertinência.\nDigite o que você quer fazer:\n1 - Adicionar um conjunto\n2- Adicionar um elemento a um conjunto\n3 - Verificar se um elemento pertence a um conjunto\n4 - Voltar ao menu principal\n")
                
        else: entrada2 = input ("Opção inválida.\nDigite o que você quer fazer:\n1 - Adicionar um conjunto\n2- Adicionar um elemento a um conjunto\n3 - Verificar se um elemento pertence a um conjunto\n4 - Voltar ao menu principal\n")
        
else: entrada1 = input ("Opção inválida.\n1 - Pertinência\n2 - Subconjunto\n3 - Conjunto Verdade\n4 - Proposição composta e Quantificadores\n5 - Sair\n")
print (conjunto)
